# -*- coding: utf-8 -*-

from django import forms
from django.utils import timezone

from irs_common.datasync import DataSync
from utils.forms import ImprovedForm
from clients.models import Client
# from .models import


class ClientFormMixin(object):
    prefix = ''
    subform_classname = ''
    mandatory_client = True

    def __init__(self, *args, **kwargs):
        client_id = kwargs.pop('client_id')
        self.client = None
        if self.mandatory_client or client_id:
            self.client = Client.objects.get(pk=client_id)
        self._object = kwargs.pop('object', None)
        super().__init__(*args, **kwargs)
        self.reinit_widgets()

    def add_subform_checkbox(self, fieldname, subform_name, reltype='1x1', count=0, max_count=0):
        if reltype == '1x1':
            self.set_widget_class(fieldname, "form1x1switcher switcher-%s" % subform_name)
        else:
            self.set_widget_class(fieldname, "form1xnswitcher switcher-%s" % subform_name)
            self.fields[fieldname].widget.attrs['data-subform-count'] = str(count)
            self.fields[fieldname].widget.attrs['data-subform-maxcount'] = str(max_count)
        self.fields[fieldname].widget.attrs['data-subform-name'] = subform_name


class OICCalculatorForm(ClientFormMixin, ImprovedForm, forms.ModelForm):
    pp_debt_total = forms.IntegerField(initial=15000)
    pp_monthly_income = forms.IntegerField(initial=200)
    pp_assessed_date = forms.DateField(initial=timezone.datetime(2009, 2, 5))
    pp_offer_amount = forms.IntegerField(initial=0)

    mandatory_client = False

    class Meta:
        model = Client  # actually not needed, but it would be useful for mixins
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.client:
            dsync = DataSync(self.client)
            self.fields['pp_debt_total'].initial = dsync.get('debt_total', 0) or 15000
            income = dsync.get('net_difference', lambda: 0)()
            if income == 0:
                income = dsync.get('monthly_income', 0)
            self.fields['pp_monthly_income'].initial = income or 200
            self.fields['pp_assessed_date'].initial = dsync.get('assessed_date') or timezone.datetime(2009, 2, 5)
            self.fields['pp_offer_amount'].initial = dsync.get('offer_amount', 0)
