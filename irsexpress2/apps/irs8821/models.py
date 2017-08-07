# -*- coding: utf-8 -*-

"""
    In this file we have to support two similar structures
    as forms 8821 should be filled in for both client and his spouse
"""

from django.db import models
from django.conf import settings
from localflavor.us.models import USSocialSecurityNumberField

from irs_common.utils import make_address
from utils.widgets import PhoneNumberField
from repository.models import County
from repository.const import US_STATES, STATES_EXTENDED
from agents.models import Appointee


# PAGE 1

class F8821Page1Base(models.Model):
    # Page 1, Section 1
    TPNAME = "Taxpayer"
    first_name = models.CharField(max_length=32, null=False, default='')
    middle_name = models.CharField(max_length=32, null=False, blank=True, default='')
    last_name = models.CharField(max_length=32, null=False, default='')
    street = models.CharField(max_length=128, null=False, blank=True, default='')
    apt = models.CharField(max_length=8, null=False, blank=True, default='')
    city = models.CharField(max_length=64, null=False, blank=True, default='')
    state_name = models.CharField('State', choices=STATES_EXTENDED, max_length=64, null=False, blank=True, default='')
    zipcode = models.CharField('Zip', max_length=10, null=False, blank=True, default='')
    county = models.ForeignKey(County, null=True, blank=True, default=None)
    phone = PhoneNumberField('Daytime telephone number', max_length=20, null=False, blank=True, default='')
    phone_ext = models.CharField('Daytime telephone extension', max_length=7, null=False, blank=True, default='')
    ssn = models.CharField(TPNAME + ' identification number(s)', max_length=128, null=True, blank=True, default='')
    plan_number = models.CharField(max_length=64, null=False, blank=True, default='', help_text='If applicable')

    # Appointees
    additional_appointees = models.BooleanField("Would you like to name more than one appointee?", default=False,
                                                help_text='If you wish to name more than one appointee, attach a list '
                                                'to this form')
    appointee = models.ForeignKey(Appointee, verbose_name="Appointee", null=True, blank=True)

    # be careful - in the original form this question is INVERTED!
    specific_use_caf_recorded = models.BooleanField(
        'Is specific use recorded on Centralized Authorization File (CAF)?',
        help_text='If the tax information authorization is for a specific use was recorded on CAF, check this box. '
        'See the instructions.', default=False)

    class Meta:
        abstract = True

    def title(self):
        mdl = ""
        if self.middle_name:
            mdl = " " + self.middle_name
        title = "%s%s %s" % (self.first_name, mdl, self.last_name)
        return title.title()

    def get_phone(self):
        phone = self.phone
        if self.phone_ext:
            phone = "%s ext %s" % (self.phone, self.phone_ext)
        return phone

    def name_address(self):
        """ (Street, City, State, ZIP code) (County of Residence). """
        retval = make_address(
            name=self.title(), apt=self.apt, street=self.street, city=self.city, state=self.state_name,
            zip=self.zipcode, county=self.county)
        return retval

    def app_name_address(self):
        """ (Street, City, State, ZIP code). """
        retval = make_address(
            name=self.app_name, apt=self.app_apt, street=self.app_street, city=self.app_city,
            state=self.app_state_name, zip=self.app_zipcode)
        return retval


class F8821Page1(F8821Page1Base):
    form = models.OneToOneField('Form8821', related_name='page1')
    specific_use_details = models.OneToOneField('SpecificUse', related_name='page', null=True)


class F8821SpousePage1(F8821Page1Base):
    # Page 1, Section 1
    TPNAME = 'Spouse'
    form = models.OneToOneField('Form8821Spouse', related_name='page1')
    specific_use_details = models.OneToOneField('SpecificUseSpouse', related_name='page', null=True)


class SpecificUseBase(models.Model):
    copies = models.BooleanField('Do you want copies sent to the appointee?',
                                 help_text='If you want copies of tax information, notices, and other written '
                                 'communications sent to the appointee on an ongoing basis, check this item. '
                                 'Note: Appointees will no longer receive forms, publications, and other related '
                                 'materials with the notices.', default=False)
    revocation = models.BooleanField('Retention/revocation of prior tax information authorizations', default=False)

    class Meta:
        abstract = True


class SpecificUse(SpecificUseBase):
    TPNAME = "Taxpayer"


class SpecificUseSpouse(SpecificUseBase):
    TPNAME = 'Spouse'


# PAGE 2

class F8821Page2Base(models.Model):
    # Page 2
    TPNAME = "Taxpayer"

    class Meta:
        abstract = True

    def get_subitem_info(self, relation_name, num):
        # helper to use in template
        all_items = getattr(self, relation_name).all()
        if len(all_items) > num:
            return all_items[num]
        return None

    def tax_info_1(self):
        return self.get_subitem_info('tax_infos', 0)

    def tax_info_2(self):
        return self.get_subitem_info('tax_infos', 1)

    def tax_info_3(self):
        return self.get_subitem_info('tax_infos', 2)


class F8821Page2(F8821Page2Base):
    form = models.OneToOneField('Form8821', related_name='page2')


class F8821SpousePage2(F8821Page2Base):
    # Page 2
    TPNAME = 'Spouse'
    form = models.OneToOneField('Form8821Spouse', related_name='page2')


class TaxInformationBase(models.Model):
    TPNAME = "Taxpayer"
    tax_information_type = models.CharField(max_length=32, null=True, default='', blank=True,
                                            help_text='(Income, Employment, Payroll, '
                                            'Excise, Estate, Gift, Civil Penalty, Sec. 4980H Payments, etc.')
    tax_form_number = models.CharField(max_length=16, null=True, default='', blank=True,
                                       help_text='1040, 941, 720, etc.')
    years = models.CharField('Year(s) or Period(s)', max_length=128, null=True, blank=True, default='')
    details = models.CharField('Specific Tax Matters', max_length=128, null=True, blank=True, default='')

    class Meta:
        abstract = True


class TaxInformation(TaxInformationBase):
    formpage = models.ForeignKey(F8821Page2, related_name='tax_infos',
                                 related_query_name='tax_info', null=True)


class TaxInformationSpouse(TaxInformationBase):
    TPNAME = "Spouse"
    formpage = models.ForeignKey(F8821SpousePage2, related_name='tax_infos',
                                 related_query_name='tax_info', null=True)


class Form8821Base(models.Model):
    TPNAME = "Taxpayer"

    class Meta:
        abstract = True

    def percent_completed(self):
        pages = ['page1', 'page2', ]
        completed_pages = 0
        for p in pages:
            if hasattr(self, p):
                completed_pages += 1
        return int(completed_pages / len(pages) * 100)

    def ready(self):
        return True

    def __str__(self):
        return "Form 8821 for %s %s" % (self.TPNAME, self.client.title())


class Form8821(Form8821Base):
    client = models.OneToOneField('clients.Client', related_name='form8821')


class Form8821Spouse(Form8821Base):
    TPNAME = 'Spouse'

    client = models.OneToOneField('clients.Client', related_name='form8821spouse')
