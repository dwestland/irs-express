# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import admin

from .views import DocumentList, DocumentScheduleView

urlpatterns = patterns(
    'repository.views',
    url(r'^$', login_required(DocumentList.as_view()), name='documents_list'),
    url(r'tasks/schedule/(?P<pk>\d+)$', permission_required('is_superuser')(DocumentScheduleView.as_view()),
        name='schedule_doc_update'),
)
