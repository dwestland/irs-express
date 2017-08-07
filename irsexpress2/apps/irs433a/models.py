# -*- coding: utf-8 -*-

import datetime
from dateutils import relativedelta

from django.db import models
from django.conf import settings
from localflavor.us.models import USSocialSecurityNumberField

from irs_common.utils import make_address
from utils.widgets import PhoneNumberField
from repository.models import County
from repository.const import US_STATES, STATES_EXTENDED, PAYPERIODS


# PAGE 1

class F433aPage1(models.Model):
    # Page 1, Section 1
    form = models.OneToOneField('Form433a', related_name='page1')
    first_name = models.CharField(max_length=32, null=False)
    middle_name = models.CharField(max_length=32, null=False, blank=True, default='')
    last_name = models.CharField(max_length=32, null=False)
    ssn = USSocialSecurityNumberField("Social Security Number on IRS Account", null=True, default='', blank=True)
    ein = models.CharField("Employer Identification Number EIN", max_length=32, null=True, default='', blank=True,
                           help_text="This is used if you are operating or receiving income under a "
                           "separate tax ID number. This can also be a corporate EIN")

    street = models.CharField(max_length=128, null=False, blank=True, default='')
    apt = models.CharField(max_length=8, null=False, blank=True, default='')
    city = models.CharField(max_length=64, null=False, blank=True, default='')
    state_name = models.CharField('State', choices=STATES_EXTENDED, max_length=64, null=False, blank=True, default='')
    zipcode = models.CharField('Zip', max_length=10, null=False, blank=True, default='')
    county = models.ForeignKey(County, null=True, blank=True)

    phone_home = PhoneNumberField('Home Phone', max_length=20, null=False, blank=True, default='')
    phone_home_bttc = models.CharField('Home: Best Time to Call', max_length=32, null=False, blank=True, default='')
    phone_cell = PhoneNumberField('Cell Phone', max_length=20, null=False, blank=True, default='')
    phone_work = PhoneNumberField('Work Phone', max_length=20, null=False, blank=True, default='')
    phone_work_ext = models.CharField('Work Phone Ext', max_length=6, null=False, blank=True, default='')
    phone_work_bttc = models.CharField('Work: Best Time to Call', max_length=32, null=False, blank=True, default='')
    phone_work_cell = PhoneNumberField('Business Cell Phone', max_length=20, null=False, blank=True, default='')

    driverlicense = models.CharField("Taxpayer Driver's License Number and State", max_length=128,
                                     null=False, blank=True, default='',
                                     help_text="")

    birthdate = models.DateField(null=True, blank=True, default=None)
    spouse = models.OneToOneField('ClientSpouse', related_name='page', null=True)

    additional_notes = models.TextField("Additional Info", null=True, blank=True,
                                        help_text="Use this space to add any additional information "
                                        "for 433-A, Section 1")

    def __str__(self):
        return "Page 1 of the form 433-1 for %s" % (self.form.client.title())

    def title(self):
        mdl = ""
        if self.middle_name:
            mdl = " " + self.middle_name
        title = "%s%s %s" % (self.first_name, mdl, self.last_name)
        return title.title()

    def address(self):
        """ (Street, City, State, ZIP code) (County of Residence). """
        retval = make_address(
            apt=self.apt, street=self.street, city=self.city, state=self.state_name, zip=self.zipcode,
            county=self.county)
        return retval

    def dependents_str(self):
        retval = []
        for dep in self.dependents.all():
            retval.append(dep.title())
        return "; ".join(retval)

    def get_family_size(self):
        cnt = 1 + self.dependents.count()
        if self.married:
            cnt += 1
        return cnt

    def get_family_ages_list(self) -> list:
        retval = []
        # age of taxpayer
        retval.append(relativedelta(datetime.datetime.now(), self.birthdate).years)
        if self.spouse:
            # age of spouse
            retval.append(relativedelta(datetime.datetime.now(), self.spouse.birthdate).years)
        # ages of all dependents
        retval.extend(self.dependents.values_list('age', flat=True))
        return retval

    @property
    def married(self):
        return self.spouse is not None


class ClientDependent(models.Model):
    formpage = models.ForeignKey(F433aPage1, related_name='dependents', related_query_name='dependent', null=True)
    first_name = models.CharField(max_length=32, null=False)
    last_name = models.CharField(max_length=32, null=False)
    age = models.PositiveIntegerField(default=0, blank=True)
    relationship = models.CharField(max_length=32, null=True, blank=True, default='')

    class Meta:
        ordering = ('id', )

    def title(self):
        return "%s %s, %s, %s" % (self.first_name, self.last_name, self.age, self.relationship)


class ClientSpouse(models.Model):
    return_with = models.BooleanField("Is this a return with your Spouse ?")
    first_name = models.CharField("Spouse First Name", max_length=32, null=False)
    middle_name = models.CharField("Spouse Middle Name", max_length=32, null=False, blank=True, default='')
    last_name = models.CharField("Spouse Last Name", max_length=32, null=False)
    ssn = USSocialSecurityNumberField("Social Security Number on IRS Account", null=True, default='', blank=True)
    birthdate = models.DateField("Spouse Birth Date", null=True, blank=True, default=None)
    driverlicense = models.CharField("Spouse Driver's License Number and State", max_length=128,
                                     null=False, blank=True, default='', help_text="")

    def title(self):
        mdl = ""
        if self.middle_name:
            mdl = " " + self.middle_name
        title = "%s%s %s" % (self.first_name, mdl, self.last_name)
        return title.title()

    def __str__(self):
        return "Spouse of client %s" % (self.formpage.form.client.title())


# PAGE 2

class F433aPage2(models.Model):
    # Page 1, Section 2
    form = models.OneToOneField('Form433a', related_name='page2')
    employment_info = models.OneToOneField('EmploymentInfo', related_name='page2_as_taxpayer', null=True)
    spouse_employment_info = models.OneToOneField('EmploymentInfo', related_name='page2_as_spouse', null=True)

    additional_notes = models.TextField("Additional Info", null=True, blank=True,
                                        help_text="Use this space to add any additional information "
                                        "for 433-A, Section 2")


