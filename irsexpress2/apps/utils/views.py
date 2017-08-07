# -*- coding: utf-8 -*-

from django.views.generic.detail import SingleObjectTemplateResponseMixin, SingleObjectMixin
from django.views.generic.edit import ModelFormMixin, ProcessFormView
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
from django.forms import ValidationError
from django.db import models


class MultiFormViewMixin(object):

    def instance_exists(self, data):
        return data.get('id') and not data.get('new')

    def get_form_extended(self, form_class, data, **form_kwargs):
        if self.instance_exists(data):
            model = form_class._meta.model
            try:
                instance = model.objects.get(pk=data['id'])
            except model.DoesNotExist:
                raise ValidationError(
                    form_class.__name__, "%s with given id (#%s) wasn't found" % (model.__name__, data['id']))
        else:
            instance = None
        user = self.request.user
        form = form_class(data, instance=instance, **form_kwargs)
        return form

    def process_form(self, form_class, data, commit=True, **form_kwargs):
        """Helper for ModelForm processing.

        Fetches instance from db if 'id' in the data and no 'new' flag
        is specified. Creates form. Asserts that form is valid. Returns
        result of form.save(commit=commit) method.
        """
        form = self.get_form_extended(form_class, data, **form_kwargs)
        self.assert_form_is_valid(form)
        return form.save(commit=commit)

    def assert_form_is_valid(self, form):
        if not form.is_valid():
            title = type(form).__name__ + ' %s'
            raise ValidationError([(title % error[0], e_msg) for error in form.errors.items() for e_msg in error[1]])


class ObjectBaseMixin(object):
    def get_context_object_name(self, obj):
        """ Get the name to use for the object. """
        if self.context_object_name:
            return self.context_object_name
        elif isinstance(obj, (models.Model, models.base.ModelBase)):
            return obj._meta.model_name
        elif self.model:
            return self.model._meta.model_name
        else:
            return ''

    def get_object(self, queryset=None):
        try:
            retval = super().get_object(queryset)
            return retval
        except AttributeError:
            return None

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['object_name'] = self.get_context_object_name(self.model)
        context['object_title'] = context['object_name'].title()
        context['new_object_urlname'] = "new_%s" % context['object_name']
        context['edit_object_urlname'] = "edit_%s" % context['object_name']
        context['delete_object_urlname'] = "delete_%s" % context['object_name']
        context['list_object_urlname'] = "%s_list" % context['object_name']
        return context


class ObjectBaseView(SingleObjectTemplateResponseMixin, ObjectBaseMixin):
    model = None  # redefine this!
    success_url_name = None
    edit_admin_only = False
    edit_author_object = False
    basetemplate = 'base.html'
    baseajaxtemplate = 'partials/popupform.html'

    def dispatch(self, request, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if self.object:
            print(self.object.pk)
            if hasattr(self.object, 'can_be_edited'):
                if not self.object.can_be_edited(request.user):
                    raise PermissionDenied("The user does not have permissions to do this")
            elif self.edit_admin_only and not request.user.is_admin:
                raise PermissionDenied("The user does not have permissions to do this")
        return super().post(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # context['object_name'] = self.get_context_object_name(self.model)
        # context['object_title'] = context['object_name'].title()
        # context['new_object_urlname'] = "new_%s" % context['object_name']
        # context['edit_object_urlname'] = "edit_%s" % context['object_name']
        # context['list_object_urlname'] = "%s_list" % context['object_name']
        context['basetemplate'] = self.basetemplate
        context['ajax'] = False
        if self.request.is_ajax():
            context['ajax'] = True
            context['basetemplate'] = self.baseajaxtemplate
        return context

    def get_success_url(self):
        return reverse(self.success_url_name)


class BaseCreateUpdateView(ObjectBaseView, ModelFormMixin, ProcessFormView):
    template_name = None
    form_class = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.form_class and hasattr(self.form_class, 'prefix') and self.form_class.prefix:
            self.form_prefix = self.form_class.prefix
        if self.form_class and not self.model:
            self.model = self.form_class._meta.model
