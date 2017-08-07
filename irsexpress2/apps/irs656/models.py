# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings

from localflavor.us.models import USSocialSecurityNumberField

from irs_common.utils import make_address
from utils.widgets import PhoneNumberField
from repository.models import County
from repository.const import STATES_EXTENDED
from agents.models import Preparer


# PAGE 1

class F656Page1(models.Model):
    # Page 1, Section 1
    form = models.OneToOneField('Form656', related_name='page1')
    first_name = models.CharField(max_length=32, null=False)
    middle_name = models.CharField(max_length=32, null=False, blank=True, default='')
    last_name = models.CharField(max_length=32, null=False)
    ssn = USSocialSecurityNumberField("Social Security Number on IRS Account", null=True, blank=True, default='')
    jointoffer = models.OneToOneField('ClientSpouse', related_name='page', null=True)
    ein = models.CharField("Employer Identification Number EIN", max_length=32, null=True, default='', blank=True,
                           help_text="(For self-employed individuals only)")

    street = models.CharField(max_length=128, null=False, blank=True, default='')
    apt = models.CharField(max_length=8, null=False, blank=True, default='')
    city = models.CharField(max_length=64, null=False, blank=True, default='')
    state_name = models.CharField('State', choices=STATES_EXTENDED, max_length=64, null=False, blank=True, default='')
    zipcode = models.CharField('Zip', max_length=10, null=False, blank=True, default='')
    county = models.ForeignKey(County, null=True, blank=True)
    mailingaddr = models.OneToOneField('MailingAddress', related_name='page', null=True)
    businessinfo = models.OneToOneField('BusinessInformation',
                                        related_name='page', null=True)

    def __str__(self):
        return "Page 1 of the form 656 for %s" % (self.form.client.title())

    def title(self):
        mdl = ""
        if self.middle_name:
            mdl = " " + self.middle_name
        return "%s%s %s" % (self.first_name, mdl, self.last_name)

    def address(self):
        """ (Street, City, State, ZIP code) (County of Residence). """
        retval = make_address(
            apt=self.apt, street=self.street, city=self.city, state=self.state_name, zip=self.zipcode,
            county=self.county)
        return retval

    def get_mailing_address(self):
        if self.mailingaddr:
            return self.mailingaddr.address()
        return self.address()

    @property
    def married(self):
        return self.jointoffer is not None


class ClientSpouse(models.Model):
    # return_with = models.BooleanField("Is this a return with your Spouse ?")
    first_name = models.CharField("Spouse First Name", max_length=32, null=False)
    middle_name = models.CharField("Spouse Middle Name", max_length=32, null=False, blank=True, default='')
    last_name = models.CharField("Spouse Last Name", max_length=32, null=False)
    ssn = USSocialSecurityNumberField("Social Security Number on IRS Account", null=True, blank=True, default='')

    def title(self):
        mdl = ""
        if self.middle_name:
            mdl = " " + self.middle_name
        return "%s%s %s" % (self.first_name, mdl, self.last_name)

    def __str__(self):
        return "Spouse of client %s" % (self.formpage.form.client.title())


class MailingAddress(models.Model):
    street = models.CharField(max_length=128, null=False, blank=True, default='')
    apt = models.CharField(max_length=8, null=False, blank=True, default='')
    city = models.CharField(max_length=64, null=False, blank=True, default='')
    state_name = models.CharField('State', choices=STATES_EXTENDED, max_length=64, null=False, blank=True, default='')
    zipcode = models.CharField('Zip', max_length=10, null=False, blank=True, default='')
    county = models.ForeignKey(County, null=True, blank=True)

    def address(self):
        """ (Street, City, State, ZIP code) (County of Residence). """
        retval = make_address(
            apt=self.apt, street=self.street, city=self.city, state=self.state_name, zip=self.zipcode,
            county=self.county)
        return retval


