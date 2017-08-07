# -*- coding: utf-8 -*-

import re
import json

from django.shortcuts import redirect
from django.http import HttpResponse, Http404

from irs_common.views import BaseFView, IRSBasePageEditView
from clients.models import Client
from .models import (F433aPage1, ClientDependent, ClientSpouse,
                     F433aPage2, EmploymentInfo,
                     F433aPage3, LawsuitPartyInfo, BankruptcyInfo, BeneficiaryInfo,
                     LiveAbroadDetails, TrusteeDetails, SafeDetails, AssetTransferDetails,
                     F433aPage4,
                     F433aPage5,
                     F433aPage6,
                     F433aPage7,
                     F433aPage8,
                     )
from .forms import (Page1Form, ClientDependentForm, ClientSpouseForm,
                    Page2Form, EmploymentInfoForm,
                    Page3Form, LawsuitPartyInfoForm, BankruptcyInfoForm, BeneficiaryInfoForm,
                    LiveAbroadInfoForm, TrusteeInfoForm, SafeInfoForm, AssetTransferInfoForm,
                    Page4Form, BankAccountInfoForm, InvestmentInfoForm, CreditInfoForm, InsuranceInfoForm,
                    Page5Form, RealPropertyInfoForm, VehicleInfoForm, PersonalAssetInfoForm,
                    Page6Form,
                    Page7Form, PaymentProcessorInfoForm, BusinessCreditCardInfoForm,
                    BusinessBankAccountInfoForm, AccountsReceivableInfoForm, BusinessAssetInfoForm,
                    Page8Form,
                    )
from .tasks import fill_form_433a
from .utils import (get_suggested_foodclothing, get_suggested_oop_healthcare, get_suggested_housing,
                    get_suggested_vehicle_oper, get_suggested_vehicle_own, get_suggested_pub_transport)


class BasePageEditView(IRSBasePageEditView):
    template_name = 'irs433a/form_base.html'
    formnameid = '433A'


class Page1EditView(BasePageEditView):
    success_url_name = '433a-page-2'
    back_url_name = ''
    form_class = Page1Form
    template_name = 'irs433a/page1edit.html'
    active_page = 'is_page1_active'
    subforms = {
        'dependent': {'form_class': ClientDependentForm, 'instattr': None,
                      'prefix-rex': re.compile(r'^dependent_(\d+)\-', re.I)},
        'spouse': {'form_class': ClientSpouseForm, 'instattr': 'spouse'},
    }
    prev_btn_title = ""


class Page2EditView(BasePageEditView):
    success_url_name = '433a-page-3'
    back_url_name = '433a-page-1'
    form_class = Page2Form
    template_name = 'irs433a/page2edit.html'
    active_page = 'is_page2_active'
    subforms = {
        'taxpayer': {'form_class': EmploymentInfoForm, 'instattr': 'employment_info'},
        'spouse': {'form_class': EmploymentInfoForm, 'instattr': 'spouse_employment_info'},
    }


class Page2EmploymentInfoEditView(BaseFView):
    form_class = EmploymentInfoForm
    template_name = 'irs433a/page2employmentinfoedit.html'
    form_prefix = 'unknown'

    def get_object(self, queryset=None):
        try:
            form_prefix = self._kwargs.get('form_prefix')
            if form_prefix == 'taxpayer':
                return self.model.objects.get(page2_as_taxpayer__form__client_id=self._kwargs['client_id'])
            elif form_prefix == 'spouse':
                return self.model.objects.get(page2_as_spouse__form__client_id=self._kwargs['client_id'])
        except:
            pass
        return None


