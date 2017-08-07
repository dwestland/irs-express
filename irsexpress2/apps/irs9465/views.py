# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404

from utils.views import BaseCreateUpdateView, MultiFormViewMixin
from irs_common.views import BaseFView, IRSBasePageEditView
from clients.models import Client
from .tasks import fill_form_9465
from .forms import (Page1Form, ClientSpouseForm,
                    Page2Form,
                    Page3Form,
                    Page4Form,
                    )


class BasePageEditView(IRSBasePageEditView):
    template_name = 'irs9465/form_base.html'
    formnameid = '9465'


class Page1EditView(BasePageEditView):
    success_url_name = '9465-page-2'
    back_url_name = ''
    form_class = Page1Form
    template_name = 'irs9465/page1edit.html'
    active_page = 'is_page1_active'
    subforms = {
        'jointoffer': {'form_class': ClientSpouseForm, 'instattr': 'jointoffer'},
    }
    prev_btn_title = ""


class Page2EditView(BasePageEditView):
    success_url_name = '9465-page-3'
    back_url_name = '9465-page-1'
    form_class = Page2Form
    template_name = 'irs9465/page2edit.html'
    active_page = 'is_page2_active'
    subforms = {
        # 'spouse': {'form_class': ClientSpouseForm, 'instattr': 'jointoffer'},
    }


class Page3EditView(BasePageEditView):
    success_url_name = '9465-page-4'
    back_url_name = '9465-page-2'
    form_class = Page3Form
    template_name = 'irs9465/page3edit.html'
    active_page = 'is_page3_active'
    subforms = {
        # 'spouse': {'form_class': ClientSpouseForm, 'instattr': 'jointoffer'},
    }


class Page4EditView(BasePageEditView):
    success_url_name = 'client_cp'
    back_url_name = '9465-page-3'
    next_btn_title = 'Done'
    form_class = Page4Form
    template_name = 'irs9465/page4edit.html'
    active_page = 'is_page4_active'
    subforms = {
        # 'spouse': {'form_class': ClientSpouseForm, 'instattr': 'jointoffer'},
    }


# ------------------------------------------------------------------------------

def get_pdf(request, client_id):
    try:
        pdf_data = fill_form_9465(client_id=client_id, return_value=True)
        response = HttpResponse(pdf_data, content_type='application/pdf')
        filename = "Form9465.pdf"
        response['Content-Disposition'] = 'attachment; filename="%s"' % filename
        return response
    except FileNotFoundError:
        raise Http404("File not found")