class BusinessInformation(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True, default='')
    ein = models.CharField("Employer Identification Number", max_length=32, null=True, default='', blank=True)
    street = models.CharField(max_length=128, null=False, blank=True, default='')
    apt = models.CharField(max_length=8, null=False, blank=True, default='')
    city = models.CharField(max_length=64, null=False, blank=True, default='')
    state_name = models.CharField('State', choices=STATES_EXTENDED, max_length=64, null=False, blank=True, default='')
    zipcode = models.CharField('Zip', max_length=10, null=False, blank=True, default='')
    phone = PhoneNumberField('Phone', max_length=20, null=False, blank=True, default='')
    primary_contact = models.CharField(max_length=64, null=False, blank=True, default='')

    def address(self):
        """ (Street, City, State, ZIP code) """
        retval = make_address(
            apt=self.apt, street=self.street, city=self.city, state=self.state_name, zip=self.zipcode)
        return retval


# PAGE 2

class F656Page2(models.Model):
    # Page 2
    form = models.OneToOneField('Form656', related_name='page2')
    is_1040_incometax = models.BooleanField(
        '1040 Income Tax', default=False, blank=True,
        help_text="Most likely you will be using this option. 95% of offers are for delinquent income tax. "
        "If you owe income taxes to the IRS, check the box and record every year in which you owe tax to the IRS.")
    years_1040 = models.CharField("Year(s)", max_length=128, null=True, blank=True, default='')
    is_trustfund_recovery_penalty = models.BooleanField(
        'Trust Fund Recovery Penalty', default=False, blank=True,
        help_text="This only applies if you had employees or were responsible for employee payroll in a business that "
        "you worked at. If you have had employees and failed to full pay your federal tax deposits, the IRS may have "
        "asserted a portion of that delinquency against you personally. If so, you need to include every quarter that "
        "the IRS asserted the Trust Fund Recovery Penalty against you. Each quarter you are responsible for is "
        "recorded on the tax lien that the IRS has previously sent you. If you do not have a copy of your tax lien, "
        "the IRS can provide each quarter you are responsible for by merely calling them at 1-800-829-1040.")
    trustfund_person = models.CharField("As a responsible person of", max_length=128, null=True, blank=True,
                                        default='', help_text='enter corporation name')
    trustfund_periods = models.CharField("For failure to pay withholding and Federal Insurance Contributions Act "
                                         "taxes (Social Security taxes), for period(s) ending",
                                         max_length=128, null=True, blank=True)
    is_941_qtaxreturn = models.BooleanField(
        "941 Employer's Quarterly Federal Tax Return", default=False, blank=True,
        help_text="If you have employees and are delinquent with your payroll tax, your problem may be complex and "
        "we recommend that you consult with our office or a tax professional. If you proceed with your offer, then "
        "be sure to record every quarter that you are delinquent with employment federal tax deposits.")
    qtaxreturn_941_periods = models.CharField("Quarterly period(s)", max_length=128, null=True, blank=True, default='')
    is_940_afuta = models.BooleanField(
        "940 Employer's Annual Federal Unemployment (FUTA) Tax Return", default=False, blank=True,
        help_text="If you have employees and are delinquent with your payroll tax, your problem may be complex and "
        "we recommend that you consult with our office or a tax professional. If you proceed with your offer, then "
        "be sure to record every quarter that you are delinquent with employment federal tax deposits.")
    years_940 = models.CharField("Years", max_length=128, null=True, blank=True, default='')
    is_other_taxes = models.BooleanField(
        "Other Federal Tax(es)", default=False, blank=True,
        help_text="This is exceedingly rare and usually applies to individuals who owe excise taxes")
    othertaxes_types_periods = models.CharField("Type(s) and Period(s)", max_length=128, null=True,
                                                blank=True, default='')
    businesstaxdebt = models.OneToOneField('BusinessTaxDebt', related_name='page', null=True)
    attachment_date = models.DateField("If you need more space, use attachment and title it \"Attachment to Form "
                                       "656 dated (this date)\"", null=True, blank=True, default=None,
                                       help_text="Make sure to sign and date the attachment")