class EmploymentInfo(models.Model):
    employer_name = models.CharField(max_length=64, blank=True, null=True, default='',
                                     help_text='If your self employed and do not have a business name, write "self"')
    street = models.CharField(max_length=128, null=False, blank=True, default='')
    city = models.CharField(max_length=64, null=False, blank=True, default='')
    state_name = models.CharField('State', choices=STATES_EXTENDED, max_length=64, null=False, blank=True, default='')
    zipcode = models.CharField('Zip', max_length=10, null=False, blank=True, default='')
    phone_work = PhoneNumberField('Work Phone', max_length=20, null=False, blank=True, default='')
    contact_at_work_allowed = models.BooleanField('Does employer allow contact at work?', default=False)
    long_work_years = models.PositiveIntegerField("How long with this employer (Years)", default=0)
    long_work_month = models.PositiveIntegerField("How long with this employer (Months)", default=0)
    occupation = models.CharField(max_length=128, null=True, blank=True, default='')
    w4extemptions = models.PositiveIntegerField('Number of exemptions claimed on Form W-4', null=True, default=0,
                                                help_text='This is only if you are a w-2 wage earner and '
                                                'do not receive a "1099".')
    pay_period = models.CharField(max_length=16, choices=PAYPERIODS,
                                  help_text='Indicate if you get paid weekly, biweekly or monthly.')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._page2 = None
        self.page2rel = None

    def address(self):
        """ (Street, City, State, ZIP code) """
        retval = make_address(
            street=self.street, city=self.city, state=self.state_name, zip=self.zipcode)
        return retval

    @property
    def page2(self):
        if not self._page2:
            if hasattr(self, 'page2_as_taxpayer'):
                self._page2 = self.page2_as_taxpayer
                self.page2rel = 'taxpayer'
            if hasattr(self, 'page2_as_spouse'):
                self._page2 = self.page2_as_spouse
                self.page2rel = 'spouse'
        return self._page2


# PAGE 3

class F433aPage3(models.Model):
    # Page 1, Section 3
    form = models.OneToOneField('Form433a', related_name='page3')
    lawsuit_party = models.OneToOneField('LawsuitPartyInfo', related_name='page', null=True)
    bankruptcy = models.OneToOneField('BankruptcyInfo', related_name='page', null=True)
    beneficiary = models.OneToOneField('BeneficiaryInfo', related_name='page', null=True)
    liveabroad = models.OneToOneField('LiveAbroadDetails', related_name='page', null=True)
    trustee = models.OneToOneField('TrusteeDetails', related_name='page', null=True)
    safe = models.OneToOneField('SafeDetails', related_name='page', null=True)
    asset_transfer = models.OneToOneField('AssetTransferDetails', related_name='page', null=True)

    additional_notes = models.TextField("Additional Info", null=True, blank=True,
                                        help_text="Use this space to add any additional information "
                                        "for 433-A, Section 3")


class LawsuitPartyInfo(models.Model):
    # is_defendant: (False: Plaintiff, True: Defendant)
    is_defendant = models.BooleanField("Plaintiff or a Defendant?", default=False)
    location = models.CharField("Location of Filing", max_length=128, null=True, blank=True, default='')
    representer = models.CharField("Represented by", max_length=128, null=True, blank=True, default='',
                                   help_text="Who is the lawyer handling your law suit.")
    case_number = models.CharField("Case Number", max_length=16, null=True, blank=True, default='')
    amount = models.PositiveIntegerField("Amount of Suit", default=0,
                                         help_text='Many times there is no "demanded" amount.'
                                         ' If that is the case, place 0 here')
    completion_date = models.DateField("Possible Completion Date", null=True, blank=True, default=None,
                                       help_text="Sometimes, this information is not available or unknown at this time")
    subject = models.CharField("Subject of Suit", max_length=256, null=True, blank=True, default='',
                               help_text="What is the cause of action? Ie. car accident, etc")


class BankruptcyInfo(models.Model):
    filed = models.DateField("Date Filed", null=True, default=None, blank=True)
    dismissed = models.DateField("Date Dismissed", null=True, blank=True, default=None)
    discharged = models.DateField("Date Discharged", null=True, blank=True, default=None)
    petition_number = models.CharField("Petition Number", max_length=16, null=True, blank=True, default='')
    location = models.CharField("Location", max_length=128, null=True, blank=True, default='')


class BeneficiaryInfo(models.Model):
    place = models.CharField("Place where recorded", max_length=128, null=True, blank=True, default='')
    ein = models.CharField("Employer Identification Number (EIN)", max_length=32, null=True, blank=True, default='')
    name = models.CharField("Name of the trust, estate, or policy", max_length=128, null=True, blank=True, default='')
    amount = models.PositiveIntegerField("Anticipated amount to be received", default=0)
    whenreceive = models.DateField("When will the amount be received", null=True, blank=True, default=None)


class LiveAbroadDetails(models.Model):
    date_from = models.DateField("From", null=True, blank=True, default=None)
    date_to = models.DateField("To", null=True, blank=True, default=None)


class TrusteeDetails(models.Model):
    name = models.CharField("Name of the trust", max_length=128, null=True, blank=True, default='')
    ein = models.CharField("EIN", max_length=32, null=False, blank=True, default='')


class SafeDetails(models.Model):
    location = models.CharField("Location (Name, address and box number(s))", max_length=256,
                                null=True, blank=True, default='')
    contents = models.CharField(max_length=256, null=True, blank=True, default='')
    value = models.PositiveIntegerField(null=False, default=0)


class AssetTransferDetails(models.Model):
    assetlist = models.CharField("List Asset(s)", max_length=128, null=True, blank=True, default='')
    value = models.PositiveIntegerField("Value at Time of Transfer", null=False, default=0)
    date = models.DateField("Date Transferred", null=True, blank=True, default=None)
    recipient = models.CharField("To Whom or Where was it Transferred", max_length=128,
                                 null=True, blank=True, default='')


