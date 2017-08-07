# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from irs_common.views import Page1x1EditView, Page1xNEditView
from . import views
from . import forms

urlpatterns = patterns(
    'irs656.views',
    # page 1
    url(r'^page-1$', view=login_required(views.Page1EditView.as_view()), name='656-page-1'),
    url(r'^page-1-jointoffer$', name='656-page-1-jointoffer',
        view=login_required(Page1x1EditView.as_view(form_class=forms.ClientSpouseForm))),
    url(r'^page-1-mailingaddr$', name='656-page-1-mailingaddr',
        view=login_required(Page1x1EditView.as_view(form_class=forms.MailingAddressForm))),
    url(r'^page-1-businessinfo$', name='656-page-1-businessinfo',
        view=login_required(Page1x1EditView.as_view(form_class=forms.BusinessInformationForm))),
    # page 2
    url(r'^page-2$', view=login_required(views.Page2EditView.as_view()), name='656-page-2'),
    url(r'^page-2-businesstaxdebt$', name='656-page-2-businesstaxdebt',
        view=login_required(Page1x1EditView.as_view(form_class=forms.BusinessTaxDebtForm))),
    # page 3
    url(r'^page-3$', view=login_required(views.Page3EditView.as_view()), name='656-page-3'),
    # page 4
    url(r'^page-4$', view=login_required(views.Page4EditView.as_view()), name='656-page-4'),
    # page 5
    url(r'^page-5$', view=login_required(views.Page5EditView.as_view()), name='656-page-5'),
    # page 6
    url(r'^page-6$', view=login_required(views.Page6EditView.as_view()), name='656-page-6'),
    # page 7
    url(r'^page-7$', view=login_required(views.Page7EditView.as_view()), name='656-page-7'),
    # get PDF
    url(r'^pdf$', view=login_required(views.get_pdf), name='656-pdf'),
)
