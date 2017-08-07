# -*- coding: utf-8 -*-

import re

from django.http import HttpResponse, Http404

from utils.views import BaseCreateUpdateView, MultiFormViewMixin
from irs_common.views import BaseFView, IRSBasePageEditView
from clients.models import Client
from .tasks import fill_form_8821, fill_form_8821spouse
from .forms import (Page1Form, Page1SpouseForm,
                    Page2Form, SpecificUseForm, TaxInformationForm,
                    Page2SpouseForm, SpecificUseSpouseForm, TaxInformationSpouseForm,
                    )


class BasePageEditView(IRSBasePageEditView):
    template_name = 'irs8821/form_base.html'
    formnameid = '8821'


class BasePageSpouseEditView(IRSBasePageEditView):
    template_name = 'irs8821/form_base.html'
    formnameid = 'spouse-8821'


class Page1EditView(BasePageEditView):
    success_url_name = '8821-page-2'
    back_url_name = ''
    form_class = Page1Form
    template_name = 'irs8821/page1edit.html'
    active_page = 'is_page1_active'
    subforms = {
        'specific_use': {'form_class': SpecificUseForm, 'instattr': 'specific_use_details'}
    }
    prev_btn_title = ""


class Page1SpouseEditView(BasePageSpouseEditView):
    success_url_name = 'spouse-8821-page-2'
    back_url_name = ''
    form_class = Page1SpouseForm
    template_name = 'irs8821/page1edit.html'
    active_page = 'is_page1_active'
    subforms = {
        'specific_use': {'form_class': SpecificUseSpouseForm, 'instattr': 'specific_use_details'}
    }
    prev_btn_title = ""


class Page2EditView(BasePageEditView):
    success_url_name = 'client_cp'
    back_url_name = '8821-page-1'
    form_class = Page2Form
    template_name = 'irs8821/page2edit.html'
    active_page = 'is_page2_active'
    subforms = {
        'tax_info': {'form_class': TaxInformationForm, 'instattr': None,
                     'prefix-rex': re.compile(r'^tax_info_(\d+)\-', re.I)},
    }
    next_btn_title = 'Done'


class Page2SpouseEditView(BasePageSpouseEditView):
    success_url_name = 'client_cp'
    back_url_name = 'spouse-8821-page-1'
    form_class = Page2SpouseForm
    template_name = 'irs8821/page2edit.html'
    active_page = 'is_page2_active'
    subforms = {
        'tax_info': {'form_class': TaxInformationSpouseForm, 'instattr': None,
                     'prefix-rex': re.compile(r'^tax_info_(\d+)\-', re.I)},
    }
    next_btn_title = 'Done'


# ------------------------------------------------------------------------------

def get_pdf(request, client_id):
    try:
        pdf_data = fill_form_8821(client_id=client_id, return_value=True)
        response = HttpResponse(pdf_data, content_type='application/pdf')
        filename = "Form8821.pdf"
        response['Content-Disposition'] = 'attachment; filename="%s"' % filename
        return response
    except FileNotFoundError:
        raise Http404("File not found")


def get_spouse_pdf(request, client_id):
    try:
        pdf_data = fill_form_8821spouse(client_id=client_id, return_value=True)
        response = HttpResponse(pdf_data, content_type='application/pdf')
        filename = "Form8821Spouse.pdf"
        response['Content-Disposition'] = 'attachment; filename="%s"' % filename
        return response
    except FileNotFoundError:
        raise Http404("File not found")
