
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import F, Value as V, Q
from django.views.generic.detail import SingleObjectTemplateResponseMixin, DetailView
from django.views.generic.edit import FormView, UpdateView, CreateView, ModelFormMixin, ProcessFormView, DeleteView
from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse
from django.conf import settings

from .models import Appointee
# from .forms import AppointeeEditform
from utils.views import BaseCreateUpdateView, ObjectBaseMixin


class AgentListView(ObjectBaseMixin, ListView):
    template_name = 'agents/agents_home.html'

    def get_pagination_page(self, page=1, maxitems=settings.CLIENTS_PAGINATE_BY, filters=None,
                            sortfield=None, sortasc='1'):
        items = self.get_queryset()
        if filters:
            ifilter = Q()
            istatusfilter = Q()  # means 'nothing'
            filter_enabled = True
            for ff in filters:
                ffs = ff.split('*', 1)
                if len(ffs) > 1:
                    fname, fvalue = ffs
                    if fvalue and fname == 'clientfilter':
                        ifilter |= Q(name__icontains=fvalue)
                        # ifilter |= Q(email__icontains=fvalue)
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

    def get_context_data(self, *args, page=1, maxitems=settings.CLIENTS_PAGINATE_BY, is_ajax=False, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['items'] = self.get_pagination_page(page, maxitems)
        context['prelast'] = context['items'].paginator.num_pages - 1
        return context

    def get_queryset(self):
        return self.model.objects.all()

    def get(self, request):
        self.object_list = self.get_queryset()
        if not request.is_ajax():
            return super().get(request)
        page = request.GET.get('page', 1)
        filters = request.GET.getlist('filters[]', [])
        maxitems = request.GET.get('maxitems', settings.CLIENTS_PAGINATE_BY)
        sortfield = request.GET.get('sort', 'id')
        sortasc = str(request.GET.get('asc', '1'))
        context = self.get_context_data()
        context['items'] = self.get_pagination_page(page, maxitems, filters, sortfield, sortasc)
        context['prelast'] = context['items'].paginator.num_pages - 1
        return render_to_response('agents/agent_list.html', context)


class AgentCreateUpdateView(BaseCreateUpdateView):
    template_name = 'agents/agent_edit_form.html'
    form_class = None

    def get_success_url(self):
        object_name = self.get_context_object_name(None)
        return reverse('%s_list' % object_name)


class AgentDeleteView(ObjectBaseMixin, DeleteView):
    success_url = '/'