# PAGE 4

class F433aPage4(models.Model):
    # Page 2, Section 4
    form = models.OneToOneField('Form433a', related_name='page4')
    cash_on_hand = models.PositiveIntegerField(null=False, default=0,
                                               help_text='Include cash that is not in a bank. '
                                               'Most people have under $100 "cash"')
    bank_balance_date = models.DateField("Bank Account Balance As of", null=True, blank=True, default=None,
                                         help_text='This is the date you are preparing the form')
    loan_balance_date = models.DateField("Loan Balance As of", null=True, blank=True, default=None,
                                         help_text='This is the date you are preparing the form')
    cc_amount_owed_date = models.DateField(" Amount Owed as of", null=True, blank=True, default=None,
                                           help_text='')
    cc_available_credit_date = models.DateField("Available Credit as of", null=True, blank=True, default=None,
                                                help_text='The IRS trying to determine unused credit that you may '
                                                'still have access to. Generally this section applies to credit cards')

    total_cash = models.IntegerField(null=False, default=0,
                                     help_text='Auto-calculated, correct the amounts from any attachments')
    total_equity = models.IntegerField(null=False, default=0,
                                       help_text='Auto-calculated, correct the amounts from any attachments')
    total_credit = models.IntegerField("Total Available Credit", null=False, default=0,
                                       help_text='Auto-calculated, correct the amounts from any attachments')
    total_available_cash = models.IntegerField(null=False, default=0,
                                               help_text='Auto-calculated, correct the amounts from any attachments')

    banking_additional_info = models.TextField(
        null=True, blank=True, default='',
        help_text="If you have additional checking, online bank accounts, money market accounts, savings accounts, "
        "stored value cards (e.g., payroll cards, government benefit cards, etc.) List safe deposit boxes "
        "including location and contents, enter the information here")
    investment_additional_info = models.TextField(
        null=True, blank=True, default='',
        help_text='If you have additional investments, enter the information here')
    credit_additional_info = models.TextField(
        null=True, blank=True, default='',
        help_text='If you have additional credit available, enter the information here')
    insurance_additional_info = models.TextField(
        null=True, blank=True, default='',
        help_text='If you have additional Life Insurance, enter the information here')

    def get_subitem_info(self, relation_name, num):
        # helper to use in template
        all_items = getattr(self, relation_name).all()
        if len(all_items) > num:
            return all_items[num]
        return None

    def bank_account_info_1(self):
        return self.get_subitem_info('bank_accounts', 0)

    def bank_account_info_2(self):
        return self.get_subitem_info('bank_accounts', 1)

    def bank_account_info_3(self):
        return self.get_subitem_info('bank_accounts', 2)

    def insurance_info_1(self):
        return self.get_subitem_info('insurances', 0)

    def insurance_info_2(self):
        return self.get_subitem_info('insurances', 1)

    def insurance_info_3(self):
        return self.get_subitem_info('insurances', 2)

    def investment_info_1(self):
        return self.get_subitem_info('investments', 0)

    def investment_info_2(self):
        return self.get_subitem_info('investments', 1)

    def investment_info_3(self):
        return self.get_subitem_info('investments', 2)

    def credit_info_1(self):
        return self.get_subitem_info('credits', 0)

    def credit_info_2(self):
        return self.get_subitem_info('credits', 1)


class BankAccountInfo(models.Model):
    formpage = models.ForeignKey(F433aPage4, related_name='bank_accounts', related_query_name='bank_account', null=True)
    account_type = models.CharField(max_length=32, null=True, blank=True, default='')
    bank_name = models.CharField(max_length=128, null=True, blank=True, default='')
    street = models.CharField(max_length=128, null=False, blank=True, default='')
    city = models.CharField(max_length=64, null=False, blank=True, default='')
    state_name = models.CharField('State', choices=STATES_EXTENDED, max_length=64, null=False, blank=True, default='')
    zipcode = models.CharField('Zip', max_length=10, null=False, blank=True, default='')
    account_number = models.CharField(max_length=32, null=True, blank=True, default='')
    account_balance = models.PositiveIntegerField(null=False, default=0)

    class Meta:
        ordering = ('id', )

    def name_address(self):
        """ (Street, City, State, ZIP code) """
        retval = make_address(
            name=self.bank_name, street=self.street, city=self.city, state=self.state_name, zip=self.zipcode, wrap=2)
        return retval


class InvestmentInfo(models.Model):
    formpage = models.ForeignKey(F433aPage4, related_name='investments', related_query_name='investment', null=True)
    investment_type = models.CharField(max_length=32, null=True, blank=True, default='')
    full_name = models.CharField(max_length=128, null=True, blank=True, default='')
    street = models.CharField(max_length=128, null=False, blank=True, default='')
    city = models.CharField(max_length=64, null=False, blank=True, default='')
    state_name = models.CharField('State', choices=STATES_EXTENDED, max_length=64, null=False, blank=True, default='')
    zipcode = models.CharField('Zip', max_length=10, null=False, blank=True, default='')
    phone = PhoneNumberField('Phone', max_length=20, null=False, blank=True, default='')
    current_value = models.PositiveIntegerField(null=False, default=0)
    loan_balance = models.PositiveIntegerField(null=True, default=0)

    class Meta:
        ordering = ('id', )

    def name_address(self):
        """ (Street, City, State, ZIP code) """
        retval = make_address(
            name=self.full_name, street=self.street, city=self.city, state=self.state_name, zip=self.zipcode, wrap=2)
        return retval

    def equity(self):
        return self.current_value - self.loan_balance


