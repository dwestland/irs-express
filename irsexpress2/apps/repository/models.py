# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone

from .const import STATE_NAMES, TRANSPORTATION_TAX_TYPE

TRANSP_APPLY_BY = (
    ('national', 'National'),
    ('msa', 'MSA'),
    ('region', 'Region'),
)


class County(models.Model):
    state_name = models.CharField('State', choices=STATE_NAMES, max_length=64, null=False, blank=True, default='')
    name = models.CharField('County', max_length=64, null=False, blank=True, default='')

    class Meta:
        ordering = ('state_name', 'name')
        verbose_name_plural = 'Counties'

    def __str__(self):
        return "County: %s / %s" % (self.state_name, self.name)

    def as_str(self):
        """ Just a compatibility """
        return "%s / %s" % (self.state_name, self.name)


class HousingUtilitiesStandard(models.Model):

    DOCUMENT_NAME = "Allowable Living Expense Housing and Utilities Standards"

    county = models.OneToOneField(County, primary_key=True)
    family1 = models.IntegerField('Family of 1', default=0, null=False)
    family2 = models.IntegerField('Family of 2', default=0, null=False)
    family3 = models.IntegerField('Family of 3', default=0, null=False)
    family4 = models.IntegerField('Family of 4', default=0, null=False)
    family_more = models.IntegerField('Family of 5 or more', default=0, null=False)

    class Meta:
        verbose_name = "Allowable Living Expense Housing and Utilities Standards"
        verbose_name_plural = "Allowable Living Expense Housing and Utilities Standards"

    def get_family_expense(self, family_size: int) -> int:
        family_size = int(family_size)
        if family_size == 1:
            return self.family1
        if family_size == 2:
            return self.family2
        if family_size == 3:
            return self.family3
        if family_size == 4:
            return self.family4
        return self.family_more

    def __str__(self):
        return "HousingUtilitiesStandard for %s / %s" % (self.county.state_name, self.county.name)


class FoodClothingStandard(models.Model):
    DOCUMENT_NAME = "National Standards: Food, Clothing and Other Items"

    expense = models.CharField(max_length=64)
    family1 = models.IntegerField('1 Person', default=0, null=False)
    family2 = models.IntegerField('2 Persons', default=0, null=False)
    family3 = models.IntegerField('3 Persons', default=0, null=False)
    family4 = models.IntegerField('4 Persons', default=0, null=False)
    additional_person = models.IntegerField('Additional Person', default=0, null=False)

    def get_family_expense(self, family_size: int) -> int:
        family_size = int(family_size)
        if family_size == 1:
            return self.family1
        if family_size == 2:
            return self.family2
        if family_size == 3:
            return self.family3
        if family_size == 4:
            return self.family4
        return self.family4 + self.additional_person * (family_size - 4)

    class Meta:
        verbose_name = "National Standards: Food, Clothing and Other Items"
        verbose_name_plural = "National Standards: Food, Clothing and Other Items"

    def __str__(self):
        return "FoodClothingStandard for %s" % (self.expense)


class OutOfPocketHealthCare(models.Model):
    DOCUMENT_NAME = "National Standards: Out-of-Pocket Health Care"

    max_age = models.IntegerField()
    cost = models.IntegerField()

    class Meta:
        verbose_name = "National Standards: Out-of-Pocket Health Care"
        verbose_name_plural = "National Standards: Out-of-Pocket Health Care"

    def __str__(self):
        return "Out-of-Pocket Health Care for %s yrs and less" % (self.max_age)


class TransportationStandard(models.Model):
    DOCUMENT_NAME = "Allowable Living Expense Transportation Standards"

    tax_type = models.CharField(max_length=20, choices=TRANSPORTATION_TAX_TYPE, null=True, blank=True, default=None)
    county = models.OneToOneField(County, null=True)
    cost_car1 = models.IntegerField(default=0, null=False)
    cost_car2 = models.IntegerField(default=0, null=False)
    apply_by = models.CharField(max_length=10, choices=TRANSP_APPLY_BY, default='national', null=False)

    class Meta:
        verbose_name = "Allowable Living Expense Transportation Standards"
        verbose_name_plural = "Allowable Living Expense Transportation Standards"

    def __str__(self):
        county_name = "unknown"
        if self.county:
            county_name = "%s" % self.county
        return "TransportationStandard (%s) for %s" % (self.tax_type, county_name)


DOCUMENT_TYPES = (
    (HousingUtilitiesStandard.__name__, HousingUtilitiesStandard.DOCUMENT_NAME),
    (FoodClothingStandard.__name__, FoodClothingStandard.DOCUMENT_NAME),
    (OutOfPocketHealthCare.__name__, OutOfPocketHealthCare.DOCUMENT_NAME),
    (TransportationStandard.__name__, TransportationStandard.DOCUMENT_NAME),
)


def longlongago():
    return timezone.datetime(1970, 1, 1)


class DocumentStatus(models.Model):
    """ Store information about last updates of the documents """

    document_name = models.CharField(max_length=24, choices=DOCUMENT_TYPES, unique=True)
    success_time = models.DateTimeField("Time of last successful update", blank=True, default=longlongago)
    error_time = models.DateTimeField("Time of last error", blank=True, default=longlongago)
    lasterror = models.CharField(max_length=256, blank=True, default='')
    scheduled = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'DocumentStatuses'
        ordering = ('document_name', )
        # ordering = ('-success_time', '-error_time')

    def status(self):
        if self.error_time > self.success_time:
            return "error"
        return "success"

    def __str__(self):
        return "Document Status: %s" % self.get_document_name_display()
