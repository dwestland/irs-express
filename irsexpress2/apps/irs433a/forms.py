# -*- coding: utf-8 -*-

import json
from collections import OrderedDict

from django import forms

from utils.forms import ImprovedForm
from utils.widgets import PlainTextField, PlainTextWidget
from clients.models import Client
from irs_common.forms import ClientFormMixin
from irs_common.datasync import DataSync
from .models import (F433aPage1, ClientDependent, ClientSpouse,
                     F433aPage2, EmploymentInfo,
                     F433aPage3, LawsuitPartyInfo, BankruptcyInfo, BeneficiaryInfo,
                     LiveAbroadDetails, TrusteeDetails, SafeDetails, AssetTransferDetails,
                     F433aPage4, BankAccountInfo, InvestmentInfo, CreditInfo, InsuranceInfo,
                     F433aPage5, RealPropertyInfo, VehicleInfo, PersonalAssetInfo,
                     F433aPage6,
                     F433aPage7, PaymentProcessorInfo, BusinessCreditCardInfo, BusinessBankAccountInfo,
                     AccountsReceivableInfo, BusinessAssetInfo,
                     F433aPage8,
                     )


class Page1Form(ClientFormMixin, ImprovedForm, forms.ModelForm):
    title = "Section 1: Personal Information"
    married = forms.BooleanField(label='Marital Status', help_text='This applies only if you have a marriage '
                                 'recognized by the state in which you were married.'
                                 'Common law marriages are not applicable.', required=False)
    has_deps = forms.BooleanField(label='Do you have any dependents?', initial=False, required=False)

    class Meta:
        model = F433aPage1
        exclude = ('form', 'spouse', 'additional_notes', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.form = self.client.get_form_433a()
        dsync = DataSync(self.client, ignore='form433a')
        for f in self.fields:
            v = dsync.get(f)
            if v:
                self.fields[f].initial = v
        self.fields['married'].widget.attrs.update({
            'data-on-text': 'Married', 'data-off-text': 'Unmarried',
            'data-on-color': 'success', 'data-off-color': 'primary',
        })
        dep_count = 0
        self.set_widget_class('ssn', 'ssn-field')
        self.set_widget_class('zipcode', 'zip-field')
        if self.instance.pk:
            dep_count = len(self.instance.dependents.all())
            self.fields['married'].initial = self.instance.spouse is not None
        else:
            self.fields['married'].initial = dsync.get('married', None) is not None
        self.add_subform_checkbox('married', ClientSpouseForm.prefix)
        self.add_subform_checkbox('has_deps', ClientDependentForm.prefix,
                                  reltype='1xn', count=dep_count, max_count=30)
        self.reinit_widgets()


class ClientDependentForm(ClientFormMixin, ImprovedForm, forms.ModelForm):
    prefix = 'dependent'
    subform_classname = "dependent_details"
    subform_title = "Dependent Details"
    object_name = 'Dependent'

    class Meta:
        model = ClientDependent
        exclude = ('formpage', )

    def __init__(self, *args, **kwargs):
        formpage = kwargs.get('formpage', None)
        super().__init__(*args, **kwargs)
        if not formpage:
            mainform = self.client.get_form_433a()
            if mainform and hasattr(mainform, 'page1'):
                formpage = mainform.page1
        if not self.instance.formpage:
            self.instance.formpage = formpage


class ClientSpouseForm(ClientFormMixin, ImprovedForm, forms.ModelForm):
    prefix = 'spouse'
    subform_classname = "spouse_details"
    subform_title = "Spouse Details"

    class Meta:
        model = ClientSpouse
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        dsync = DataSync(self.client, ignore='form433a')
        for f in self.fields:
            v = dsync.get('spouse_%s' % f)
            if v:
                self.fields[f].initial = v
        self.fields['return_with'].initial = dsync.get('jointoffer')
        self.set_widget_class('ssn', 'ssn-field')
        # self.reinit_widgets()


class Page2Form(ClientFormMixin, ImprovedForm, forms.ModelForm):
    title = "Section 2: Employment Information for Wage Earners"
    employed = forms.BooleanField(label="Are you employed?", initial=False, required=False)
    spouse_employed = forms.BooleanField(label="Is your spouse employed?", initial=False, required=False)

    class Meta:
        model = F433aPage2
        fields = ('employed', 'spouse_employed', 'additional_notes')
        exclude = ('form', 'employment_info', 'spouse_employment_info', 'additional_notes', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.form = self.client.get_form_433a()
        self.fields['employed'].initial = self.instance.employment_info is not None
        self.fields['spouse_employed'].initial = self.instance.spouse_employment_info is not None
        self.add_subform_checkbox('employed', 'taxpayer_emp')
        self.add_subform_checkbox('spouse_employed', 'spouse_emp')
        self.reinit_widgets()


class EmploymentInfoForm(ClientFormMixin, ImprovedForm, forms.ModelForm):

    class Meta:
        model = EmploymentInfo
        exclude = ()

    def __init__(self, *args, **kwargs):
        formpage2 = kwargs.get('formpage', None)
        super().__init__(*args, **kwargs)
        dsync = DataSync(self.client, ignore='form433a')
        if self.prefix == 'taxpayer':
            for f in self.fields:
                v = dsync.get('employer_%s' % f)
                if v:
                    self.fields[f].initial = v
            self.fields['employer_name'].initial = dsync.get('employer_name')
            self.fields['pay_period'].initial = dsync.get('pay_period')
            self.fields['phone_work'].initial = dsync.get('phone_work')
        elif self.prefix == 'spouse':
            self.fields['pay_period'].initial = dsync.get('spouse_pay_period')
        self.set_widget_class('zipcode', 'zip-field')
        # self.reinit_widgets()


class Page3Form(ClientFormMixin, ImprovedForm, forms.ModelForm):
    title = "Section 3: Other Financial Information (Attach copies of applicable documentation)"

    lawsuited = forms.BooleanField(label="Are you a party to a lawsuit?", initial=False, required=False)
    bankrupted = forms.BooleanField(label="Have you ever filed bankruptcy?", initial=False, required=False,
                                    help_text="Even though the bankruptcy filing may have been over 10 years ago,"
                                    " this answer is 'Yes'")
    lived_abroad = forms.BooleanField(
        required=False,
        label="In the past 10 years, have you lived outside of the U.S for 6 months or longer?", initial=False,
        help_text='Some individuals move out of the country for a period of 6 months or longer for a number of '
        'reasons. If you have lived abroad for periods in excess of 6 months at a time, please indicate it here.')
    is_beneficiary = forms.BooleanField(label="Are you the beneficiary of a trust, estate, or life insurance policy?",
                                        initial=False, help_text='You may have an elderly parent that is alive and you '
                                        'expect to inherit money. Unless you have actual knowledge that you are a '
                                        'beneficiary under a trust or estate, the answer is "No"', required=False)
    is_trustee = forms.BooleanField(label="Are you a trustee, fiduciary, or contributor of a trust?", initial=False,
                                    required=False)
    has_safe = forms.BooleanField(label="Do you have a safe deposit box (business or personal)?", initial=False,
                                  required=False)
    assets_transferred = forms.BooleanField(
        label="In the past 10 years, have you transferred any assets for less than their full value?", initial=False,
        help_text='If you transferred a house for example and there was no equity at the time of the transfer, '
        'the answer is "no". The IRS is trying to determine if you have intentionally divested yourself of assets '
        'in order to qualify for an offer in compromise. If so, the IRS will try to add back the value of the '
        'divested asset back into your offer amount.', required=False)

    class Meta:
        model = F433aPage3
        fields = ('lawsuited', 'bankrupted', 'lived_abroad', 'is_beneficiary', 'is_trustee',
                  'has_safe', 'assets_transferred', 'additional_notes')
        exclude = ('form', 'lawsuit_party', 'bankruptcy', 'beneficiary', 'additional_notes')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.form = self.client.get_form_433a()
        self.fields['lawsuited'].initial = self.instance.lawsuit_party is not None
        self.fields['bankrupted'].initial = self.instance.bankruptcy is not None
        self.fields['lived_abroad'].initial = self.instance.liveabroad is not None
        self.fields['is_beneficiary'].initial = self.instance.beneficiary is not None
        self.fields['is_trustee'].initial = self.instance.trustee is not None
        self.fields['has_safe'].initial = self.instance.safe is not None
        self.fields['assets_transferred'].initial = self.instance.asset_transfer is not None
        self.add_subform_checkbox('lawsuited', LawsuitPartyInfoForm.prefix)
        self.add_subform_checkbox('bankrupted', BankruptcyInfoForm.prefix)
        self.add_subform_checkbox('lived_abroad', LiveAbroadInfoForm.prefix)
        self.add_subform_checkbox('is_beneficiary', BeneficiaryInfoForm.prefix)
        self.add_subform_checkbox('is_trustee', TrusteeInfoForm.prefix)
        self.add_subform_checkbox('has_safe', SafeInfoForm.prefix)
        self.add_subform_checkbox('assets_transferred', AssetTransferInfoForm.prefix)
        self.reinit_widgets()


class LawsuitPartyInfoForm(ClientFormMixin, ImprovedForm, forms.ModelForm):
    prefix = 'lawsuit'
    subform_classname = "lawsuit_details"
    subform_title = "Lawsuit Details"

    class Meta:
        model = LawsuitPartyInfo
        exclude = ()

    def __init__(self, *args, **kwargs):
        # formpage3 = kwargs.get('formpage', None)
        super().__init__(*args, **kwargs)
        self.fields['is_defendant'].widget.attrs.update({
            'data-on-text': 'Defendant', 'data-off-text': 'Plaintiff',
            'data-off-color': 'default', 'data-on-color': 'primary',
        })
        self.reinit_widgets()


class BankruptcyInfoForm(ClientFormMixin, ImprovedForm, forms.ModelForm):
    prefix = 'bankruptcy'
    subform_classname = "bankruptcy_details"
    subform_title = "Bankruptcy Details"

    class Meta:
        model = BankruptcyInfo
        exclude = ()


class BeneficiaryInfoForm(ClientFormMixin, ImprovedForm, forms.ModelForm):
    prefix = 'beneficiary'
    subform_classname = "beneficiary_details"
    subform_title = "Beneficiary Details"

    class Meta:
        model = BeneficiaryInfo
        exclude = ()


class LiveAbroadInfoForm(ClientFormMixin, ImprovedForm, forms.ModelForm):
    prefix = 'liveabroad'
    subform_classname = "liveabroad_details"
    subform_title = "Live Abroad Details"

    class Meta:
        model = LiveAbroadDetails
        exclude = ()


class TrusteeInfoForm(ClientFormMixin, ImprovedForm, forms.ModelForm):
    prefix = 'trustee'
    subform_classname = "trustee_details"
    subform_title = "Trust Details"

    class Meta:
        model = TrusteeDetails
        exclude = ()


class SafeInfoForm(ClientFormMixin, ImprovedForm, forms.ModelForm):
    prefix = 'safe'
    subform_classname = "safe_details"
    subform_title = "Safe Details"

    class Meta:
        model = SafeDetails
        exclude = ()


class AssetTransferInfoForm(ClientFormMixin, ImprovedForm, forms.ModelForm):
    prefix = 'trassets'
    subform_classname = "trassets_details"
    subform_title = "Asset Transfers Details"

    class Meta:
        model = AssetTransferDetails
        exclude = ()


class Page4Form(ClientFormMixin, ImprovedForm, forms.ModelForm):
    title = "Section 4: Personal Asset Information for All Individuals"

    has_bank_accounts = forms.BooleanField(
        label='Do you have a bank account?', initial=False, required=False,
        help_text='Include all checking, online and mobile (e.g., PayPal) accounts, money market accounts, '
        'savings accounts, and stored value cards (e.g., payroll cards, government benefit cards, etc.).')
    has_investments = forms.BooleanField(
        label='Do you have Investments?', initial=False, required=False,
        help_text='Include stocks, bonds, mutual funds, stock options, certificates of deposit, and retirement '
        'assets such as IRAs, Keogh, and 401(k) plans. Include all corporations, partnerships, limited liability '
        'companies or other business entities in which the individual is an officer, director, owner, member, '
        'or otherwise has a financial interest.')
    has_cc = forms.BooleanField(
        label='Available Credit', initial=False, required=False,
        help_text='List bank issued credit cards with available credit')
    has_insurance = forms.BooleanField(
        label='Do you have life insurance with a cash value?', initial=False, required=False,
        help_text='Does the individual have life insurance with a cash value '
        '(Term Life insurance does not have a cash value.)')

    class Meta:
        model = F433aPage4
        fields = ('cash_on_hand',
                  'has_bank_accounts', 'bank_balance_date', 'total_cash',
                  'has_investments', 'loan_balance_date', 'total_equity',
                  'has_cc', 'cc_amount_owed_date', 'cc_available_credit_date', 'total_credit',
                  'has_insurance', 'total_available_cash', )
        exclude = ('form', 'banking_additional_info', 'investment_additional_info', 'credit_additional_info',
                   'insurance_additional_info', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.form = self.client.get_form_433a()
        banks_count, investments_count, credits_count, insurance_count = 0, 0, 0, 0
        if self.instance.pk:
            banks_count = self.instance.bank_accounts.count()
            investments_count = self.instance.investments.count()
            credits_count = self.instance.credits.count()
            insurance_count = self.instance.insurances.count()
        self.add_subform_checkbox('has_bank_accounts', BankAccountInfoForm.prefix,
                                  reltype='1xn', count=banks_count, max_count=3)
        self.add_subform_checkbox('has_investments', InvestmentInfoForm.prefix,
                                  reltype='1xn', count=investments_count, max_count=3)
        self.add_subform_checkbox('has_cc', CreditInfoForm.prefix,
                                  reltype='1xn', count=credits_count, max_count=2)
        self.add_subform_checkbox('has_insurance', InsuranceInfoForm.prefix,
                                  reltype='1xn', count=insurance_count, max_count=3)
        # add auto-hiding behaviour
        self.set_widget_class('bank_balance_date', 'showhidewith-chk-' + BankAccountInfoForm.prefix)
        self.set_widget_class('total_cash', 'showhidewith-chk-' + BankAccountInfoForm.prefix)
        self.set_widget_class('loan_balance_date', 'showhidewith-chk-' + InvestmentInfoForm.prefix)
        self.set_widget_class('total_equity', 'showhidewith-chk-' + InvestmentInfoForm.prefix)
        self.set_widget_class('cc_amount_owed_date', 'showhidewith-chk-' + CreditInfoForm.prefix)
        self.set_widget_class('cc_available_credit_date', 'showhidewith-chk-' + CreditInfoForm.prefix)
        self.set_widget_class('total_credit', 'showhidewith-chk-' + CreditInfoForm.prefix)
        self.set_widget_class('total_available_cash', 'showhidewith-chk-' + InsuranceInfoForm.prefix)
        self.reinit_widgets()


class Page4SubForm(ClientFormMixin, ImprovedForm, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        formpage = kwargs.get('formpage', None)
        super().__init__(*args, **kwargs)
        if not formpage:
            mainform = self.client.get_form_433a()
            if mainform and hasattr(mainform, 'page4'):
                formpage = mainform.page4
        if not self.instance.formpage:
            self.instance.formpage = formpage
        self.set_widget_class('zipcode', 'zip-field')


class BankAccountInfoForm(Page4SubForm):
    prefix = 'bankaccount'
    subform_classname = "bankaccount_details"
    subform_title = "Bank Account Details"
    object_name = 'Bank Account'

    class Meta:
        exclude = ('formpage', )
        model = BankAccountInfo

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_widget_class('account_balance', 'account_balance')
        # self.fields['account_balance'].widget.set_class('account_balance')


class InvestmentInfoForm(Page4SubForm):
    prefix = 'investment'
    subform_classname = "investment_details"
    subform_title = "Investments Details"
    object_name = 'Investment'

    class Meta:
        exclude = ('formpage', )
        model = InvestmentInfo

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['loan_balance'].widget.set_class('loan_balance_curval loan_balance')
        self.fields['current_value'].widget.set_class('loan_balance_curval current_value')


class CreditInfoForm(Page4SubForm):
    prefix = 'credit'
    subform_classname = "credit_details"
    subform_title = "Credits Details"
    object_name = 'Credit'

    class Meta:
        exclude = ('formpage', )
        model = CreditInfo

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['amount_owed'].widget.set_class('amount_owed_crlimit amount_owed')
        self.fields['credit_limit'].widget.set_class('amount_owed_crlimit credit_limit')


class InsuranceInfoForm(Page4SubForm):
    prefix = 'insurance'
    subform_classname = "insurance_details"
    subform_title = "Insurances Details"
    object_name = 'Insurance'

    class Meta:
        exclude = ('formpage', )
        model = InsuranceInfo

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cash_value'].widget.set_class('cash_value_lbal cash_value')
        self.fields['loan_balance'].widget.set_class('cash_value_lbal iiloan_balance')


class Page5Form(ClientFormMixin, ImprovedForm, forms.ModelForm):
    title = "Section 4: Personal Asset Information for All Individuals"

    has_real_property = forms.BooleanField(
        label='Do you own or are purchasing any real property?', initial=False, required=False,
        help_text='Includes all real property owned or being purchased')
    has_vehicle = forms.BooleanField(
        label='Do you own a personal vehicle?', initial=False, required=False,
        help_text='Includes boats, RVs, motorcycles, all-terrain and off-road vehicles, trailers, etc.')
    has_personal_assets = forms.BooleanField(
        label='Do you have any other personal assets?', initial=False, required=False,
        help_text='Includes all furniture, personal effects, artwork, jewelry, collections (coins, guns, etc.), '
        'antiques or other assets. Include intangible assets such as licenses, domain names, patents, copyrights, '
        'mining claims, etc.')

    class Meta:
        model = F433aPage5
        fields = ('has_real_property', 'real_property_total_equity',
                  'has_vehicle', 'vehicles_total_equity',
                  'has_personal_assets', 'personal_assets_total_equity')
        exclude = ('form', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.form = self.client.get_form_433a()
        rprops, vhcls, assets = 0, 0, 0
        if self.instance.pk:
            rprops = self.instance.realproperties.count()
            vhcls = self.instance.vehicles.count()
            assets = self.instance.personalassets.count()
        self.add_subform_checkbox('has_real_property', RealPropertyInfoForm.prefix,
                                  reltype='1xn', count=rprops, max_count=2)
        self.add_subform_checkbox('has_vehicle', VehicleInfoForm.prefix,
                                  reltype='1xn', count=vhcls, max_count=2)
        self.add_subform_checkbox('has_personal_assets', PersonalAssetInfoForm.prefix,
                                  reltype='1xn', count=assets, max_count=2)
        self.set_widget_class('real_property_total_equity', 'showhidewith-chk-' + RealPropertyInfoForm.prefix)
        self.set_widget_class('vehicles_total_equity', 'showhidewith-chk-' + VehicleInfoForm.prefix)
        self.set_widget_class('personal_assets_total_equity', 'showhidewith-chk-' + PersonalAssetInfoForm.prefix)
        self.reinit_widgets()


class Page5SubForm(ClientFormMixin, ImprovedForm, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        formpage = kwargs.get('formpage', None)
        super().__init__(*args, **kwargs)
        if not formpage:
            mainform = self.client.get_form_433a()
            if mainform and hasattr(mainform, 'page5'):
                formpage = mainform.page5
        if not self.instance.formpage:
            self.instance.formpage = formpage
        self.set_widget_class('lender_zipcode', 'zip-field')


class RealPropertyInfoForm(Page5SubForm):
    prefix = 'realproperty'
    subform_classname = "realproperty_details"
    subform_title = "Real Properties Details"
    object_name = 'Real Property'

    class Meta:
        fields = (
            'description',
            'location_street', 'location_city', 'location_state_name', 'location_zipcode', 'location_county',
            'purchase_date', 'market_value', 'current_loan_balance', 'monthly_payment', 'final_payment_date',
            'lender_name', 'lender_street', 'lender_city', 'lender_state_name', 'lender_zipcode', 'lender_phone',
        )
        exclude = ('formpage', )
        model = RealPropertyInfo

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['market_value'].widget.set_class('rpfmv_clb rpmarket_value')
        self.fields['current_loan_balance'].widget.set_class('rpfmv_clb rpcurrent_loan_balance')
        self.set_widget_class('location_zipcode', 'zip-field')


class VehicleInfoForm(Page5SubForm):
    prefix = 'vehicle'
    subform_classname = "vehicle_details"
    subform_title = "Vehicles Details"
    object_name = 'Vehicle'

    class Meta:
        fields = (
            'year', 'make', 'model', 'mileage', 'license_number', 'vin',
            'purchase_date', 'market_value', 'current_loan_balance', 'monthly_payment', 'final_payment_date',
            'lender_name', 'lender_street', 'lender_city', 'lender_state_name', 'lender_zipcode', 'lender_phone',
        )
        exclude = ('formpage', )
        model = VehicleInfo

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['year'].widget.unset_class('number-field')
        self.fields['year'].widget.set_class('year-field')
        self.fields['market_value'].widget.set_class('vvfmv_clb vvmarket_value')
        self.fields['current_loan_balance'].widget.set_class('vvfmv_clb vvcurrent_loan_balance')


class PersonalAssetInfoForm(Page5SubForm):
    prefix = 'personalasset'
    subform_classname = "personalasset_details"
    subform_title = "Personal Assets Details"
    object_name = 'Asset'

    home_location = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        fields = (
            'description',
            'location_street', 'location_city', 'location_state_name', 'location_zipcode', 'location_county',
            'purchase_date', 'market_value', 'current_loan_balance', 'monthly_payment', 'final_payment_date',
            'lender_name', 'lender_street', 'lender_city', 'lender_state_name', 'lender_zipcode', 'lender_phone',
        )
        exclude = ('formpage', )
        model = PersonalAssetInfo

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        dsync = DataSync(self.client)
        home_location = {}
        for af in ('street', 'city', 'state_name', 'zipcode', 'county'):
            home_location["location_" + af] = dsync.get(af)
        if home_location['location_county']:
            home_location['location_county'] = home_location['location_county'].id
        self.fields['home_location'].initial = json.dumps(home_location)
        self.fields['market_value'].widget.set_class('pafmv_clb pamarket_value')
        self.fields['current_loan_balance'].widget.set_class('pafmv_clb pacurrent_loan_balance')
        self.set_widget_class('location_zipcode', 'zip-field')
        self.set_widget_class('home_location', 'home_location')


class Page6Form(ClientFormMixin, ImprovedForm, forms.ModelForm):
    title = "Section 5: Monthly Income and Expenses"

    text_income = PlainTextField(label='', tag='h3', html_text='Income Items')
    text_expenses = PlainTextField(label='', tag='h3', html_text='Expense Items')
    total_income_cnt = PlainTextField(label='Total Income', tag='span', html_text='$ <span>0</span>')
    total_expenses_cnt = PlainTextField(label='Total Expenses', tag='span', html_text='$ <span>0</span>')
    net_difference_cnt = PlainTextField(label='Net Difference', tag='span', html_text='$ <span>0</span>')

    class Meta:
        model = F433aPage6
        # fields = ()
        exclude = ('form', )

    income_fields = ['wages', 'wages_spouse', 'interest', 'net_business_income', 'net_rental_income', 'distributions',
                     'pension', 'pension_spouse', 'social_security', 'social_security_spouse', 'child_support',
                     'alimony', 'other_1', 'other_2']
    expense_fields = ['food_clothing', 'housing', 'vehicle_own', 'vehicle_oper', 'pub_transport', 'health',
                      'oop_healthcare', 'court', 'child_care', 'life_insurance', 'taxes', 'secured_debts',
                      'local_taxes', 'other_expenses']

    def __init__(self, *args, **kwargs):
        suggestions = kwargs.pop('suggestions', [])
        super().__init__(*args, **kwargs)
        self.instance.form = self.client.get_form_433a()
        # reorder a bit
        new_fields_order = list(self.fields.keys())
        new_fields_order.remove('text_income')
        new_fields_order.insert(0, 'text_income')
        new_fields_order.remove('text_expenses')
        ii = new_fields_order.index('food_clothing')
        new_fields_order.insert(ii, 'text_expenses')
        self.fields = OrderedDict((k, self.fields[k]) for k in new_fields_order)
        # for sugg in suggestions:
        #     if sugg['name'] in self.fields:
        #         self.fields[sugg['name']].initial = sugg['value']
        p8 = getattr(self.instance.form, 'page8', None)
        if p8:
            business_income = p8.net_business_income()
            if business_income < 0:
                business_income = 0
            self.fields['net_business_income'] = PlainTextField(
                tag='span', html_text="$ <span>%s</span>" % business_income,
                help_text='This value had been taken from Section 7')
        else:
            self.fields['net_business_income'] = PlainTextField(
                tag='span', html_text='$ <span>0</span>', help_text='Fill Sections 6-7 to count this field correctly!')
        for fname in self.income_fields:
            self.fields[fname].widget.set_class('income_field inpfld')
        for fname in self.expense_fields:
            self.fields[fname].widget.set_class('expense_field inpfld')
        self.reinit_widgets()


class Page7Form(ClientFormMixin, ImprovedForm, forms.ModelForm):
    title = "Section 6: Business Information"

    is_self_employed = forms.BooleanField(
        label="Is the business a sole proprietorship", initial=False, required=False,
        help_text='All other business entities, including limited liability companies, partnerships or corporations, '
        'must complete Form 433-B. This field should be set to proceed with Sections 6 and 7')
    has_payment_processors = forms.BooleanField(
        label='Does the business engage in e-Commerce (Internet sales)?', initial=False, required=False,
        help_text='e.g., PayPal, Authorize.net, Google Checkout, etc.')
    has_creditcards = forms.BooleanField(
        label='Does your business accept credit cards?', initial=False, required=False,
        help_text='')
    has_bank_account = forms.BooleanField(
        label='Do you have a bank account?', initial=False, required=False,
        help_text='Include checking accounts, online bank accounts, money market accounts, savings accounts, '
        'and stored value cards (e.g. payroll cards, government benefit cards, etc.) '
        'Report Personal Accounts in Section 4.')
    has_accounts_receivable = forms.BooleanField(
        label='Do you have accounts receivable accounts?', initial=False, required=False,
        help_text='Include e-payment accounts receivable and factoring companies, and any bartering or '
        'online auction accounts. (List all contracts separately, including contracts awarded, but not started.) '
        'Include Federal Government Contracts.')
    has_business_assets = forms.BooleanField(
        label='Do you have business assets?', initial=False, required=False,
        help_text='Include all tools, books, machinery, equipment, inventory or other assets used in trade or '
        'business. Include Uniform Commercial Code (UCC) filings. Include Vehicles and Real Property '
        'owned/leased/rented by the business, if not shown in Section 4')

    class Meta:
        model = F433aPage7
        fields = ('is_self_employed',
                  'business_name', 'business_street', 'business_city', 'business_state_name',
                  # 'business_county',
                  'business_zipcode',
                  'ein', 'business_type', 'fed_contractor', 'business_web', 'num_employees',
                  'average_gross_monthly_payroll', 'tax_deposit_freq',
                  'has_payment_processors',
                  'has_creditcards', 'total_cash_on_hand', 'bank_balance_date',
                  'has_bank_account', 'total_cash_in_banks',
                  'has_accounts_receivable', 'outstanding_balance',
                  'has_business_assets', 'total_equity'
                  )
        exclude = ('form', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.form = self.client.get_form_433a()
        dsync = DataSync(self.client)
        for f in self.fields:
            value = dsync.get(f)
            if value:
                self.fields[f].initial = value
        pprocs_count, ccs_count, banks_count, accrec_count, busass_count = 0, 0, 0, 0, 0
        if self.instance.pk:
            pprocs_count = self.instance.paymentprocessors.count()
            ccs_count = self.instance.businessccs.count()
            banks_count = self.instance.businessbankaccs.count()
            accrec_count = self.instance.accountsreceivables.count()
            busass_count = self.instance.businessassets.count()
            self.fields['is_self_employed'].initial = True
        self.add_subform_checkbox('has_payment_processors', PaymentProcessorInfoForm.prefix,
                                  reltype='1xn', count=pprocs_count, max_count=2)
        self.add_subform_checkbox('has_creditcards', BusinessCreditCardInfoForm.prefix,
                                  reltype='1xn', count=ccs_count, max_count=3)
        self.add_subform_checkbox('has_bank_account', BusinessBankAccountInfoForm.prefix,
                                  reltype='1xn', count=banks_count, max_count=2)
        self.add_subform_checkbox('has_accounts_receivable', AccountsReceivableInfoForm.prefix,
                                  reltype='1xn', count=accrec_count, max_count=5)
        self.add_subform_checkbox('has_business_assets', BusinessAssetInfoForm.prefix,
                                  reltype='1xn', count=busass_count, max_count=2)
        self.set_widget_class('total_cash_in_banks', 'showhidewith-chk-' + BusinessBankAccountInfoForm.prefix)
        self.set_widget_class('bank_balance_date', 'showhidewith-chk-' + BusinessBankAccountInfoForm.prefix)
        self.set_widget_class('outstanding_balance', 'showhidewith-chk-' + AccountsReceivableInfoForm.prefix)
        self.set_widget_class('total_equity', 'showhidewith-chk-' + BusinessAssetInfoForm.prefix)
        self.set_widget_class('business_zipcode', 'zip-field')
        self.reinit_widgets()


class Page7SubForm(ClientFormMixin, ImprovedForm, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        formpage = kwargs.get('formpage', None)
        super().__init__(*args, **kwargs)
        if not formpage:
            mainform = self.client.get_form_433a()
            if mainform and hasattr(mainform, 'page7'):
                formpage = mainform.page7
        if not self.instance.formpage:
            self.instance.formpage = formpage


class PaymentProcessorInfoForm(Page7SubForm):
    prefix = 'paymentprocessor'
    subform_classname = "paymentprocessor_details"
    subform_title = "Payment Processors Details"
    object_name = 'Payment Processor'

    class Meta:
        # fields = ()
        exclude = ('formpage', )
        model = PaymentProcessorInfo


class BusinessCreditCardInfoForm(Page7SubForm):
    prefix = 'businesscc'
    subform_classname = "businesscc_details"
    subform_title = "Credit Cards Details"
    object_name = 'Credit Card'

    class Meta:
        # fields = ()
        exclude = ('formpage', )
        model = BusinessCreditCardInfo


class BusinessBankAccountInfoForm(Page7SubForm):
    prefix = 'businessbankacc'
    subform_classname = "businessbankacc_details"
    subform_title = "Bank Accounts Details"
    object_name = 'Bank Account'

    class Meta:
        # fields = ()
        exclude = ('formpage', )
        model = BusinessBankAccountInfo

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['account_balance'].widget.set_class('bba_account_balance')
        self.set_widget_class('bank_zipcode', 'zip-field')


class AccountsReceivableInfoForm(Page7SubForm):
    prefix = 'accountsreceivable'
    subform_classname = "accountsreceivable_details"
    subform_title = "Accounts/Notes Receivable Details"
    object_name = 'Account'

    class Meta:
        # fields = ()
        exclude = ('formpage', )
        model = AccountsReceivableInfo

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['amount_due'].widget.set_class('ar_amount_due')
        self.set_widget_class('zipcode', 'zip-field')


class BusinessAssetInfoForm(Page7SubForm):
    prefix = 'businessasset'
    subform_classname = "businessasset_details"
    subform_title = "Business Assets Details"
    object_name = 'Asset'

    class Meta:
        fields = (
            'description',
            'location_street', 'location_city', 'location_state_name', 'location_zipcode', 'location_county',
            'purchase_date', 'market_value', 'current_loan_balance', 'monthly_payment', 'final_payment_date',
            'lender_name', 'lender_street', 'lender_city', 'lender_state_name', 'lender_zipcode', 'lender_phone',
        )
        exclude = ('formpage', )
        model = BusinessAssetInfo

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['current_loan_balance'].widget.set_class('bafmv_clb bacurrent_loan_balance')
        self.fields['market_value'].widget.set_class('bafmv_clb bamarket_value')
        self.set_widget_class('lender_zipcode', 'zip-field')
        self.set_widget_class('location_zipcode', 'zip-field')


class Page8Form(ClientFormMixin, ImprovedForm, forms.ModelForm):
    title = "Section 7: Sole Proprietorship Information"

    text_income = PlainTextField(label='', tag='h3', html_text='Income Items')
    text_expenses = PlainTextField(label='', tag='h3', html_text='Expense Items')
    total_income_cnt = PlainTextField(label='Total Income', tag='span', html_text='$ <span>0</span>')
    total_expenses_cnt = PlainTextField(label='Total Expenses', tag='span', html_text='$ <span>0</span>')
    net_difference_cnt = PlainTextField(label='Net Business Difference', tag='span', html_text='$ <span>0</span>')

    class Meta:
        model = F433aPage8
        # fields = ()
        exclude = ('form', )

    income_fields = ['gross_receipts', 'gross_rental_income', 'interest', 'dividends', 'cash_receipts_other',
                     'other_1_value', 'other_2_value', 'other_3_value', 'other_4_value']
    expense_fields = ['materials', 'inventory', 'gross_wages_and_salaries', 'rent', 'supplies', 'utilities_telephone',
                      'vehicle_suppl', 'maintenance', 'insurance', 'taxes', 'other_expenses']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.form = self.client.get_form_433a()
        self.fields['accounting_method'].widget.attrs.update({
            'data-on-text': 'Cash', 'data-off-text': 'Accrual',
            'data-on-color': 'success', 'data-off-color': 'primary',
        })
        # reorder a bit
        new_fields_order = list(self.fields.keys())
        new_fields_order.remove('text_income')
        new_fields_order.insert(0, 'text_income')
        new_fields_order.remove('text_expenses')
        ii = new_fields_order.index('materials')
        new_fields_order.insert(ii, 'text_expenses')
        self.fields = OrderedDict((k, self.fields[k]) for k in new_fields_order)
        for fname in self.income_fields:
            self.fields[fname].widget.set_class('income_field inpfld')
        for fname in self.expense_fields:
            self.fields[fname].widget.set_class('expense_field inpfld')
        self.reinit_widgets()
