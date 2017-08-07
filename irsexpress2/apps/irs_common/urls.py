# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from . import views
from . import forms

urlpatterns = patterns(
    'irs_common.views',
    url(r'^oic_calculator/(?P<client_id>\d+)?$',
        views.OICCalculatorView.as_view(), name='oic_calculator'),
)
