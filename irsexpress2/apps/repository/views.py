# -*- coding: utf-8 -*-

from django.views.generic.list import ListView
from django.views.generic.base import View
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied

from .models import DocumentStatus
from .tasks import run_update_for


class DocumentList(ListView):
    model = DocumentStatus
    template_name = 'repository/doc_list.html'


class DocumentScheduleView(View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        if not request.user.is_admin:
            raise PermissionDenied("The user does not have permissions to do this")
        docstatus_id = kwargs['pk']
        ds = get_object_or_404(DocumentStatus, pk=docstatus_id)
        if not ds.scheduled:
            if run_update_for(ds.document_name, force=True):
                ds.scheduled = True
                ds.save()
        return HttpResponse("OK")
