# -*- coding: utf-8 -*-

from django import forms

from utils.forms import ImprovedForm
from clients.models import Client
from irs_common.forms import ClientFormMixin
from irs_common.datasync import DataSync
from .models import (F8821Page1, F8821SpousePage1,
                     F8821Page2, TaxInformation, SpecificUse,
                     F8821SpousePage2, TaxInformationSpouse, SpecificUseSpouse,
                     )


class Page1Form(ClientFormMixin, ImprovedForm, forms.ModelForm):
    title = "Part 1. Taxpayer and Appointee information"

    class Meta:
        model = F8821Page1
        exclude = ('form', 'specific_use_details')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.form = self.client.get_form_8821()
        dsync = DataSync(self.client, ignore='form8821')
        for f in self.fields:
            self.fields[f].initial = dsync.get(f)
        self.set_widget_class('zipcode', 'zip-field')
        self.set_widget_class('ssn', 'ssn-field')
        # self.set_widget_class('app_zipcode', 'zip-field')
        # self.set_widget_class('app_caf', 'caf-field')
        # self.set_widget_class('app_ptin', 'ptin-field')
        self.add_subform_checkbox('specific_use_caf_recorded', SpecificUseForm.prefix)
        self.reinit_widgets()


class Page1SpouseForm(ClientFormMixin, ImprovedForm, forms.ModelForm):
    title = "Part 1. Spouse and Appointee information"

    class Meta:
        model = F8821SpousePage1
        exclude = ('form', 'specific_use_details')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.form = self.client.get_form_8821spouse()
        dsync = DataSync(self.client, ignore='form8821')
        for f in self.fields:
            self.fields[f].initial = dsync.get('spouse_' + f)
        # spouse's address might be the same as for taxpayer
        for f in ['apt', 'street', 'city', 'state_name', 'zipcode', 'county']:
            self.fields[f].initial = dsync.get(f)
        self.set_widget_class('zipcode', 'zip-field')
        self.set_widget_class('ssn', 'ssn-field')
        # self.set_widget_class('app_zipcode', 'zip-field')
        # self.set_widget_class('app_caf', 'caf-field')
        # self.set_widget_class('app_ptin', 'ptin-field')
        self.add_subform_checkbox('specific_use_caf_recorded', SpecificUseSpouseForm.prefix)
        self.reinit_widgets()


class SpecificUseForm(ClientFormMixin, ImprovedForm, forms.ModelForm):
    prefix = 'specific_use'
    subform_classname = "specific_use_details"
    subform_title = "Specific Use Details"

    class Meta:
        model = SpecificUse
        exclude = ()


class SpecificUseSpouseForm(ClientFormMixin, ImprovedForm, forms.ModelForm):
    prefix = 'specific_use'
    subform_classname = "specific_use_details"
    subform_title = "Specific Use Details"

    class Meta:
        model = SpecificUseSpouse
        exclude = ()


class Page2Form(ClientFormMixin, ImprovedForm, forms.ModelForm):
    title = "Part 2. Tax information"
    has_tax_info = forms.BooleanField(label='Would you like to specify tax information?', initial=False,
                                      help_text='Appointee is authorized to inspect and/or receive confidential tax '
                                      'information for the type of tax, forms, periods, and specific matters you '
                                      'list below. See the line 3 instructions.')

    class Meta:
        model = F8821Page2
        exclude = ('form', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.form = self.client.get_form_8821()
        tax_count = 0
        if self.instance.pk:
            tax_count = self.instance.tax_infos.count()
        self.add_subform_checkbox('has_tax_info', TaxInformationForm.prefix,
                                  reltype='1xn', count=tax_count, max_count=3)
        self.reinit_widgets()


class Page2SpouseForm(ClientFormMixin, ImprovedForm, forms.ModelForm):
    title = "Part 2. Spouse Tax information"
    has_tax_info = forms.BooleanField(label='Would you like to specify tax information?', initial=False,
                                      help_text='Appointee is authorized to inspect and/or receive confidential tax '
                                      'information for the type of tax, forms, periods, and specific matters you '
                                      'list below. See the line 3 instructions.')

    class Meta:
        model = F8821SpousePage2
        exclude = ('form', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.form = self.client.get_form_8821spouse()
        tax_count = 0
        if self.instance.pk:
            tax_count = self.instance.tax_infos.count()
        self.add_subform_checkbox('has_tax_info', TaxInformationSpouseForm.prefix,
                                  reltype='1xn', count=tax_count, max_count=3)
        self.reinit_widgets()


class TaxInformationForm(ClientFormMixin, ImprovedForm, forms.ModelForm):
    prefix = 'tax_info'
    subform_classname = "tax_info_details"
    subform_title = "Tax Details"
    object_name = 'Tax Details'

    class Meta:
        exclude = ('formpage', )
        model = TaxInformation

    def __init__(self, *args, **kwargs):
        formpage = kwargs.get('formpage', None)
        super().__init__(*args, **kwargs)
        if not formpage:
            mainform = self.client.get_form_8821()
            if mainform and hasattr(mainform, 'page2'):
                formpage = mainform.page2
        if not self.instance.formpage:
            self.instance.formpage = formpage


class TaxInformationSpouseForm(ClientFormMixin, ImprovedForm, forms.ModelForm):
    prefix = 'tax_info'
    subform_classname = "tax_info_details"
    subform_title = "Tax Details"
    object_name = 'Tax Details'

    class Meta:
        exclude = ('formpage', )
        model = TaxInformationSpouse

    def __init__(self, *args, **kwargs):
        formpage = kwargs.get('formpage', None)
        super().__init__(*args, **kwargs)
        if not formpage:
            mainform = self.client.get_form_8821spouse()
            if mainform and hasattr(mainform, 'page2'):
                formpage = mainform.page2
        if not self.instance.formpage:
            self.instance.formpage = formpage
