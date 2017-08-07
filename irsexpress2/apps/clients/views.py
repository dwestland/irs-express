# -*- coding: utf-8 -*-

import logging
import json

from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, BaseDetailView
from django.views.generic.edit import FormView, UpdateView, CreateView, ModelFormMixin, ProcessFormView, DeleteView
from django.core.exceptions import PermissionDenied
from django.template.context_processors import csrf

from django.http import HttpResponse, HttpResponseBadRequest, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import F, Value as V, Q
from django.db.models.functions import Concat
from django.core.urlresolvers import reverse
from django.conf import settings

from utils.views import ObjectBaseView
from .models import Client, ClientNote, ClientDocument, CLIENT_STATUS
from .forms import ClientEditForm, ClientNoteEditForm, ClientDocumentUploadForm

logger = logging.getLogger('main')


class ClientListView(ListView):
    model = Client
    template_name = 'clients/clients_home.html'

    def get_pagination_page(self, page=1, maxitems=settings.CLIENTS_PAGINATE_BY, filters=None,
                            sortfield=None, sortasc='1'):
        items = self.get_objects()
        if filters:
            ifilter = Q()
            istatusfilter = Q(email=None)  # means 'nothing'
            filter_enabled = True
            for ff in filters:
                ffs = ff.split('*', 1)
                if len(ffs) > 1:
                    fname, fvalue = ffs
                    if fvalue and fname == 'clientfilter':
                        ifilter |= Q(display_name__icontains=fvalue)
                        ifilter |= Q(email__icontains=fvalue)
                        filter_enabled = True
                    if fvalue and fname == 'status[]':
                        istatusfilter |= Q(status=fvalue)
                        filter_enabled = True
            if filter_enabled:
                ifilter &= istatusfilter
                items = items.filter(ifilter)
        if sortfield:
            if sortasc == '0':
                items = items.order_by("-%s" % sortfield)
            else:
                items = items.order_by("%s" % sortfield)
        paginator = Paginator(items, maxitems)
        try:
            page = int(page)
        except ValueError:
            page = 1

        try:
            items = paginator.page(page)
        except (EmptyPage, InvalidPage):
            items = paginator.page(paginator.num_pages)

        return items

    def get_context_data(self, page=1, maxitems=settings.CLIENTS_PAGINATE_BY, is_ajax=False):
        context = {}
        context['items'] = self.get_pagination_page(page, maxitems)
        context['prelast'] = context['items'].paginator.num_pages - 1
        context['active_clients'] = self.get_active_clients()
        return context

    def get_objects(self):
        return self.model.objects.all().annotate(display_name=Concat('first_name', V(' '), 'last_name'))

    def get_active_clients(self):
        return self.model.objects.filter(status='active').\
            annotate(display_name=Concat('first_name', V(' '), 'last_name')).\
            order_by('stage_change_date', '-stage', 'case_opened')

    def get(self, request):
        if not request.is_ajax():
            return super().get(request)
        page = request.GET.get('page', 1)
        filters = request.GET.getlist('filters[]', [])
        maxitems = request.GET.get('maxitems', settings.CLIENTS_PAGINATE_BY)
        sortfield = request.GET.get('sort', 'id')
        sortasc = str(request.GET.get('asc', '1'))
        items = self.get_pagination_page(page, maxitems, filters, sortfield, sortasc)
        prelast = items.paginator.num_pages - 1
        return render_to_response('clients/client_list.html', {'items': items, 'prelast': prelast})


class ClientBaseView(ObjectBaseView):
    model = Client
    success_url_name = 'clients_list'


class ClientDeleteView(DeleteView):
    model = Client

    def get_success_url(self):
        return reverse('clients_list')


class ClientCreateUpdateView(ClientBaseView, ModelFormMixin, ProcessFormView):
    template_name = 'clients/client_edit_form.html'
    form_class = ClientEditForm
    success_url_name = 'client_cp'

    def get_success_url(self):
        return reverse('client_cp', kwargs={'pk': self.object.pk})