class CreditInfo(models.Model):
    formpage = models.ForeignKey(F433aPage4, related_name='credits', related_query_name='credit', null=True)
    name = models.CharField("Name of Institution", max_length=128, null=True, blank=True, default='')
    street = models.CharField(max_length=128, null=False, blank=True, default='')
    city = models.CharField(max_length=64, null=False, blank=True, default='')
    state_name = models.CharField('State', choices=STATES_EXTENDED, max_length=64, null=False, blank=True, default='')
    zipcode = models.CharField('Zip', max_length=10, null=False, blank=True, default='')
    account_number = models.CharField(max_length=32, null=True, blank=True, default='')
    credit_limit = models.PositiveIntegerField(null=False, default=0)
    amount_owed = models.PositiveIntegerField(null=False, default=0)

    class Meta:
        ordering = ('id', )

    def name_address(self):
        """ (Street, City, State, ZIP code) """
        retval = make_address(
            name=self.name, street=self.street, city=self.city, state=self.state_name, zip=self.zipcode)
        return retval

    def available_credit(self):
        return self.credit_limit - self.amount_owed


class InsuranceInfo(models.Model):
    formpage = models.ForeignKey(F433aPage4, related_name='insurances', related_query_name='insurance', null=True)
    name = models.CharField("Name", max_length=128, null=True, blank=True, default='')
    street = models.CharField(max_length=128, null=False, blank=True, default='')
    city = models.CharField(max_length=64, null=False, blank=True, default='')
    state_name = models.CharField('State', choices=STATES_EXTENDED, max_length=64, null=False, blank=True, default='')
    zipcode = models.CharField('Zip', max_length=10, null=False, blank=True, default='')
    policy_number = models.CharField(max_length=32, null=True, blank=True, default='')
    policy_owner = models.CharField("owner of the Policy", max_length=64, null=True, blank=True, default='')
    cash_value = models.PositiveIntegerField("Current Cash Value", null=False, default=0)
    loan_balance = models.PositiveIntegerField("Outstanding Loan Balance", null=False, default=0)

    class Meta:
        ordering = ('id', )

    def name_address(self):
        """ (Street, City, State, ZIP code) """
        retval = make_address(
            name=self.name, street=self.street, city=self.city, state=self.state_name, zip=self.zipcode)
        return retval


# PAGE 5

class F433aPage5(models.Model):
    # Page 3, Section 4, part 2
    form = models.OneToOneField('Form433a', related_name='page5')
    real_property_total_equity = models.IntegerField(
        "Total Equity", null=False, default=0, help_text='Auto-calculated, correct the amounts from any attachments')
    vehicles_total_equity = models.IntegerField(
        "Total Equity", null=False, default=0, help_text='Auto-calculated, correct the amounts from any attachments')
    personal_assets_total_equity = models.IntegerField(
        "Total Equity", null=False, default=0, help_text='Auto-calculated, correct the amounts from any attachments')

    def get_subitem_info(self, relation_name, num):
        # helper to use in template
        all_items = getattr(self, relation_name).all()
        if len(all_items) > num:
            return all_items[num]
        return None

    def realproperty_info_1(self):
        return self.get_subitem_info('realproperties', 0)

    def realproperty_info_2(self):
        return self.get_subitem_info('realproperties', 1)

    def vehicle_info_1(self):
        return self.get_subitem_info('vehicles', 0)

    def vehicle_info_2(self):
        return self.get_subitem_info('vehicles', 1)

    def personalasset_info_1(self):
        return self.get_subitem_info('personalassets', 0)

    def personalasset_info_2(self):
        return self.get_subitem_info('personalassets', 1)

    def get_vehicles_count(self):
        return self.vehicles.count()


class BasePropertyModel(models.Model):
    """ All property types from page 3 (and 6) seem to have the same common fields """
    market_value = models.PositiveIntegerField("Current Fair Market Value", null=False, default=0)
    current_loan_balance = models.PositiveIntegerField(null=False, default=0)

    lender_name = models.CharField(max_length=128, null=False, blank=True, default='')
    lender_street = models.CharField(max_length=128, null=False, blank=True, default='')
    lender_city = models.CharField(max_length=64, null=False, blank=True, default='')
    lender_state_name = models.CharField('Lender State', choices=STATES_EXTENDED, max_length=64,
                                         null=False, blank=True, default='')
    lender_zipcode = models.CharField('Lender Zip', max_length=10, null=False, blank=True, default='')
    lender_phone = PhoneNumberField('Lender Phone', max_length=20, null=False, blank=True, default='')
    monthly_payment = models.PositiveIntegerField(null=False, default=0)
    purchase_date = models.DateField("Purchase Lease Date", null=True, blank=True, default=None)
    final_payment_date = models.DateField("Date of final payment", null=True, blank=True, default=None)

    class Meta:
        abstract = True
        ordering = ('id', )

    small_address_field = False

    def lender_name_address(self):
        """ Name, (Street, City, State, ZIP code) """
        retval = make_address(
            name=self.lender_name, street=self.lender_street, city=self.lender_city,
            state=self.lender_state_name, zip=self.lender_zipcode,
            wrap=2 if self.small_address_field else 3)
        return retval

    def equity(self):
        return self.market_value - self.current_loan_balance


class RealPropertyInfo(BasePropertyModel):
    formpage = models.ForeignKey(F433aPage5, related_name='realproperties',
                                 related_query_name='realproperty', null=True)
    description = models.CharField("Property Description", max_length=128, null=True, blank=True, default='')

    location_street = models.CharField("Location Street", max_length=128, null=False, blank=True, default='')
    location_city = models.CharField("Location City", max_length=64, null=False, blank=True, default='')
    location_state_name = models.CharField('Location State', choices=STATES_EXTENDED, max_length=64,
                                           null=False, blank=True, default='')
    location_zipcode = models.CharField('Location Zip', max_length=10, null=False, blank=True, default='')
    location_county = models.ForeignKey(County, null=True, blank=True)

    def location_address(self):
        """ (Street, City, State, ZIP code) and County """
        retval = make_address(
            street=self.location_street, city=self.location_city, state=self.location_state_name,
            zip=self.location_zipcode, county=self.location_county)
        return retval


