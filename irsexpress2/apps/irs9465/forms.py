# -*- coding: utf-8 -*-

from django import forms

from utils.forms import ImprovedForm
from clients.models import Client
from irs_common.forms import ClientFormMixin
from irs_common.datasync import DataSync
from .models import (F9465Page1, ClientSpouse,
                     F9465Page2,
                     F9465Page3,
                     F9465Page4,
                     )


class Page1Form(ClientFormMixin, ImprovedForm, forms.ModelForm):
    title = "Part 1: Personal Information"
    jointoffer_b = forms.BooleanField(label='Is this a joint offer with your Spouse?',
                                      help_text='This applies only if you have a marriage '
                                      'recognized by the state in which you were married.'
                                      'Common law marriages are not applicable.', required=False)

    class Meta:
        model = F9465Page1
        exclude = ('form', 'jointoffer', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.form = self.client.get_form_9465()
        dsync = DataSync(self.client, ignore='form9465')
        for f in self.fields:
            self.fields[f].initial = dsync.get(f)
        if self.instance.pk:
            self.fields['jointoffer_b'].initial = self.instance.jointoffer is not None
        else:
            self.fields['jointoffer_b'].initial = dsync.get('jointoffer')
        self.set_widget_class('ssn', 'ssn-field')
        self.set_widget_class('zipcode', 'zip-field')
        self.add_subform_checkbox('jointoffer_b', ClientSpouseForm.prefix)
        self.reinit_widgets()


class ClientSpouseForm(ClientFormMixin, ImprovedForm, forms.ModelForm):
    prefix = 'jointoffer'
    subform_classname = "jointoffer_details"
    subform_title = "Spouse Details"

    class Meta:
        model = ClientSpouse
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_widget_class('ssn', 'ssn-field')
        dsync = DataSync(self.client, ignore='form9465')
        for f in self.fields:
            self.fields[f].initial = dsync.get('spouse_%s' % f)
        # self.reinit_widgets()


class Page2Form(ClientFormMixin, ImprovedForm, forms.ModelForm):
    title = "Part 1: Business and Employment Information"

    class Meta:
        model = F9465Page2
        exclude = ('form', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.form = self.client.get_form_9465()
        dsync = DataSync(self.client, ignore='form9465')
        for f in self.fields:
            self.fields[f].initial = dsync.get(f)
        self.set_widget_class('employer_zipcode', 'zip-field')
        self.set_widget_class('bank_zipcode', 'zip-field')
        self.reinit_widgets()


class Page3Form(ClientFormMixin, ImprovedForm, forms.ModelForm):
    title = "Part 1: Payment Information"

    class Meta:
        model = F9465Page3
        exclude = ('form', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.form = self.client.get_form_9465()
        # dsync = DataSync(self.client, ignore='form9465')
        # for f in self.fields:
        #     self.fields[f].initial = dsync.get(f)
        self.reinit_widgets()


class Page4Form(ClientFormMixin, ImprovedForm, forms.ModelForm):
    title = "Part 2: Additional Information"

    class Meta:
        model = F9465Page4
        exclude = ('form', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.form = self.client.get_form_9465()
        self.fields['married'].widget.attrs.update({
            'data-on-text': 'Married', 'data-off-text': 'Unmarried',
            'data-on-color': 'success', 'data-off-color': 'primary',
        })
        dsync = DataSync(self.client, ignore='form9465')
        self.fields['county'].initial = dsync.get('county')
        self.fields['married'].initial = dsync.get('married')
        self.fields['expenses_shared'].initial = dsync.get('jointoffer')
        self.fields['pay_period'].initial = dsync.get('pay_period')
        self.fields['spouse_pay_period'].initial = dsync.get('spouse_pay_period')
        self.fields['vehicles'].initial = dsync.get('vehicles_count')
        hh = dsync.get('health_insurance')
        if hh:
            self.fields['has_health_insurance'].initial = hh > 0
        # for f in self.fields:
        #     self.fields[f].initial = dsync.get(f)
        self.reinit_widgets()
