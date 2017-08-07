# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from irs_common.views import Page1x1EditView, Page1xNEditView
from . import views
from . import forms

urlpatterns = patterns(
    'irs9465.views',
    # page 1
    url(r'^page-1$', view=login_required(views.Page1EditView.as_view()), name='9465-page-1'),
    url(r'^page-1-jointoffer$', name='9465-page-1-jointoffer',
        view=login_required(Page1x1EditView.as_view(form_class=forms.ClientSpouseForm))),
    # page 2
    url(r'^page-2$', view=login_required(views.Page2EditView.as_view()), name='9465-page-2'),
    # page 3
    url(r'^page-3$', view=login_required(views.Page3EditView.as_view()), name='9465-page-3'),
    # page 4
    url(r'^page-4$', view=login_required(views.Page4EditView.as_view()), name='9465-page-4'),
    # get PDF
    url(r'^pdf$', view=login_required(views.get_pdf), name='9465-pdf'),
)
