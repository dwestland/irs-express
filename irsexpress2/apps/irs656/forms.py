# -*- coding: utf-8 -*-

from django import forms

from utils.forms import ImprovedForm
from utils.widgets import PlainTextField
from utils.templatetags.misc_helpers import intcomma_force
from clients.models import Client
from irs_common.forms import ClientFormMixin
from irs_common.datasync import DataSync
from .models import (F656Page1, ClientSpouse, MailingAddress, BusinessInformation,
                     F656Page2, BusinessTaxDebt,
                     F656Page3,
                     F656Page4,
                     F656Page5,
                     F656Page6,
                     F656Page7,
                     )
from .utils import get_low_income_suggestion


class Page1Form(ClientFormMixin, ImprovedForm, forms.ModelForm):
    title = "Section 1: Taxpayer Information / Business Information"
    jointoffer_b = forms.BooleanField(label='Is this a joint offer with your Spouse?',
                                      help_text='This applies only if you have a marriage '
                                      'recognized by the state in which you were married.'
                                      'Common law marriages are not applicable.', required=False)
    has_mailaddr = forms.BooleanField(label='Does your mailing address differ from above address?',
                                      help_text='', required=False)
    has_business = forms.BooleanField(label='Is your business a Corporation, Partnership, LLC, or LLP?',
                                      help_text='Use if you want to compromise those tax debts. You must also '
                                      'include all required documentation including the Form 433-B (OIC), '
                                      '$186 application fee, and initial payment', required=False)

    class Meta:
        model = F656Page1
        exclude = ('form', 'jointoffer', 'mailingaddr', 'businessinfo', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.form = self.client.get_form_656()
        dsync = DataSync(self.client, ignore='form656')
        for f in self.fields:
            self.fields[f].initial = dsync.get(f)
        self.set_widget_class('ssn', 'ssn-field')
        self.set_widget_class('zipcode', 'zip-field')
        if self.instance.pk:
            self.fields['jointoffer_b'].initial = self.instance.jointoffer is not None
            self.fields['has_business'].initial = self.instance.businessinfo is not None
        else:
            self.fields['jointoffer_b'].initial = dsync.get('jointoffer')
        self.add_subform_checkbox('jointoffer_b', ClientSpouseForm.prefix)
        self.add_subform_checkbox('has_mailaddr', MailingAddressForm.prefix)
        self.add_subform_checkbox('has_business', BusinessInformationForm.prefix)
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
        dsync = DataSync(self.client, ignore='form656')
        for f in self.fields:
            self.fields[f].initial = dsync.get('spouse_%s' % f)
        # self.reinit_widgets()


class MailingAddressForm(ClientFormMixin, ImprovedForm, forms.ModelForm):
    prefix = 'mailingaddr'
    subform_classname = "mailingaddr_details"
    subform_title = "Address Details"

    class Meta:
        model = MailingAddress
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_widget_class('zipcode', 'zip-field')


class BusinessInformationForm(ClientFormMixin, ImprovedForm, forms.ModelForm):
    prefix = 'businessinfo'
    subform_classname = "businessinfo_details"
    subform_title = "Business Information"

    class Meta:
        model = BusinessInformation
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        dsync = DataSync(self.client, ignore='form656')
        for f in self.fields:
            self.fields[f].initial = dsync.get('business_%s' % f)
        self.fields['ein'].initial = dsync.get('ein')
        self.fields['phone'].initial = dsync.get('phone_work')
        self.set_widget_class('zipcode', 'zip-field')


class Page2Form(ClientFormMixin, ImprovedForm, forms.ModelForm):
    title = "Section 2: Tax Periods"

    businesstaxdebt_b = forms.BooleanField(label="Is Your Offer is for Business Tax Debt?", required=False,
                                           help_text='This section is shown only if you have filled '
                                           '"Business Information" section in Section 1')

    class Meta:
        model = F656Page2
        exclude = ('form', 'businesstaxdebt')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.form = self.client.get_form_656()
        chk_fields = [('is_1040_incometax', 'years_1040'),
                      ('is_trustfund_recovery_penalty', 'trustfund_person', 'trustfund_periods'),
                      ('is_941_qtaxreturn', 'qtaxreturn_941_periods'),
                      ('is_940_afuta', 'years_940'),
                      ('is_other_taxes', 'othertaxes_types_periods'),
                      ]
        for cf_elems in chk_fields:
            cf, *deps = cf_elems
            self.set_widget_class(cf, 'chk-radiogroup radiogroup-p2')
            self.fields[cf].widget.attrs.update({'data-radiogroup': 'radiogroup-p2'})
            self.fields[cf].widget.attrs.update({'data-dep_rows': ' '.join(deps)})
            if not getattr(self.instance, cf):
                for d in deps:
                    self.set_widget_class(d, 'hidden')
        # business tax section (2B) initialization
        self.fields['businesstaxdebt_b'].initial = False
        page1 = getattr(self.instance.form, 'page1', None)
        if page1 and page1.businessinfo is not None:
            self.fields['businesstaxdebt_b'].initial = True
        self.set_widget_class('businesstaxdebt_b', 'disabled readonly')
        self.add_subform_checkbox('businesstaxdebt_b', BusinessTaxDebtForm.prefix)
        self.reinit_widgets()


class BusinessTaxDebtForm(ClientFormMixin, ImprovedForm, forms.ModelForm):
    prefix = 'businesstaxdebt'
    subform_classname = "businesstaxdebt_details"
    subform_title = "Business Tax Debt"

    class Meta:
        model = BusinessTaxDebt
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        chk_fields = [('is_1120_incometax', 'years_1120'),
                      ('is_941_qtaxreturn_bus', 'qtaxreturn_941_periods_bus'),
                      ('is_940_afuta_bus', 'years_940_bus'),
                      ('is_other_taxes_bus', 'othertaxes_types_periods_bus'),
                      ]
        for cf_elems in chk_fields:
            cf, *deps = cf_elems
            self.set_widget_class(cf, 'chk-radiogroup radiogroup-p2-btd')
            self.fields[cf].widget.attrs.update({'data-radiogroup': 'radiogroup-p2-btd'})
            self.fields[cf].widget.attrs.update({'data-dep_rows': ' '.join(("%s-%s" % (self.prefix, d) for d in deps))})
            if not getattr(self.instance, cf):
                for d in deps:
                    self.set_widget_class(d, 'hidden')
        self.reinit_widgets()


class Page3Form(ClientFormMixin, ImprovedForm, forms.ModelForm):
    title = "Section 3: Reason for Offer"

    class Meta:
        model = F656Page3
        exclude = ('form', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.form = self.client.get_form_656()
        #
        self.reinit_widgets()


class Page4Form(ClientFormMixin, ImprovedForm, forms.ModelForm):
    title = "Section 4: Low-Income Certification"
    suggestion = PlainTextField(label='IRS Express Recommends')

    class Meta:
        model = F656Page4
        fields = ('suggestion', 'low_income_qualify')
        exclude = ('form', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.form = self.client.get_form_656()
        decision, suggestion_data = get_low_income_suggestion(self.client)
        self.fields['suggestion'].widget.html_text = suggestion_data
        if decision == 'DO':
            self.fields['low_income_qualify'].initial = True
        self.reinit_widgets()


class Page5Form(ClientFormMixin, ImprovedForm, forms.ModelForm):
    title = "Section 5: Payment Terms"
    income_info = PlainTextField(label='', )
    suggestion_lumpsum = PlainTextField(label='IRS Express Recommends')
    statute_exp_date = PlainTextField(label="The Taxpayer's statute of limitation expires")
    statute_months_avail = PlainTextField(label="Months remaining until the end of the statue")
    can_pay = PlainTextField(label="The Taxpayer can pay", html_text='$ <span class="number-field">0</span>')
    suggested_amount = PlainTextField(label="Suggested offer amount",
                                      html_text='$ <span class="number-field">0</span>')
    remaining_balance = PlainTextField(label="Remaining Balance", html_text='$ <span class="number-field">0</span>')

    class Meta:
        model = F656Page5
        fields = ('income_info',
                  'lump_sum_cash', 'debt_total', 'assessed_date', 'monthly_income',
                  'statute_exp_date', 'statute_months_avail', 'can_pay', 'suggestion_lumpsum',
                  'suggested_amount', 'offer_amount_lumpsum', 'initial_payment', 'remaining_balance',
                  'payment_1', 'payment_2', 'payment_3', 'payment_4', 'payment_5',
                  'periodic_payment', 'offer_amount_period', 'offer_included', 'monthly_payment',
                  'payment_day', 'pay_months', 'final_payment', 'final_payment_day', 'final_pay_month',
                  )
        exclude = ('form', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.form = self.client.get_form_656()
        dsync = DataSync(self.client, ignore='form656')
        income = dsync.get('net_difference', lambda: 0)()
        self.fields['income_info'].widget.html_text = '<span class="irsexpress_info">The Tax Payer’s available ' + \
            'monthly income is <span class="data">$%s</span></span>' % intcomma_force(income)
        self.fields['monthly_income'].initial = income
        self.fields['suggestion_lumpsum'].widget.html_text = \
            'The Taxpayer is <span class="decision"><span id="lumpsum_decision">NOT</span> eligible</span> ' + \
            'for an Offer in Compromise'
        chk_fields = [('lump_sum_cash', 'debt_total', 'assessed_date', 'monthly_income',
                       'statute_exp_date', 'statute_months_avail', 'can_pay', 'suggestion_lumpsum', 'suggested_amount',
                       'offer_amount_lumpsum', 'initial_payment', 'remaining_balance',
                       'payment_1', 'payment_2', 'payment_3', 'payment_4', 'payment_5', ),
                      ('periodic_payment', 'offer_amount_period', 'offer_included', 'monthly_payment', 'payment_day',
                       'pay_months', 'final_payment', 'final_payment_day', 'final_pay_month',),
                      ]
        for cf_elems in chk_fields:
            cf, *deps = cf_elems
            self.set_widget_class(cf, 'chk-radiogroup radiogroup-p5')
            self.fields[cf].widget.attrs.update({'data-radiogroup': 'radiogroup-p5'})
            self.fields[cf].widget.attrs.update({'data-dep_rows': ' '.join(("%s" % (d) for d in deps))})
            if not getattr(self.instance, cf):
                for d in deps:
                    self.set_widget_class(d, 'hidden')
        self.reinit_widgets()


class Page6Form(ClientFormMixin, ImprovedForm, forms.ModelForm):
    title = "Sections 6 / 7: Designation of Down Payment and Deposit / " + \
        "Source of Funds, Making Your Payment, and Filing Requirements"

    class Meta:
        model = F656Page6
        exclude = ('form', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.form = self.client.get_form_656()
        self.set_widget_class('all_taxreturns_filed', 'disabled readonly')
        self.set_widget_class('noreturn_for', 'disabled readonly')
        self.set_widget_class('has_deposit', 'chk-radiogroup radiogroup-p61')
        self.fields['has_deposit'].widget.attrs.update({'data-radiogroup': 'radiogroup-p61'})
        self.fields['has_deposit'].widget.attrs.update({'data-dep_rows':
                                                        'total_payment initial_payment deposit_payment'})
        if not self.instance.has_deposit:
            for cf in ['total_payment', 'initial_payment', 'deposit_payment']:
                self.set_widget_class(cf, 'hidden')
        self.reinit_widgets()


class Page7Form(ClientFormMixin, ImprovedForm, forms.ModelForm):
    title = "Authorized Persons"

    class Meta:
        model = F656Page7
        exclude = ('form', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.form = self.client.get_form_656()
        self.set_widget_class('allow_designee', 'chk-radiogroup radiogroup-p71')
        self.fields['allow_designee'].widget.attrs.update({'data-radiogroup': 'radiogroup-p71'})
        self.fields['allow_designee'].widget.attrs.update({'data-dep_rows':
                                                           'designee_name designee_phone'})
        if not self.instance.allow_designee:
            for cf in ['designee_name', 'designee_phone']:
                self.set_widget_class(cf, 'hidden')
        self.reinit_widgets()
