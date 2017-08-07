# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from django.contrib import admin

from . import views
from . import models
from . import forms

urlpatterns = patterns(
    'agents.views',
    url(r'^appointees/list$', name='appointee_list',
        view=login_required(views.AgentListView.as_view(model=models.Appointee))),
    url(r'^preparers/list$', name='preparer_list',
        view=login_required(views.AgentListView.as_view(model=models.Preparer))),
    url(r'^appointees/new$', name='new_appointee',
        view=login_required(views.AgentCreateUpdateView.as_view(form_class=forms.AppointeeEditform))),
    url(r'^preparers/new$', name='new_preparer',
        view=login_required(views.AgentCreateUpdateView.as_view(form_class=forms.PreparerEditform))),
    url(r'^appointees/(?P<pk>\d+)/edit$', name='edit_appointee',
        view=login_required(views.AgentCreateUpdateView.as_view(form_class=forms.AppointeeEditform))),
    url(r'^preparers/(?P<pk>\d+)/edit$', name='edit_preparer',
        view=login_required(views.AgentCreateUpdateView.as_view(form_class=forms.PreparerEditform))),
    url(r'^appointees/(?P<pk>\d+)/delete$', name='delete_appointee',
        view=login_required(views.AgentDeleteView.as_view(model=models.Appointee))),
    url(r'^preparers/(?P<pk>\d+)/delete$', name='delete_preparer',
        view=login_required(views.AgentDeleteView.as_view(model=models.Preparer))),
)