class Page3EditView(BasePageEditView):
    success_url_name = '433a-page-4'
    back_url_name = '433a-page-2'
    form_class = Page3Form
    template_name = 'irs433a/page3edit.html'
    active_page = 'is_page3_active'
    subforms = {
        'lawsuit': {'form_class': LawsuitPartyInfoForm, 'instattr': 'lawsuit_party'},
        'bankruptcy': {'form_class': BankruptcyInfoForm, 'instattr': 'bankruptcy'},
        'liveabroad': {'form_class': LiveAbroadInfoForm, 'instattr': 'liveabroad'},
        'beneficiary': {'form_class': BeneficiaryInfoForm, 'instattr': 'beneficiary'},
        'trustee': {'form_class': TrusteeInfoForm, 'instattr': 'trustee'},
        'safe': {'form_class': SafeInfoForm, 'instattr': 'safe'},
        'trassets': {'form_class': AssetTransferInfoForm, 'instattr': 'asset_transfer'},
    }


class Page4EditView(BasePageEditView):
    success_url_name = '433a-page-5'
    back_url_name = '433a-page-3'
    form_class = Page4Form
    template_name = 'irs433a/page4edit.html'
    active_page = 'is_page4_active'
    subforms = {
        'bankaccount': {'form_class': BankAccountInfoForm, 'instattr': None,
                        'prefix-rex': re.compile(r'^bankaccount_(\d+)\-', re.I)},
        'investment': {'form_class': InvestmentInfoForm, 'instattr': None,
                       'prefix-rex': re.compile(r'^investment_(\d+)\-', re.I)},
        'credit': {'form_class': CreditInfoForm, 'instattr': None,
                   'prefix-rex': re.compile(r'^credit_(\d+)\-', re.I)},
        'insurance': {'form_class': InsuranceInfoForm, 'instattr': None,
                      'prefix-rex': re.compile(r'^insurance_(\d+)\-', re.I)},
    }


class Page5EditView(BasePageEditView):
    success_url_name = '433a-page-6'
    back_url_name = '433a-page-4'
    form_class = Page5Form
    template_name = 'irs433a/page5edit.html'
    active_page = 'is_page5_active'
    subforms = {
        'realproperty': {'form_class': RealPropertyInfoForm, 'instattr': None,
                         'prefix-rex': re.compile(r'^realproperty_(\d+)\-', re.I)},
        'vehicle': {'form_class': VehicleInfoForm, 'instattr': None,
                    'prefix-rex': re.compile(r'^vehicle_(\d+)\-', re.I)},
        'personalasset': {'form_class': PersonalAssetInfoForm, 'instattr': None,
                          'prefix-rex': re.compile(r'^personalasset_(\d+)\-', re.I)},
    }


class Page6EditView(BasePageEditView):
    success_url_name = '433a-page-7'
    back_url_name = '433a-page-5'
    form_class = Page6Form
    template_name = 'irs433a/page6edit.html'
    active_page = 'is_page6_active'
    subforms = {
        # 'xxx': {'form_class': XXXInfoForm, 'instattr': None,
        #                  'prefix-rex': re.compile(r'^xxx_(\d+)\-', re.I)},
    }

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['suggestions'] = self.get_suggestions(self._kwargs['client_id'])
        return kwargs

    def get_suggestions(self, client):
        if not hasattr(self, '_suggestions'):
            if not isinstance(client, Client):
                client = Client.objects.get(pk=client)
            self._suggestions = []

            foodclothing = get_suggested_foodclothing(client)
            if foodclothing:
                foodclothing['class'] = 'suggestion sugg-foodclothing'
                foodclothing['element-selector'] = 'label[for="id_food_clothing"]'
                self._suggestions.append(foodclothing)

            oop_hc = get_suggested_oop_healthcare(client)
            if oop_hc:
                oop_hc['class'] = 'suggestion sugg-oop_healthcare'
                oop_hc['element-selector'] = 'label[for="id_oop_healthcare"]'
                self._suggestions.append(oop_hc)

            housing = get_suggested_housing(client)
            if housing:
                housing['class'] = 'suggestion sugg-housing'
                housing['element-selector'] = 'label[for="id_housing"]'
                self._suggestions.append(housing)

            vehicle_oper = get_suggested_vehicle_oper(client)
            if vehicle_oper:
                vehicle_oper['class'] = 'suggestion sugg-vehicle_oper'
                vehicle_oper['element-selector'] = 'label[for="id_vehicle_oper"]'
                self._suggestions.append(vehicle_oper)

            vehicle_own = get_suggested_vehicle_own(client)
            if vehicle_own:
                vehicle_own['class'] = 'suggestion sugg-vehicle_own'
                vehicle_own['element-selector'] = 'label[for="id_vehicle_own"]'
                self._suggestions.append(vehicle_own)

            pub_transport = get_suggested_pub_transport(client)
            if pub_transport:
                pub_transport['class'] = 'suggestion sugg-pub_transport'
                pub_transport['element-selector'] = 'label[for="id_pub_transport"]'
                self._suggestions.append(pub_transport)

        return self._suggestions

    def get_context_data(self, *args, **kwargs):
        # On this page we should calculate some suggestions for the user basing on previous values
        context = super().get_context_data(*args, **kwargs)
        suggestions = self.get_suggestions(context['client'])
        suggestions = json.dumps(suggestions)
        context['suggestions'] = suggestions
        return context


