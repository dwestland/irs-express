# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from irs_common.views import Page1x1EditView, Page1xNEditView
from . import views
from . import forms

urlpatterns = patterns(
    'irs433a.views',
    # page 1
    url(r'^page-1$', view=login_required(views.Page1EditView.as_view()), name='433a-page-1'),
    url(r'^page-1-dependent/(?P<form_prefix>\w+)?$', name='433a-page-1-dependent',
        view=login_required(Page1xNEditView.as_view(form_class=forms.ClientDependentForm))),
    url(r'^page-1-spouse$', name='433a-page-1-spouse',
        view=login_required(Page1x1EditView.as_view(form_class=forms.ClientSpouseForm))),
    # page 2
    url(r'^page-2$', view=login_required(views.Page2EditView.as_view()), name='433a-page-2'),
    url(r'^page-2-emp/(?P<form_prefix>\w+)?$',
        view=login_required(views.Page2EmploymentInfoEditView.as_view()), name='433a-page-2-emp'),
    # page 3
    url(r'^page-3$', view=login_required(views.Page3EditView.as_view()), name='433a-page-3'),
    url(r'^page-3-lawsuit$', name='433a-page-3-lawsuit',
        view=login_required(Page1x1EditView.as_view(form_class=forms.LawsuitPartyInfoForm))),
    url(r'^page-3-bankruptcy$', name='433a-page-3-bankruptcy',
        view=login_required(Page1x1EditView.as_view(form_class=forms.BankruptcyInfoForm))),
    url(r'^page-3-liveabroad$', name='433a-page-3-liveabroad',
        view=login_required(Page1x1EditView.as_view(form_class=forms.LiveAbroadInfoForm))),
    url(r'^page-3-beneficiary$', name='433a-page-3-beneficiary',
        view=login_required(Page1x1EditView.as_view(form_class=forms.BeneficiaryInfoForm))),
    url(r'^page-3-trustee$', name='433a-page-3-trustee',
        view=login_required(Page1x1EditView.as_view(form_class=forms.TrusteeInfoForm))),
    url(r'^page-3-safe$', name='433a-page-3-safe',
        view=login_required(Page1x1EditView.as_view(form_class=forms.SafeInfoForm))),
    url(r'^page-3-trassets$', name='433a-page-3-trassets',
        view=login_required(Page1x1EditView.as_view(form_class=forms.AssetTransferInfoForm))),
    # page 4
    url(r'^page-4$', view=login_required(views.Page4EditView.as_view()), name='433a-page-4'),
    url(r'^page-4-bankaccount/(?P<form_prefix>\w+)?$', name='433a-page-4-bankaccount',
        view=login_required(Page1xNEditView.as_view(form_class=forms.BankAccountInfoForm))),
    url(r'^page-4-investment/(?P<form_prefix>\w+)?$', name='433a-page-4-investment',
        view=login_required(Page1xNEditView.as_view(form_class=forms.InvestmentInfoForm))),
    url(r'^page-4-credit/(?P<form_prefix>\w+)?$', name='433a-page-4-credit',
        view=login_required(Page1xNEditView.as_view(form_class=forms.CreditInfoForm))),
    url(r'^page-4-insurance/(?P<form_prefix>\w+)?$', name='433a-page-4-insurance',
        view=login_required(Page1xNEditView.as_view(form_class=forms.InsuranceInfoForm))),
    # page 5
    url(r'^page-5$', view=login_required(views.Page5EditView.as_view()), name='433a-page-5'),
    url(r'^page-5-realproperty/(?P<form_prefix>\w+)?$', name='433a-page-5-realproperty',
        view=login_required(Page1xNEditView.as_view(form_class=forms.RealPropertyInfoForm))),
    url(r'^page-5-vehicle/(?P<form_prefix>\w+)?$', name='433a-page-5-vehicle',
        view=login_required(Page1xNEditView.as_view(form_class=forms.VehicleInfoForm))),
    url(r'^page-5-personalasset/(?P<form_prefix>\w+)?$', name='433a-page-5-personalasset',
        view=login_required(Page1xNEditView.as_view(form_class=forms.PersonalAssetInfoForm,
                                                    template_name='irs433a/page5personalassetedit.html'))),
    # page 6
    url(r'^page-6$', view=login_required(views.Page6EditView.as_view()), name='433a-page-6'),
    # page 7
    url(r'^page-7$', view=login_required(views.Page7EditView.as_view()), name='433a-page-7'),
    url(r'^page-7-paymentprocessor/(?P<form_prefix>\w+)?$', name='433a-page-7-paymentprocessor',
        view=login_required(Page1xNEditView.as_view(form_class=forms.PaymentProcessorInfoForm))),
    url(r'^page-7-businesscc/(?P<form_prefix>\w+)?$', name='433a-page-7-businesscc',
        view=login_required(Page1xNEditView.as_view(form_class=forms.BusinessCreditCardInfoForm))),
    url(r'^page-7-businessbankacc/(?P<form_prefix>\w+)?$', name='433a-page-7-businessbankacc',
        view=login_required(Page1xNEditView.as_view(form_class=forms.BusinessBankAccountInfoForm))),
    url(r'^page-7-accountsreceivable/(?P<form_prefix>\w+)?$', name='433a-page-7-accountsreceivable',
        view=login_required(Page1xNEditView.as_view(form_class=forms.AccountsReceivableInfoForm))),
    url(r'^page-7-businessasset/(?P<form_prefix>\w+)?$', name='433a-page-7-businessasset',
        view=login_required(Page1xNEditView.as_view(form_class=forms.BusinessAssetInfoForm,
                                                    template_name='irs433a/page7businessassetedit.html'))),
    # page 8
    url(r'^page-8$', view=login_required(views.Page8EditView.as_view()), name='433a-page-8'),
    # get PDF
    url(r'^pdf$', view=login_required(views.get_pdf), name='433a-pdf'),
)