class BusinessTaxDebt(models.Model):
    is_1120_incometax = models.BooleanField(
        '1120 Income Tax', default=False, blank=True,
        help_text=""
        "If you owe income taxes to the IRS, check the box and record every year in which you owe tax to the IRS.")
    years_1120 = models.CharField("Year(s)", max_length=128, null=True, blank=True, default='')
    is_941_qtaxreturn_bus = models.BooleanField(
        "941 Employer's Quarterly Federal Tax Return", default=False, blank=True,
        help_text="If you have employees and are delinquent with your payroll tax, your problem may be complex and "
        "we recommend that you consult with our office or a tax professional. If you proceed with your offer, then "
        "be sure to record every quarter that you are delinquent with employment federal tax deposits.")
    qtaxreturn_941_periods_bus = models.CharField("Quarterly period(s)", max_length=128, null=True,
                                                  blank=True, default='')
    is_940_afuta_bus = models.BooleanField(
        "940 Employer's Annual Federal Unemployment (FUTA) Tax Return", default=False, blank=True,
        help_text="If you have employees and are delinquent with your payroll tax, your problem may be complex and "
        "we recommend that you consult with our office or a tax professional. If you proceed with your offer, then "
        "be sure to record every quarter that you are delinquent with employment federal tax deposits.")
    years_940_bus = models.CharField("Years", max_length=128, null=True, blank=True, default='')
    is_other_taxes_bus = models.BooleanField(
        "Other Federal Tax(es)", default=False, blank=True,
        help_text="This is exceedingly rare and usually applies to individuals who owe excise taxes")
    othertaxes_types_periods_bus = models.CharField("Type(s) and Period(s)", max_length=128, null=True,
                                                    blank=True, default='')


# PAGE 3

class F656Page3(models.Model):
    # Page 3
    form = models.OneToOneField('Form656', related_name='page3')
    doubt_collectibility = models.BooleanField(
        "Doubt as to Collectibility", blank=True, default=False,
        help_text="Set if you have insufficient assets and income to pay the full amount")
    exceptional_circumstances = models.BooleanField(
        'Exceptional Circumstances (Effective Tax Administration)', blank=True, default=False,
        help_text='I owe this amount and have sufficient assets to pay the full amount, but due to my exceptional '
        'circumstances, requiring full payment would cause an economic hardship or would be unfair and inequitable. '
        'I am submitting a written narrative explaining my circumstances.')
    circumstances = models.TextField(
        "Explanation of Circumstances", null=True, blank=True, default='',
        help_text='The IRS understands that there are unplanned events or special circumstances, such as serious '
        'illness, where paying the full amount or the minimum offer amount might impair your ability to provide for '
        'yourself and your family. If this is the case and you can provide documentation to prove your situation, '
        'then your offer may be accepted despite your financial profile. Describe your situation here and attach '
        'appropriate documents to this offer application.')


# PAGE 4

class F656Page4(models.Model):
    # Page 4
    form = models.OneToOneField('Form656', related_name='page4')
    low_income_qualify = models.BooleanField("Do you qualify for Low-Income Certification?",
                                             blank=True, default=False)


# PAGE 5