class VehicleInfo(BasePropertyModel):
    formpage = models.ForeignKey(F433aPage5, related_name='vehicles',
                                 related_query_name='vehicle', null=True)
    mileage = models.PositiveIntegerField(null=False, default=0)
    make = models.CharField(max_length=128, null=True, blank=True, default='')
    year = models.PositiveIntegerField(null=False, default=1999)
    model = models.CharField(max_length=128, null=True, blank=True, default='')
    vin = models.CharField("Vehicle Identification Number", max_length=32, null=True, blank=True, default='')
    license_number = models.CharField("License/Tag Number", max_length=32, null=True, blank=True, default='')

    small_address_field = True

    def get_make_model(self):
        if self.make and self.model:
            return "%s / %s" % (self.make, self.model)
        return ""


class PersonalAssetInfo(BasePropertyModel):
    formpage = models.ForeignKey(F433aPage5, related_name='personalassets',
                                 related_query_name='personalasset', null=True)
    description = models.CharField("Property Description", max_length=128, null=True, blank=True, default='')

    location_street = models.CharField(max_length=128, null=False, blank=True, default='')
    location_city = models.CharField(max_length=64, null=False, blank=True, default='')
    location_state_name = models.CharField('State', choices=STATES_EXTENDED, max_length=64,
                                           null=False, blank=True, default='')
    location_zipcode = models.CharField('Zip', max_length=10, null=False, blank=True, default='')
    location_county = models.ForeignKey(County, null=True, blank=True)

    small_address_field = True

    def location_address(self):
        """ (Street, City, State, ZIP code) and County """
        retval = make_address(
            street=self.location_street, city=self.location_city, state=self.location_state_name,
            zip=self.location_zipcode, county=self.location_county)
        return retval


# PAGE 6


class F433aPage6(models.Model):
    WAGES_COMMENT = """ Enter gross monthly wages and/or salaries.
Do not deduct withholding or allotments taken out of pay, such as insurance payments, credit union deductions,
car payments, etc. To calculate the gross monthly wages and/or salaries:
If paid weekly - multiply weekly gross wages by 4.3. Example: $425.89 x 4.3 = $1,831.33
If paid biweekly (every 2 weeks) - multiply biweekly gross wages by 2.17. Example: $972.45 x 2.17 = $2,110.22
If paid semimonthly (twice each month) - multiply semimonthly gross wages by 2. Example: $856.23 x 2 = $1,712.46"""
    BUSINESS_INCOME_COMMENT = """Enter monthly net business income. This is the amount earned after ordinary and
necessary monthly business expenses are paid. This figure is the amount from page 6, line 89. If the net business
income is a loss, enter “0”. Do not enter a negative number. If this amount is more or less than previous years,
attach an explanation."""
    NET_RENTAL_INCOME_COMMENT = """Enter monthly net rental income. This is the amount earned after ordinary and
necessary monthly rental expenses are paid. Do not include deductions for depreciation or depletion.
If the net rental income is a loss, enter “0.” Do not enter a negative number."""
    DISTRIBUTIONS_COMMENT = """Enter the total distributions from partnerships and subchapter S corporations
reported on Schedule K-1, and from limited liability companies reported on Form 1040, Schedule C, D or E.
Enter total distributions from IRAs if not included under pension income."""
    OTHER_INCOME_COMMENT = """Include agricultural subsidies, unemployment compensation, gambling income,
oil credits, rent subsidies, etc."""
    FOOD_CLOTHING_COMMENT = """Total of food, clothing, housekeeping supplies, and personal care products for
one month. The miscellaneous allowance is for expenses incurred that are not included in any other allowable living
expense items. Examples are credit card payments, bank fees and charges, reading material, and school supplies."""
    HOUSING_COMMENT = """For principal residence: Total of rent or mortgage payment. Add the average monthly expenses
for the following: property taxes, homeowner’s or renter’s insurance, maintenance, dues, fees, and utilities.
Utilities include gas, electricity, water, fuel, oil, other fuels, trash collection, telephone, cell phone,
cable television and internet services."""
    VEHICLE_OPER_COMMENT = """Total of maintenance, repairs, insurance, fuel, registrations, licenses, inspections,
parking, and tolls for one month."""
    PUB_TRANSPORT_COMMENT = """Total of monthly fares for mass transit (e.g., bus, train, ferry, taxi, etc.)"""
    OOP_HEALTHCARE_COMMENT = """Monthly total of medical services, prescription drugs and medical supplies
(e.g., eyeglasses, hearing aids, etc.)"""

    form = models.OneToOneField('Form433a', related_name='page6')
    # Income
    wages = models.PositiveIntegerField('Wages (Taxpayer)', default=0, null=False, blank=True, help_text=WAGES_COMMENT)
    wages_spouse = models.PositiveIntegerField('Wages (Spouse)', default=0, null=False, blank=True,
                                               help_text=WAGES_COMMENT)
    interest = models.PositiveIntegerField('Interest (Dividends)', default=0, null=False, blank=True, help_text='')
    net_business_income = models.PositiveIntegerField('Net Business Income', default=0, null=False, blank=True,
                                                      help_text=BUSINESS_INCOME_COMMENT)
    net_rental_income = models.PositiveIntegerField('Net Rental Income', default=0, null=False, blank=True,
                                                    help_text=NET_RENTAL_INCOME_COMMENT)
    distributions = models.PositiveIntegerField('Distributions', default=0, null=False, blank=True,
                                                help_text=DISTRIBUTIONS_COMMENT)
    pension = models.PositiveIntegerField('Pension (Taxpayer)', default=0, null=False, blank=True,
                                          help_text='')
    pension_spouse = models.PositiveIntegerField('Pension (Spouse)', default=0, null=False, blank=True,
                                                 help_text='')
    social_security = models.PositiveIntegerField('Social Security (Taxpayer)', default=0, null=False, blank=True,
                                                  help_text='')
    social_security_spouse = models.PositiveIntegerField('Social Security (Spouse)', default=0, null=False, blank=True,
                                                         help_text='')
    child_support = models.PositiveIntegerField('Child Support', default=0, null=False, blank=True,
                                                help_text='')
    alimony = models.PositiveIntegerField('Alimony', default=0, null=False, blank=True,
                                          help_text='')
    other_1_name = models.CharField('Other Income 1: Description', max_length=64, null=True, blank=True, default='',
                                    help_text=OTHER_INCOME_COMMENT)
    other_1 = models.PositiveIntegerField('Other Income 1', default=0, null=False, blank=True, help_text='')
    other_2_name = models.CharField('Other Income 2: Description', max_length=64, null=True, blank=True, default='',
                                    help_text=OTHER_INCOME_COMMENT)
    other_2 = models.PositiveIntegerField('Other Income 2', default=0, null=False, blank=True, help_text='')
    # expenses
    food_clothing = models.PositiveIntegerField('Food, Clothing and Misc.', default=0, null=False, blank=True,
                                                help_text=FOOD_CLOTHING_COMMENT)
    housing = models.PositiveIntegerField('Housing and Utilities', default=0, null=False, blank=True,
                                          help_text=HOUSING_COMMENT)
    vehicle_own = models.PositiveIntegerField('Vehicle Ownership Costs', default=0, null=False, blank=True,
                                              help_text='Total of monthly lease or purchase/loan payments.')
    vehicle_oper = models.PositiveIntegerField('Vehicle Operating Costs', default=0, null=False, blank=True,
                                               help_text=VEHICLE_OPER_COMMENT)
    pub_transport = models.PositiveIntegerField('Public Transportation', default=0, null=False, blank=True,
                                                help_text=PUB_TRANSPORT_COMMENT)
    health = models.PositiveIntegerField('Health Insurance', default=0, null=False, blank=True,
                                         help_text='')
    oop_healthcare = models.PositiveIntegerField('Out of Pocket Health Care Costs', default=0, null=False, blank=True,
                                                 help_text=OOP_HEALTHCARE_COMMENT)
    court = models.PositiveIntegerField('Court Ordered Payments', default=0, null=False, blank=True,
                                        help_text='')
    child_care = models.PositiveIntegerField('Child/Dependent Care', default=0, null=False, blank=True,
                                             help_text='')
    life_insurance = models.PositiveIntegerField('Life Insurance', default=0, null=False, blank=True,
                                                 help_text='')
    taxes = models.PositiveIntegerField('Current year taxes (Income/FICA)', default=0, null=False, blank=True,
                                        help_text='Include state and Federal taxes withheld from salary or wages, '
                                        'or paid as estimated taxes.')
    secured_debts = models.PositiveIntegerField('Secured Debts', default=0, null=False, blank=True,
                                                help_text='')
    local_taxes = models.PositiveIntegerField('Delinquent State or Local Taxes', default=0, null=False, blank=True,
                                              help_text='')
    other_expenses = models.PositiveIntegerField('Other Expenses', default=0, null=False, blank=True,
                                                 help_text='')

    def total_income(self):
        net_business_income = 0
        # net_business_income = self.net_business_income
        if hasattr(self.form, 'page8'):
            net_business_income = self.form.page8.net_business_income()
            if net_business_income < 0:
                net_business_income = 0
        income = self.wages + self.wages_spouse + self.interest + net_business_income + self.net_rental_income
        income += self.distributions + self.pension + self.pension_spouse + self.social_security
        income += self.social_security_spouse + self.child_support + self.alimony + self.other_1 + self.other_2
        return income

    def total_expenses(self):
        expenses = self.food_clothing + self.housing + self.vehicle_own + self.vehicle_oper + self.pub_transport
        expenses += self.health + self.oop_healthcare + self.court + self.child_care + self.life_insurance
        expenses += self.taxes + self.secured_debts + self.local_taxes + self.other_expenses
        return expenses

    def net_difference(self):
        netdiff = self.total_income() - self.total_expenses()
        return netdiff

    def save(self, *args, **kwargs):
        if self.net_business_income is None:
            self.net_business_income = 0
        super().save(*args, **kwargs)


