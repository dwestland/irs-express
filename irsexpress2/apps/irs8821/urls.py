# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from irs_common.views import Page1x1EditView, Page1xNEditView
from . import views
from . import forms

urlpatterns = patterns(
    'irs8821.views',
    # Taxpayer
    # page 1
    url(r'^page-1$', view=login_required(views.Page1EditView.as_view()), name='8821-page-1'),
    url(r'^page-1-specific_use$', name='8821-page-1-specific_use',
        view=login_required(Page1x1EditView.as_view(form_class=forms.SpecificUseForm))),
    # page 2
    url(r'^page-2$', view=login_required(views.Page2EditView.as_view()), name='8821-page-2'),
    url(r'^page-2-tax_info/(?P<form_prefix>\w+)?$', name='8821-page-2-tax_info',
        view=login_required(Page1xNEditView.as_view(form_class=forms.TaxInformationForm))),
    # get PDF
    url(r'^pdf$', view=login_required(views.get_pdf), name='8821-pdf'),
    # Spouse
    # page 1
    url(r'^spouse-page-1$', view=login_required(views.Page1SpouseEditView.as_view()), name='spouse-8821-page-1'),
    url(r'^spouse-page-1-specific_use$', name='spouse-8821-page-1-specific_use',
        view=login_required(Page1x1EditView.as_view(form_class=forms.SpecificUseSpouseForm))),
    # page 2
    url(r'^spouse-page-2$', view=login_required(views.Page2SpouseEditView.as_view()), name='spouse-8821-page-2'),
    url(r'^spouse-page-2-tax_info/(?P<form_prefix>\w+)?$', name='spouse-8821-page-2-tax_info',
        view=login_required(Page1xNEditView.as_view(form_class=forms.TaxInformationSpouseForm))),
    # get PDF
    url(r'^spouse-pdf$', view=login_required(views.get_spouse_pdf), name='spouse-8821-pdf'),
)