class F656Page5(models.Model):
    PAYDAYS = [(str(d), str(d)) for d in range(1, 29)]
    PAYMONTHS = [(str(d), str(d)) for d in range(1, 24)]

    # Page 5
    form = models.OneToOneField('Form656', related_name='page5')
    # help_text='Note: The total amount must equal all of the proposed '
    # 'payments including the first and last payments.')
    lump_sum_cash = models.BooleanField("Lump Sum Cash", blank=True, help_text='Check here if you will pay your offer '
                                        'in 5 or fewer payments in 5 or fewer months from the date of acceptance')
    debt_total = models.PositiveIntegerField("Total debt owed to the IRS", blank=True, default=0)
    assessed_date = models.DateField("IRS Assessed Date", null=True, blank=True)
    monthly_income = models.PositiveIntegerField("The Tax Payer's available monthly income", blank=True, default=0)
    offer_amount_lumpsum = models.PositiveIntegerField("Total amount of your offer", null=True, blank=True, default=0, )
    initial_payment = models.PositiveIntegerField("20% Initial Payment", null=True, blank=True, default=0, )
    payment_1 = models.PositiveIntegerField("Payment within 1 month", null=True, blank=True, default=0, )
    payment_2 = models.PositiveIntegerField("Payment within 2 months", null=True, blank=True, default=0, )
    payment_3 = models.PositiveIntegerField("Payment within 3 months", null=True, blank=True, default=0, )
    payment_4 = models.PositiveIntegerField("Payment within 4 months", null=True, blank=True, default=0, )
    payment_5 = models.PositiveIntegerField("Payment within 5 months", null=True, blank=True, default=0, )

    periodic_payment = models.BooleanField("Periodic Payment", blank=True,
                                           help_text='Check here if you will pay your offer in full in 6 to 24 months')
    offer_amount_period = models.PositiveIntegerField("Total amount of your offer", null=True, blank=True, default=0, )
    offer_included = models.PositiveIntegerField("Included with this offer", null=True, blank=True, default=0,)
    monthly_payment = models.PositiveIntegerField("Monthly payment", null=True, blank=True, default=0,)
    payment_day = models.CharField('Day you want to make your payment each month', max_length=3, null=True,
                                   blank=True, choices=PAYDAYS)
    pay_months = models.CharField('Total months', max_length=3, null=True, blank=True, choices=PAYMONTHS)
    final_payment = models.PositiveIntegerField("Final payment", null=True, blank=True, default=0,)
    final_payment_day = models.CharField('Final payment day', max_length=3, null=True, blank=True, choices=PAYDAYS)
    final_pay_month = models.CharField('Final payment month', max_length=3, null=True, blank=True, choices=PAYMONTHS)

    def remaining_balance(self):
        return self.offer_amount_lumpsum - self.initial_payment


# PAGE 6

class F656Page6(models.Model):
    # Page 6
    form = models.OneToOneField('Form656', related_name='page6')

    tax_form = models.CharField(max_length=20, null=True, blank=True, default='')
    tax_year = models.CharField("Tax year/quarter", max_length=20, null=True, blank=True, default='')
    has_deposit = models.BooleanField("Would you like to treat any part of the payment as a deposit?", blank=True)
    total_payment = models.PositiveIntegerField(null=True, blank=True, default=0)
    initial_payment = models.PositiveIntegerField(null=True, blank=True, default=0)
    deposit_payment = models.PositiveIntegerField(null=True, blank=True, default=0)

    funds_source = models.TextField("Source of Funds", null=True, blank=True, default='', help_text='Tell us where '
                                    'you will obtain the funds to pay your offer. You may consider borrowing from '
                                    'friends and/or family, taking out a loan, or selling assets.')
    all_taxreturns_filed = models.BooleanField("I certify that I have filed all required tax returns", default=True)
    noreturn_for = models.BooleanField(
        "I certify that I was not required to file a tax return for the following years", default=True)
    noreturn_for_years = models.CharField("Years", max_length=64, null=True, blank=True, default='')


# PAGE 7

class F656Page7(models.Model):
    # Page 7
    form = models.OneToOneField('Form656', related_name='page7')
    preparer = models.ForeignKey(Preparer, verbose_name="Paid Preparer", null=True, blank=True,
                                 help_text="To add a Preparer - go to Management -> Preparers")
    preparer_date = models.DateField("Paid Preparer Sign Date", null=True, blank=True)
    allow_designee = models.BooleanField("Do you want to allow another person to discuss this offer with the IRS?",
                                         blank=True, default=False)
    designee_name = models.CharField("Designee's name", max_length=64, null=True, blank=True, default='')
    designee_phone = PhoneNumberField("Designee's phone", max_length=20, null=False, blank=True, default='')


class Form656(models.Model):

    client = models.OneToOneField('clients.Client', related_name='form656')

    def percent_completed(self):
        pages = ['page1', 'page2', 'page3', 'page4', 'page5', 'page6', 'page7', ]
        completed_pages = 0
        for p in pages:
            if hasattr(self, p):
                completed_pages += 1
        return int(completed_pages / len(pages) * 100)

    def ready(self):
        return True

    def __str__(self):
        return "Form 656 for %s" % (self.client.title())