# PAGE 7

class F433aPage7(models.Model):
    form = models.OneToOneField('Form433a', related_name='page7')

    business_name = models.CharField(max_length=128, null=True, blank=True, default='')
    business_street = models.CharField(max_length=128, null=False, blank=True, default='')
    business_city = models.CharField(max_length=64, null=False, blank=True, default='')
    business_state_name = models.CharField('Business State', choices=STATES_EXTENDED, max_length=64,
                                           null=False, blank=True, default='')
    # business_county = models.ForeignKey(County, null=True, blank=True)
    business_zipcode = models.CharField('Business Zip', max_length=10, null=False, blank=True, default='')
    ein = models.CharField("Employer Identification Number", max_length=32, null=True, default='', blank=True)
    business_type = models.CharField("Type of Business", max_length=128, null=True, blank=True, default='')
    fed_contractor = models.BooleanField("Federal Contractor?", default=False)
    business_web = models.CharField("Business Website", max_length=256, null=True, blank=True, default='')
    num_employees = models.PositiveIntegerField(null=False, default=0)
    average_gross_monthly_payroll = models.PositiveIntegerField(null=False, default=0, blank=True)
    tax_deposit_freq = models.CharField("Frequency of Tax Deposits", max_length=64, null=True, blank=True, default='')

    bank_balance_date = models.DateField("Bank Account Balance As of", null=True, default=None, blank=True,
                                         help_text='This is the date you are preparing the form')
    total_cash_on_hand = models.PositiveIntegerField(default=0, help_text='Include cash that is not in a bank')
    total_cash_in_banks = models.PositiveIntegerField(
        default=0, help_text='Auto-calculated, correct the amounts from any attachments')
    outstanding_balance = models.PositiveIntegerField(
        'Total Outstanding Balance',
        default=0, help_text='Auto-calculated, correct the amounts from any attachments')
    total_equity = models.PositiveIntegerField(
        default=0, help_text='Auto-calculated, correct the amounts from any attachments')

    def business_name_address(self):
        """ (Street, City, State, ZIP code) and County"""
        retval = make_address(
            name=self.business_name, street=self.business_street, city=self.business_city,
            state=self.business_state_name, zip=self.business_zipcode  # , county=self.business_county
        )
        return retval

    def get_subitem_info(self, relation_name, num):
        # helper to use in template
        all_items = getattr(self, relation_name).all()
        if len(all_items) > num:
            return all_items[num]
        return None

    def paymentprocessor_info_1(self):
        return self.get_subitem_info('paymentprocessors', 0)

    def paymentprocessor_info_2(self):
        return self.get_subitem_info('paymentprocessors', 1)

    def businesscc_info_1(self):
        return self.get_subitem_info('businessccs', 0)

    def businesscc_info_2(self):
        return self.get_subitem_info('businessccs', 1)

    def businesscc_info_3(self):
        return self.get_subitem_info('businessccs', 2)

    def businessbankacc_info_1(self):
        return self.get_subitem_info('businessbankaccs', 0)

    def businessbankacc_info_2(self):
        return self.get_subitem_info('businessbankaccs', 1)

    def accountsreceivable_info_1(self):
        return self.get_subitem_info('accountsreceivables', 0)

    def accountsreceivable_info_2(self):
        return self.get_subitem_info('accountsreceivables', 1)

    def accountsreceivable_info_3(self):
        return self.get_subitem_info('accountsreceivables', 2)

    def accountsreceivable_info_4(self):
        return self.get_subitem_info('accountsreceivables', 3)

    def accountsreceivable_info_5(self):
        return self.get_subitem_info('accountsreceivables', 4)

    def businessasset_info_1(self):
        return self.get_subitem_info('businessassets', 0)

    def businessasset_info_2(self):
        return self.get_subitem_info('businessassets', 1)