class ClientControlPanelView(ClientBaseView, DetailView):
    template_name = 'clients/client_cp_form.html'

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            context = self.get_context_data()
            context.update({'cp_edit_enabled': request.GET.get('ee', 'false').lower() == 'true',
                            'user': request.user})
            return render_to_response("clients/client_cp_header.html", context=context)
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        if not request.is_ajax():
            return super().put(request, *args, **kwargs)
        params = json.loads(request.body.decode('utf-8'))
        if 'status' in params:
            if params['status'] in (c[0] for c in CLIENT_STATUS):
                self.object.status = params['status']
            else:
                params.pop('status')
        if 'summary' in params:
            self.object.summary = params['summary']
        if 'stage' in params:
            stage = int(params['stage'])
            if self.object.is_stage_correct(stage):
                if not request.user.is_admin and stage < self.object.stage:
                    raise PermissionDenied("The user has no permission to do this!")
                self.object.set_stage(stage, request.user.id, save=False)
            else:
                params.pop('stage')
        # Save object
        if params:
            self.object.save()
        data = {
            'id': self.object.pk,
            'status': self.object.status, 'status_display': self.object.get_status_display(),
        }
        # data.update(csrf(request))
        return HttpResponse(json.dumps(data), content_type='application/json')


class ClientNotesView(ClientBaseView, DetailView):
    template_name = 'clients/client_notes_form.html'

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            context = self.get_context_data()
            context.update({'note_edit_enabled': request.GET.get('ee', 'false').lower() == 'true',
                            'user': request.user})
            return render_to_response("clients/notes_list.html", context=context)
        return super().get(request, *args, **kwargs)


class ClientNotesEditView(ObjectBaseView, ModelFormMixin, ProcessFormView):
    template_name = 'clients/client_note_edit.html'
    model = ClientNote
    form_class = ClientNoteEditForm
    success_url_name = 'client_notes'
    pk_url_kwarg = 'note_pk'
    edit_admin_only = True
    edit_author_object = True

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['client_id'] = self._kwargs['pk']
        return kwargs

    def delete(self, request, *args, **kwargs):
        if not self.object.can_be_edited(request.user):
            raise PermissionDenied("The user does not have permissions to do this")
        self.object.delete()
        return HttpResponse("refresh")

    def get_success_url(self):
        return reverse(self.success_url_name, kwargs={'pk': self._kwargs['pk']})


class ClientDocumentsView(ClientBaseView, DetailView):
    template_name = 'clients/client_docs.html'

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            context = self.get_context_data()
            context.update({'note_edit_enabled': request.GET.get('ee', 'false').lower() == 'true',
                            'user': request.user})
            return render_to_response("clients/documents_list.html", context=context)
        return super().get(request, *args, **kwargs)


class ClientDocumentUploadView(ObjectBaseView, ModelFormMixin, ProcessFormView):
    template_name = 'clients/client_doc_upload.html'
    model = ClientDocument
    form_class = ClientDocumentUploadForm
    success_url_name = 'client_docs'
    pk_url_kwarg = 'doc_pk'
    edit_admin_only = True

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['client_id'] = self._kwargs['pk']
        return kwargs

    def delete(self, request, *args, **kwargs):
        if not request.user.is_admin:
            raise PermissionDenied("The user does not have permissions to do this")
        self.object.delete()
        return HttpResponse("refresh")

    def get_success_url(self):
        return reverse(self.success_url_name, kwargs={'pk': self._kwargs['pk']})


def return_file(request, pk, uuid):
    try:
        doc = get_object_or_404(ClientDocument, client_id=pk, uuid=uuid)
        response = HttpResponse(doc.document, content_type=doc.mime_type())
        response['Content-Disposition'] = 'attachment; filename="%s"' % doc.file_name
        return response
    except FileNotFoundError:
        raise Http404("File not found")
