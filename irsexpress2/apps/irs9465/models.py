# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings

from localflavor.us.models import USSocialSecurityNumberField
from utils.widgets import PhoneNumberField
from repository.models import County
from repository.const import US_STATES, STATES_EXTENDED, PAYPERIODS2


# PAGE 1

class F9465Page1(models.Model):
    # Page 1, Section 1
    form = models.OneToOneField('Form9465', related_name='page1')
    request_for_form = models.CharField('This request is for Form(s)', max_length=128, null=False, blank=True,
                                        help_text='for example, Form 1040 or Form 941', default='')
    request_for_years = models.CharField('What tax year(s) is this Installment Arrangement for', max_length=128,
                                         null=True, default=None, blank=True,
                                         help_text='For example, 2014 and 2015')
    first_name = models.CharField(max_length=32, null=False)
    middle_name = models.CharField(max_length=32, null=False, blank=True, default='')
    last_name = models.CharField(max_length=32, null=False)
    ssn = USSocialSecurityNumberField("Social Security Number on IRS Account", null=True, blank=True, default='')
    jointoffer = models.OneToOneField('ClientSpouse', related_name='page', null=True)
    street = models.CharField(max_length=128, null=False, blank=True, default='')
    apt = models.CharField(max_length=8, null=False, blank=True, default='')
    city = models.CharField(max_length=64, null=False, blank=True, default='')
    state_name = models.CharField('State', choices=STATES_EXTENDED, max_length=64, null=False, blank=True, default='')
    zipcode = models.CharField('Zip', max_length=10, null=False, blank=True, default='')
    county = models.ForeignKey(County, null=True, blank=True)
    country = models.CharField('Foreign Country', max_length=32, null=True, blank=True, default='')
    foreign_county = models.CharField('Foreign province/state/county', max_length=32, null=True, blank=True, default='')
    foreign_zip = models.CharField('Foreign postal code', max_length=8, null=True, blank=True, default='')
    address_new = models.BooleanField('Is this address new since you filed your last tax return?', default=False)

    def city_state_zip(self):
        return ', '.join(r.strip() for r in [self.city, self.state_name, self.zipcode] if r.strip())


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
        return "Spouse of client %s" % (self.page.form.client.title())


# PAGE 2

class F9465Page2(models.Model):
    # Page 1, Section 2
    form = models.OneToOneField('Form9465', related_name='page2')
    business_name = models.CharField('Name of your business', max_length=128, null=False, blank=True, default='',
                                     help_text='Must be no longer operating')
    ein = models.CharField("Employer Identification Number", max_length=32, null=True, default='', blank=True)
    phone_home = PhoneNumberField('Home Phone', max_length=20, null=False, blank=True, default='')
    phone_home_bttc = models.CharField('Home: Best Time to Call', max_length=32, null=False, blank=True, default='')
    phone_work = PhoneNumberField('Work Phone', max_length=20, null=False, blank=True, default='')
    phone_work_ext = models.CharField('Work Phone Ext', max_length=6, null=False, blank=True, default='')
    phone_work_bttc = models.CharField('Work: Best Time to Call', max_length=32, null=False, blank=True, default='')

    employer_name = models.CharField(max_length=64, null=True, blank=True, default='')
    employer_street = models.CharField('Employer Address', max_length=128, null=False, blank=True, default='')
    employer_city = models.CharField(max_length=64, null=False, blank=True, default='')
    employer_state_name = models.CharField('Employer State', choices=STATES_EXTENDED, max_length=64,
                                           null=False, blank=True, default='')
    employer_zipcode = models.CharField('Employer Zip', max_length=10, null=False, blank=True, default='')

    bank_name = models.CharField('Name of your bank or other financial institution', max_length=128,
                                 null=False, blank=True, default='')
    bank_street = models.CharField(max_length=128, null=False, blank=True, default='')
    bank_city = models.CharField(max_length=64, null=False, blank=True, default='')
    bank_state_name = models.CharField('Bank State', choices=STATES_EXTENDED, max_length=64,
                                       null=False, blank=True, default='')
    bank_zipcode = models.CharField('Bank Zip', max_length=10, null=False, blank=True, default='')

    def bank_city_state_zip(self):
        return ', '.join(r.strip() for r in [self.bank_city, self.bank_state_name, self.bank_zipcode] if r.strip())

    def employer_city_state_zip(self):
        return ', '.join(r.strip() for r in [self.employer_city, self.employer_state_name, self.employer_zipcode]
                         if r.strip())