class PaymentProcessorInfo(models.Model):
    formpage = models.ForeignKey(F433aPage7, related_name='paymentprocessors',
                                 related_query_name='paymentprocessor', null=True)
    name = models.CharField(max_length=128, null=True, blank=True, default='')
    account_number = models.CharField(max_length=64, null=True, blank=True, default='')
    street = models.CharField(max_length=128, null=False, blank=True, default='')
    city = models.CharField(max_length=64, null=False, blank=True, default='')
    state_name = models.CharField('State', choices=STATES_EXTENDED, max_length=64,
                                  null=False, blank=True, default='')
    zipcode = models.CharField('Zip', max_length=10, null=False, blank=True, default='')
    # account_balance = models.PositiveIntegerField(default=0, null=False)

    class Meta:
        ordering = ('id', )

    def name_address(self):
        """ Name, (Street, City, State, ZIP code) """
        retval = make_address(
            name=self.name, street=self.street, city=self.city,
            state=self.state_name, zip=self.zipcode, wrap=2)
        return retval


class BusinessCreditCardInfo(models.Model):
    formpage = models.ForeignKey(F433aPage7, related_name='businessccs',
                                 related_query_name='businesscc', null=True)
    credit_card = models.CharField(max_length=64, null=True, blank=True, default='')
    merchant_account_number = models.CharField(max_length=64, null=False, blank=True, default='')
    bank_name = models.CharField(max_length=128, null=True, blank=True, default='')
    bank_street = models.CharField(max_length=128, null=False, blank=True, default='')
    bank_city = models.CharField(max_length=64, null=False, blank=True, default='')
    bank_state_name = models.CharField('Bank State', choices=STATES_EXTENDED, max_length=64,
                                       null=False, blank=True, default='')
    bank_zipcode = models.CharField('Bank Zip', max_length=10, null=False, blank=True, default='')

    class Meta:
        ordering = ('id', )

    def bank_name_address(self):
        """ Name, (Street, City, State, ZIP code) """
        retval = make_address(
            name=self.bank_name, street=self.bank_street, city=self.bank_city,
            state=self.bank_state_name, zip=self.bank_zipcode, wrap=2)
        return retval


class BusinessBankAccountInfo(models.Model):
    formpage = models.ForeignKey(F433aPage7, related_name='businessbankaccs',
                                 related_query_name='businessbankacc', null=True)
    account_type = models.CharField('Type of Account', max_length=64, null=True, blank=True, default='')
    account_number = models.CharField(max_length=64, null=True, blank=True, default='')
    account_balance = models.PositiveIntegerField(default=0, null=False)
    bank_name = models.CharField(max_length=128, null=True, blank=True, default='')
    bank_street = models.CharField(max_length=128, null=False, blank=True, default='')
    bank_city = models.CharField(max_length=64, null=False, blank=True, default='')
    bank_state_name = models.CharField('Bank State', choices=STATES_EXTENDED, max_length=64,
                                       null=False, blank=True, default='')
    bank_zipcode = models.CharField('Bank Zip', max_length=10, null=False, blank=True, default='')

    class Meta:
        ordering = ('id', )

    def name_address(self):
        """ Name, (Street, City, State, ZIP code) """
        retval = make_address(
            name=self.bank_name, street=self.bank_street, city=self.bank_city,
            state=self.bank_state_name, zip=self.bank_zipcode, wrap=2)
        return retval


class AccountsReceivableInfo(models.Model):
    formpage = models.ForeignKey(F433aPage7, related_name='accountsreceivables',
                                 related_query_name='accountsreceivable', null=True)
    status = models.CharField(max_length=32, null=True, blank=True, default='', help_text='e.g., age, factored, other')
    name = models.CharField(max_length=128, null=False, blank=True, default='')
    date_due = models.DateField(null=True, default=None, blank=True)
    contract_number = models.CharField(max_length=64, null=True, blank=True, default='',
                                       help_text='Invoice Number or Government Grant or Contract Number')
    street = models.CharField(max_length=128, null=False, blank=True, default='')
    city = models.CharField(max_length=64, null=False, blank=True, default='')
    state_name = models.CharField('State', choices=STATES_EXTENDED, max_length=64,
                                  null=False, blank=True, default='')
    zipcode = models.CharField('Zip', max_length=10, null=False, blank=True, default='')
    amount_due = models.PositiveIntegerField(default=0, null=False)

    class Meta:
        ordering = ('id', )

    def name_address(self):
        """ Name, (Street, City, State, ZIP code) """
        retval = make_address(
            name=self.name, street=self.street, city=self.city,
            state=self.state_name, zip=self.zipcode, wrap=2)
        return retval


