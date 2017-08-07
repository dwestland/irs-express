# -*- coding: utf-8 -*-

import logging

from repository.models import FoodClothingStandard, OutOfPocketHealthCare, TransportationStandard

logger = logging.getLogger(__name__)


def get_suggested_foodclothing(client):
    retval = {'name': 'food_clothing'}
    form = client.get_form_433a()
    if not hasattr(form, 'page1'):
        # on page1 we have information about family size
        return {}
    total_expense = FoodClothingStandard.objects.get(expense='Total')
    family_size = form.page1.get_family_size()
    retval['value'] = total_expense.get_family_expense(family_size)
    retval['desc'] = "Based on family size of %s" % family_size
    return retval


def get_suggested_oop_healthcare(client):
    retval = {'name': 'oop_healthcare'}
    form = client.get_form_433a()
    if not hasattr(form, 'page1'):
        # on page1 we have information about family ages
        return {}
    family_ages = form.page1.get_family_ages_list()
    oops = list(OutOfPocketHealthCare.objects.values_list('max_age', 'cost').order_by('max_age'))
    value = 0
    for age in family_ages:
        for max_age, cost in oops:
            if age < max_age:
                value += cost
                break
    retval['value'] = value
    retval['desc'] = "Based on family members with ages of %s years old" % \
        (", ".join((str(y) for y in sorted(family_ages))))
    return retval


def get_suggested_housing(client):
    retval = {'name': 'housing'}
    form = client.get_form_433a()
    if not hasattr(form, 'page1'):
        # on page1 we have information about family ages and county
        return {}
    family_size = form.page1.get_family_size()
    county = form.page1.county or client.county
    if not hasattr(county, 'housingutilitiesstandard'):
        logger.error("County %s has NO housingutilitiesstandard object!" % county)
        return {}
    retval['value'] = county.housingutilitiesstandard.get_family_expense(family_size)
    retval['desc'] = "Based on family size of %s and %s" % (family_size, county)
    return retval


def get_suggested_vehicle_oper(client):
    # we take the cost by counties
    retval = {'name': 'vehicle_oper'}
    form = client.get_form_433a()
    if not hasattr(form, 'page5'):
        # on page5 we have information about owed cars
        return {}
    county = client.county
    if hasattr(form, 'page1'):
        county = form.page1.county
    if not county:
        return {}
    value = 0
    cars_count = form.page5.get_vehicles_count()
    if cars_count > 0:
        if not hasattr(county, 'transportationstandard'):
            logger.error("County %s has NO transportationstandard object!" % county)
        elif county.transportationstandard.tax_type != 'operating':
            logger.error("County %s has transportationstandard object of type '%s' instead of 'operating'!" %
                         (county, county.transportationstandard.tax_type))
        else:
            if cars_count == 1:
                value = county.transportationstandard.cost_car1
            elif cars_count > 1:
                value = county.transportationstandard.cost_car2
        if value == 0:
            return {}
    retval['value'] = value
    retval['desc'] = "Based on %s cars and %s" % (cars_count, county)
    return retval


def get_suggested_vehicle_own(client):
    # we assume that ownership cost is only national-wide
    retval = {'name': 'vehicle_own'}
    form = client.get_form_433a()
    if not hasattr(form, 'page5'):
        # on page5 we have information about owed cars
        return {}
    cars_count = form.page5.get_vehicles_count()
    value = 0
    if cars_count > 0:
        ts_qs = TransportationStandard.objects.filter(tax_type='ownership')
        if ts_qs.count() == 0:
            return {}
        if cars_count == 1:
            value = ts_qs[0].cost_car1
        elif cars_count > 1:
            value = ts_qs[0].cost_car2
    retval['value'] = value
    retval['desc'] = "Based on information about %s cars" % (cars_count)
    return retval


def get_suggested_pub_transport(client):
    retval = {'name': 'pub_transport'}
    ts_qs = TransportationStandard.objects.filter(tax_type='publictrans')
    if ts_qs.count() == 0:
        return {}
    value = ts_qs[0].cost_car1
    retval['value'] = value
    retval['desc'] = "National Standard"
    return retval