class Page7EditView(BasePageEditView):
    success_url_name = '433a-page-8'
    back_url_name = '433a-page-6'
    form_class = Page7Form
    template_name = 'irs433a/page7edit.html'
    active_page = 'is_page7_active'
    subforms = {
        'paymentprocessor': {'form_class': PaymentProcessorInfoForm, 'instattr': None,
                             'prefix-rex': re.compile(r'^paymentprocessor_(\d+)\-', re.I)},
        'businesscc': {'form_class': BusinessCreditCardInfoForm, 'instattr': None,
                       'prefix-rex': re.compile(r'^businesscc_(\d+)\-', re.I)},
        'businessbankacc': {'form_class': BusinessBankAccountInfoForm, 'instattr': None,
                            'prefix-rex': re.compile(r'^businessbankacc_(\d+)\-', re.I)},
        'accountsreceivable': {'form_class': AccountsReceivableInfoForm, 'instattr': None,
                               'prefix-rex': re.compile(r'^accountsreceivable_(\d+)\-', re.I)},
        'businessasset': {'form_class': BusinessAssetInfoForm, 'instattr': None,
                          'prefix-rex': re.compile(r'^businessasset_(\d+)\-', re.I)},
    }

    def post(self, *args, **kwargs):
        if self.request.POST.get('is_self_employed', '').lower() != 'true':
            # not self employed, sections 6 and 7 should not be used, deleting
            f7qs = F433aPage7.objects.filter(form__client_id=self._kwargs['client_id'])
            if f7qs.exists():
                f7 = f7qs[0]
                f7.delete()
            f8qs = F433aPage8.objects.filter(form__client_id=self._kwargs['client_id'])
            if f8qs.exists():
                f8 = f8qs[0]
                f8.delete()
            return HttpResponse("OK")
        return super().post(*args, **kwargs)


class Page8EditView(BasePageEditView):
    success_url_name = 'client_cp'
    back_url_name = '433a-page-7'
    form_class = Page8Form
    template_name = 'irs433a/page8edit.html'
    active_page = 'is_page8_active'
    subforms = {
        # 'xxx': {'form_class': XXXInfoForm, 'instattr': None,
        #                  'prefix-rex': re.compile(r'^xxx_(\d+)\-', re.I)},
    }
    next_btn_title = 'Done'

    def get(self, *args, **kwargs):
        # if there is no page7 ready yet - that means client did not choose "self-employed"
        # first we want to fill Section 6
        f7qs = F433aPage7.objects.filter(form__client_id=self._kwargs['client_id'])
        if not f7qs.exists():
            return redirect('433a-page-7', client_id=self._kwargs['client_id'])
        return super().get(*args, **kwargs)


# ------------------------------------------------------------------------------

def get_pdf(request, client_id):
    try:
        pdf_data = fill_form_433a(client_id=client_id, return_value=True)
        response = HttpResponse(pdf_data, content_type='application/pdf')
        filename = "Form433a.pdf"
        response['Content-Disposition'] = 'attachment; filename="%s"' % filename
        return response
    except FileNotFoundError:
        raise Http404("File not found")