# PAGE 3

class F9465Page3(models.Model):
    PAYDAYS = ((str(d), str(d)) for d in range(1, 27))

    # Page 1, Section 3
    form = models.OneToOneField('Form9465', related_name='page3')
    amount_owed = models.FloatField('Total amount you owe', default=0, null=False,
                                    help_text='as shown on your tax return(s) (or notice(s))')
    amount_paid = models.FloatField(
        'Payment Amount', default=0, null=False,
        help_text='Enter the amount of any payment you are making with your tax return(s) (or notice(s)).')
    can_pay = models.FloatField(
        'Amount you can pay each month', default=0, null=False,
        help_text='Make your payments as large as possible to limit interest and penalty charges. The charges '
        'will continue until you pay in full. If no payment amount is listed here, a payment will be determined '
        'for you by dividing the balance due by 72 months')
    payment_day = models.CharField('Day you want to make your payment each month', max_length=3, choices=PAYDAYS)
    routing_number = models.CharField(max_length=32, null=True, blank=True, default='', help_text='9 digits')
    account_number = models.CharField(max_length=32, null=True, blank=True, default='', help_text='17 digits')
    pay_payroll = models.BooleanField('Do you want to make your payments by payroll deduction?',
                                      help_text='Attach a completed Form 2159, Payroll Deduction Agreement')

    def amount_difference(self):
        return self.amount_owed - self.amount_paid

    def auto_can_pay(self):
        return self.amount_difference() / 72


# PAGE 4

class F9465Page4(models.Model):
    # Page 2 (Part II)
    form = models.OneToOneField('Form9465', related_name='page4')
    county = models.ForeignKey(County, verbose_name='Your primary county', null=True, blank=True)
    married = models.BooleanField("Marital Status")
    expenses_shared = models.BooleanField('Do you share household expenses with your spouse?')
    dependents_cnt = models.PositiveIntegerField("How many dependents will you be able to claim on "
                                                 "this year's tax return?", null=False, blank=True, default=0)
    has_older65 = models.PositiveIntegerField('How many people in your household are 65 or older?',
                                              null=False, blank=True, default=0)
    pay_period = models.CharField('How often are you paid?', max_length=16, choices=PAYPERIODS2,
                                  help_text='Indicate if you get paid weekly, biweekly or monthly.')
    net_income_day = models.FloatField('Net income per pay period', null=False, default=0, help_text='Take home pay')
    spouse_pay_period = models.CharField('How often is your spouse paid?', max_length=16, choices=PAYPERIODS2,
                                         null=True, blank=True)
    spouse_net_income_day = models.FloatField("Spouse's Net income per pay period", null=False, default=0,
                                              help_text='Take home pay')
    vehicles = models.PositiveIntegerField('How many vehicles do you own?', null=False, default=0)
    car_payments = models.PositiveIntegerField('How many car payments do you have each month?', null=False, default=0)
    has_health_insurance = models.BooleanField('Do you have health insurance?')
    premiums_deducted = models.BooleanField('Are your premiums deducted from your paycheck?')
    premiums = models.FloatField('How much are your monthly premiums?', null=False, default=0)
    has_court_payments = models.BooleanField('Do you make court-ordered payments?')
    court_payments_deducted = models.BooleanField('Are your court-ordered payments deducted from your paycheck?')
    court_payments = models.FloatField('How much are your court-ordered payments each month?', null=False, default=0)
    child_care = models.FloatField('Not including any court-ordered payments for child and dependent support, '
                                   'how much do you pay for child or dependent care each month?',
                                   null=False, default=0)


class Form9465(models.Model):

    client = models.OneToOneField('clients.Client', related_name='form9465')

    def percent_completed(self):
        pages = ['page1', 'page2', 'page3', 'page4', ]
        completed_pages = 0
        for p in pages:
            if hasattr(self, p):
                completed_pages += 1
        return int(completed_pages / len(pages) * 100)

    def ready(self):
        return True

    def __str__(self):
        return "Form 9465 for %s" % (self.client.title())
