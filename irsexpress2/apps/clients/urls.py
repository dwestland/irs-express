# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from django.contrib import admin

from .views import (ClientListView, ClientCreateUpdateView, ClientDeleteView,
                    ClientControlPanelView,
                    ClientNotesView, ClientNotesEditView,
                    ClientDocumentsView, ClientDocumentUploadView, return_file)

urlpatterns = patterns(
    'clients.views',
    url(r'^$', login_required(RedirectView.as_view(pattern_name='clients_list', permanent=False)), name='clients_home'),
    url(r'^list$', login_required(ClientListView.as_view()), name='clients_list'),
    url(r'^new$', login_required(ClientCreateUpdateView.as_view()), name='new_client'),
    url(r'^(?P<pk>\d+)/edit$', login_required(ClientCreateUpdateView.as_view()), name='edit_client'),
    url(r'^(?P<pk>\d+)/delete$', login_required(ClientDeleteView.as_view()), name='delete_client'),
    url(r'^(?P<pk>\d+)/control-panel$', login_required(ClientControlPanelView.as_view()), name='client_cp'),
    url(r'^(?P<pk>\d+)/notes$', login_required(ClientNotesView.as_view()), name='client_notes'),
    url(r'^(?P<pk>\d+)/notes/edit/(?P<note_pk>\d+)?$', login_required(ClientNotesEditView.as_view()),
        name='client_note_edit'),
    url(r'^(?P<pk>\d+)/docs$', login_required(ClientDocumentsView.as_view()), name='client_docs'),
    url(r'^(?P<pk>\d+)/docs/upload/(?P<doc_pk>\d+)?$', login_required(ClientDocumentUploadView.as_view()),
        name='client_doc_upload'),
    url(r'^(?P<pk>\d+)/document/(?P<uuid>\w+)$', login_required(return_file), name='get_client_doc'),
    # include Form433-a URLs
    url(r'^(?P<client_id>\d+)/irs433a/', include('irs433a.urls')),
    # include Form656 URLs
    url(r'^(?P<client_id>\d+)/irs656/', include('irs656.urls')),
    # include Form8821 URLs
    url(r'^(?P<client_id>\d+)/irs8821/', include('irs8821.urls')),
    # include Form9465 URLs
    url(r'^(?P<client_id>\d+)/irs9465/', include('irs9465.urls')),
)
