# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404

from utils.views import BaseCreateUpdateView, MultiFormViewMixin
from irs_common.views import BaseFView, IRSBasePageEditView
from clients.models import Client
from .tasks import fill_form_656
from .forms import (Page1Form, ClientSpouseForm, MailingAddressForm, BusinessInformationForm,
                    Page2Form, BusinessTaxDebtForm,
                    Page3Form,
                    Page4Form,
                    Page5Form,
                    Page6Form,
                    Page7Form,
                    )


class BasePageEditView(IRSBasePageEditView):
    template_name = 'irs656/form_base.html'
    formnameid = '656'


class Page1EditView(BasePageEditView):
    success_url_name = '656-page-2'
    back_url_name = ''
    form_class = Page1Form
    template_name = 'irs656/page1edit.html'
    active_page = 'is_page1_active'
    subforms = {
        'jointoffer': {'form_class': ClientSpouseForm, 'instattr': 'jointoffer'},
        'mailingaddr': {'form_class': MailingAddressForm, 'instattr': 'mailingaddr'},
        'businessinfo': {'form_class': BusinessInformationForm, 'instattr': 'businessinfo'},
    }
    prev_btn_title = ""


class Page2EditView(BasePageEditView):
    success_url_name = '656-page-3'
    back_url_name = '656-page-1'
    form_class = Page2Form
    template_name = 'irs656/page2edit.html'
    active_page = 'is_page2_active'
    subforms = {
        'businesstaxdebt': {'form_class': BusinessTaxDebtForm, 'instattr': 'businesstaxdebt'},
    }


class Page3EditView(BasePageEditView):
    success_url_name = '656-page-4'
    back_url_name = '656-page-2'
    form_class = Page3Form
    template_name = 'irs656/page3edit.html'
    active_page = 'is_page3_active'
    subforms = {
    }


class Page4EditView(BasePageEditView):
    success_url_name = '656-page-5'
    back_url_name = '656-page-3'
    form_class = Page4Form
    template_name = 'irs656/page4edit.html'
    active_page = 'is_page4_active'
    subforms = {
    }


class Page5EditView(BasePageEditView):
    success_url_name = '656-page-6'
    back_url_name = '656-page-4'
    form_class = Page5Form
    template_name = 'irs656/page5edit.html'
    active_page = 'is_page5_active'
    subforms = {
    }


class Page6EditView(BasePageEditView):
    success_url_name = '656-page-7'
    back_url_name = '656-page-5'
    form_class = Page6Form
    template_name = 'irs656/page6edit.html'
    active_page = 'is_page6_active'
    subforms = {
    }


class Page7EditView(BasePageEditView):
    success_url_name = 'client_cp'
    back_url_name = '656-page-6'
    form_class = Page7Form
    template_name = 'irs656/page7edit.html'
    active_page = 'is_page7_active'
    subforms = {
    }


# ------------------------------------------------------------------------------

def get_pdf(request, client_id):
    try:
        pdf_data = fill_form_656(client_id=client_id, return_value=True)
        response = HttpResponse(pdf_data, content_type='application/pdf')
        filename = "Form656.pdf"
        response['Content-Disposition'] = 'attachment; filename="%s"' % filename
        return response
    except FileNotFoundError:
        raise Http404("File not found")
