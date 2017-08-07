
from django.db import models

from repository.const import STATES_EXTENDED
from utils.widgets import PhoneNumberField
from irs_common.utils import make_address


class BaseAgent(models.Model):
    name = models.CharField('Name', max_length=128, null=False, default='')
    street = models.CharField('Street', max_length=128, null=False, blank=False, default='')
    apt = models.CharField('Apt No', max_length=8, null=False, blank=True, default='')
    city = models.CharField('City', max_length=64, null=False, blank=False, default='')
    state_name = models.CharField('State', choices=STATES_EXTENDED, max_length=64, null=False,
                                  blank=False, default='')
    zipcode = models.CharField('Zip', max_length=10, null=False, blank=False, default='')
    # https://www.irs.gov/Businesses/Small-Businesses-&-Self-Employed/What-is-a-CAF-number
    caf = models.CharField("CAF No", max_length=12, null=False, blank=True, default='',
                           help_text='Nine-digits code')
    ptin = models.CharField('PTIN', max_length=10, null=False, blank=True, default='',
                            help_text='Eight-digits code')
    phone = PhoneNumberField('Telephone', max_length=20, null=False, blank=True, default='')

    class Meta:
        abstract = True
        ordering = ('id', )

    def get_address(self):
        """ (Street, City, State, ZIP code). """
        retval = make_address(
            apt=self.apt, street=self.street, city=self.city, state=self.state_name,
            zip=self.zipcode)
        return retval

    def get_caf_or_ptin(self):
        if self.caf:
            return "R%s" % self.caf
        return self.ptin

    def __str__(self):
        return "%s %s" % (self._meta.model_name.title(), self.name)


class Appointee(BaseAgent):
    fax = PhoneNumberField('Fax', max_length=20, null=False, blank=True, default='')
    addr_new = models.BooleanField("Is Appointee's address new?", default=False)
    phone_new = models.BooleanField("Is Appointee's telephone new?", default=False)
    fax_new = models.BooleanField("Is Appointee's fax new?", default=False)

    def name_address(self):
        retval = self.name + "\\n" + self.get_address()
        return retval


class Preparer(BaseAgent):
    firm_name = models.CharField("Firm's name (or taxpayer's if self-employed)",
                                 max_length=32, blank=True, null=True, default='')

    def get_firm_name_address(self):
        retval = self.firm_name + " " + self.get_address()
        return retval
