# -*- coding: utf-8 -*-

import re
import json
from collections import defaultdict

from django.core.urlresolvers import reverse, resolve
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.http import HttpResponse, Http404

from utils.views import BaseCreateUpdateView, MultiFormViewMixin
from .forms import OICCalculatorForm


class BaseFView(BaseCreateUpdateView):
    form_prefix = None
    self_url_name = None
    active_page = None
    formnameid = None  # 433a or 656 or etc

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['client'] = kwargs['form'].client
        context['self_url_name'] = self.self_url_name
        context['formnameid'] = self.formnameid
        context['page_active'] = self.active_page
        context['success_url_name'] = self.success_url_name
        context[self.active_page] = 'active'
        form_prefix = self._kwargs.get('form_prefix')
        self.form_prefix = form_prefix or self.form_prefix
        context['prefix'] = self.form_prefix
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['client_id'] = self._kwargs['client_id']
        kwargs['object'] = self.object
        form_prefix = self._kwargs.get('form_prefix')
        self.form_prefix = form_prefix or self.form_prefix
        if self.form_prefix:
            kwargs['prefix'] = self.form_prefix
        return kwargs

    def get_success_url(self):
        return reverse(self.success_url_name, kwargs={'client_id': self._kwargs['client_id']})


class Page1x1EditView(BaseFView):
    model = None
    success_url_name = '433a-page-1'
    form_class = None
    template_name = 'irs_common/form1x1edit.html'
    active_page = 'is_page1_active'
    form_prefix = 'unknown'

    def get_object(self, queryset=None):
        try:
            return self.model.objects.get(page__form__client_id=self._kwargs['client_id'])
        except:
            pass
        return None


class Page1xNEditView(BaseFView):
    model = None
    success_url_name = '433a-page-1'
    form_class = None
    template_name = 'irs_common/form1xnedit.html'
    active_page = 'is_page1_active'
    form_prefix = 'unknown'

    def get_object(self, queryset=None):
        try:
            all_objects = self.model.objects.filter(formpage__form__client_id=self._kwargs['client_id']).order_by('-id')
            index = int(self._kwargs['form_prefix'].split('_')[-1]) - 1
            return all_objects[index]
        except Exception as ee:
            print("Exception (%s): %s" % (type(ee), str(ee)))
        return None


class IRSBasePageEditView(BaseFView, MultiFormViewMixin):
    """ Base class for Page views """
    template_name = 'irs_common/form_base.html'
    subforms = {}
    back_url_name = 'client_cp'
    prev_btn_title = 'Prev Page'
    next_btn_title = 'Next Page'

    def get_context_data(self, *args, **kwargs):
        current_url = resolve(self.request.path_info).url_name
        context = super().get_context_data(*args, **kwargs)
        # for the subforms: tuple(prefix, classname, url)
        context['subforms'] = tuple((sfi['form_class'].prefix,
                                     sfi['form_class'].subform_classname,
                                     "%s-%s" % (current_url, sfi['form_class'].prefix))
                                    for sfn, sfi in self.subforms.items())
        context['back_url_name'] = self.back_url_name
        context['prev_btn_title'] = self.prev_btn_title
        context['next_btn_title'] = self.next_btn_title
        return context

    def get_object(self, queryset=None):
        try:
            return self.model.objects.get(form__client_id=self._kwargs['client_id'])
        except:
            pass
        return None

    def validate_subforms(self, *args, **kwargs):
        # print("POST: %s" % self.request.POST)
        validation_errors = []
        subform_params, common_params = defaultdict(dict), {}
        subforms = dict.fromkeys(self.subforms)
        for param in self.request.POST:
            for sfname in self.subforms:
                if 'prefix-rex' in self.subforms[sfname]:
                    mtch = self.subforms[sfname]['prefix-rex'].match(param)
                    if mtch:  # parameter belongs to 1xN subform
                        sf_num = mtch.group(1)
                        sfname_new = "%s_%s" % (sfname, sf_num)
                        subform_params[sfname_new][param[len(mtch.group(0)):]] = self.request.POST.get(param)
                        if sfname_new not in subforms:
                            subforms[sfname_new] = self.subforms[sfname]['form_class']
                        break
                if param.startswith('%s-' % sfname):
                    subform_params[sfname][param[len(sfname) + 1:]] = self.request.POST.get(param)
                    if not subforms.get('sfname'):
                        subforms[sfname] = self.subforms[sfname]['form_class']
                    break
            else:
                common_params[param] = self.request.POST.get(param)

        for sfname in subform_params:
            # print("%s_params: %s" % (sfname, subform_params[sfname]))
            subform_params[sfname]['formpage'] = self.object
            subforms[sfname] = self.get_form_extended(subforms[sfname], subform_params[sfname],
                                                      client_id=self._kwargs['client_id'])
            if not subforms[sfname].is_valid():
                validation_errors.extend([("%s-%s" % (sfname, e), l) for e, l in subforms[sfname].errors.items()])
        # print("common_params: %s" % common_params)
        mainform = self.get_form_extended(self.form_class, common_params, client_id=self._kwargs['client_id'])
        if not mainform.is_valid():
            validation_errors.extend(mainform.errors.items())
        if self.request.is_ajax():
            if validation_errors:
                return HttpResponse(json.dumps(validation_errors))
            return (mainform, subforms)
        raise Exception("This URL should be called with AJAX only")

    def save_subforms(self, mainform, subforms):
        # processing 1x1 subforms
        for sfname in self.subforms:
            instattr = self.subforms[sfname].get('instattr')
            if instattr:
                # 'instattr' - attribute name on the 'page' object
                # if it exists - we assume this is 1x1 relation
                if subforms[sfname]:
                    subform = subforms[sfname].save()
                    setattr(mainform.instance, instattr, subform)
                else:
                    subform = getattr(mainform.instance, instattr)
                    if subform:
                        subform.delete()
                del subforms[sfname]
                continue
        page = mainform.save()
        # processing 1xN subforms
        new_1xn_ids = dict((finfo['form_class']._meta.model, [])
                           for _, finfo in self.subforms.items()
                           if not finfo.get('instattr'))
        for sfname in subforms:
            # no 'instattr' - then this is 1xN relation
            #         and link should be set on the sub-component's side to page
            # OR 'sfname' not in self.subforms - unknown form?
            if subforms[sfname]:
                subforms[sfname].instance.formpage = page
                subform = subforms[sfname].save()
                new_1xn_ids[subform.__class__].append(subform.id)
        # delete all old objects
        for fclass, new_ids in new_1xn_ids.items():
            fclass.objects.filter(formpage_id=page.id).exclude(id__in=new_ids).delete()
        return page

    def post(self, *args, **kwargs):
        validate_result = self.validate_subforms()
        if isinstance(validate_result, HttpResponse):
            # validation errors, response has been already prepared
            return validate_result
        # everything is ok
        if self.request.POST.get('do_form_save') == 'true':
            mainform, subforms = validate_result
            page2 = self.save_subforms(mainform, subforms)
        return HttpResponse("OK")


class OICCalculatorView(BaseFView):
    template_name = 'irs_common/oic_calculator.html'
    form_class = OICCalculatorForm