class BusinessAssetInfo(BasePropertyModel):
    formpage = models.ForeignKey(F433aPage7, related_name='businessassets',
                                 related_query_name='businessasset', null=True)
    description = models.CharField("Property Description", max_length=128, null=True, blank=True, default='')

    location_street = models.CharField(max_length=128, null=False, blank=True, default='')
    location_city = models.CharField(max_length=64, null=False, blank=True, default='')
    location_state_name = models.CharField('State', choices=STATES_EXTENDED, max_length=64,
                                           null=False, blank=True, default='')
    location_zipcode = models.CharField('Zip', max_length=10, null=False, blank=True, default='')
    location_county = models.ForeignKey(County, null=True, blank=True)

    small_address_field = True

    def location_address(self):
        """ (Street, City, State, ZIP code) and County """
        retval = make_address(
            street=self.location_street, city=self.location_city, state=self.location_state_name,
            zip=self.location_zipcode, county=self.location_county)
        return retval


# PAGE 8

class F433aPage8(models.Model):
    ACCOUNTING_METHODS = (
        ('cash', 'Cash'),
        ('accrual', 'Accrual'),
    )

    form = models.OneToOneField('Form433a', related_name='page8')
    accounting_method = models.BooleanField(  # True=Cash, False=Accrual
        'Accounting Method Used', default=False,  # max_length=8, choices=ACCOUNTING_METHODS,
        help_text='Use the prior 3, 6, 9 or 12 month period to determine your typical business income and expenses.')
    period_start = models.DateField('Income and Expenses period start date', null=True, default=None, blank=True)
    period_end = models.DateField('Income and Expenses period end date', null=True, default=None, blank=True)
    # income values
    gross_receipts = models.PositiveIntegerField(default=0, null=False, blank=True)
    gross_rental_income = models.PositiveIntegerField(default=0, null=False, blank=True)
    interest = models.PositiveIntegerField(default=0, null=False, blank=True)
    dividends = models.PositiveIntegerField(default=0, null=False, blank=True)
    cash_receipts_other = models.PositiveIntegerField('Cash Receipts not included in lines above',
                                                      default=0, null=False, blank=True)
    other_1_name = models.CharField('Other Income 1: description', max_length=64, null=True, blank=True)
    other_1_value = models.PositiveIntegerField('Other Income 1: value', default=0, null=False, blank=True)
    other_2_name = models.CharField('Other Income 2: description', max_length=64, null=True, blank=True)
    other_2_value = models.PositiveIntegerField('Other Income 2: value', default=0, null=False, blank=True)
    other_3_name = models.CharField('Other Income 3: description', max_length=64, null=True, blank=True)
    other_3_value = models.PositiveIntegerField('Other Income 3: value', default=0, null=False, blank=True)
    other_4_name = models.CharField('Other Income 4: description', max_length=64, null=True, blank=True)
    other_4_value = models.PositiveIntegerField('Other Income 4: value', default=0, null=False, blank=True)
    # expenses
    materials = models.PositiveIntegerField(
        'Materials Purchased', default=0, null=False, blank=True,
        help_text='Materials are items directly related to the production of a product or service')
    inventory = models.PositiveIntegerField(
        'Inventory Purchased', default=0, null=False, blank=True,
        help_text='Goods bought for resale')
    gross_wages_and_salaries = models.PositiveIntegerField(default=0, null=False, blank=True)
    rent = models.PositiveIntegerField(default=0, null=False)
    supplies = models.PositiveIntegerField(default=0, null=False, help_text='Supplies are items used in the business '
                                           'that are consumed or used up within one year. This could be the cost of '
                                           'books, office supplies, professional equipment, etc')
    utilities_telephone = models.PositiveIntegerField(
        'Utilities/Telephone', default=0, null=False, help_text='Utilities include gas, electricity, water, oil, '
        'other fuels, trash collection, telephone, cell phone and business internet.', blank=True)
    vehicle_suppl = models.PositiveIntegerField('Vehicle Gasoline/Oil', default=0, null=False, blank=True)
    maintenance = models.PositiveIntegerField('Repairs & Maintenance', default=0, null=False, blank=True)
    insurance = models.PositiveIntegerField(default=0, null=False, blank=True)
    taxes = models.PositiveIntegerField('Current Taxes', default=0, null=False, help_text='Real estate, excise, '
                                        'franchise, occupational, personal property, sales and employer’s portion of '
                                        'employment taxes', blank=True)
    other_expenses = models.PositiveIntegerField('Other Expenses, including installment payments',
                                                 default=0, null=False, blank=True)

    def total_income(self):
        income = self.gross_receipts + self.gross_rental_income + self.interest + self.dividends
        income += self.cash_receipts_other + self.other_1_value + self.other_2_value + self.other_3_value
        income += self.other_4_value
        return income

    def total_expenses(self):
        expenses = self.materials + self.inventory + self.gross_wages_and_salaries + self.rent + self.supplies
        expenses += self.utilities_telephone + self.vehicle_suppl + self.maintenance + self.insurance
        expenses += self.taxes + self.other_expenses
        return expenses

    def net_business_income(self):
        return self.total_income() - self.total_expenses()


# Form itself

class Form433a(models.Model):

    client = models.OneToOneField('clients.Client', related_name='form433a')

    def percent_completed(self):
        pages = ['page1', 'page2', 'page3', 'page4', 'page5', 'page6', 'page7', 'page8']
        completed_pages = 0
        if hasattr(self, 'page7'):  # if not - it might be ok - just not self-employed client
            pages.extend(['page7', 'page8'])
        for p in pages:
            if hasattr(self, p):
                completed_pages += 1
        return int(completed_pages / len(pages) * 100)

    def ready(self):
        return True

    def __str__(self):
        return "Form 433-A for %s" % (self.client.title())
