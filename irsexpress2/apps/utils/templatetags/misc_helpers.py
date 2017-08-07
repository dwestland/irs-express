# -*- coding: utf-8 -*-

import re

from django import template
from django.utils.encoding import force_text

register = template.Library()


@register.filter
def substr(arr, start=None, step=None, end=None):
    """ Extract string's substring """
    start = start or None
    step = step or None
    end = end or None
    return arr[start:step:end]


@register.filter
def intcomma_force(value):
    """ The same as django's intcomma, but not depending on locale """
    if not value:
        return value
    orig = force_text(value)
    new = re.sub("^(-?\d+)(\d{3})", '\g<1>,\g<2>', orig)
    if orig == new:
        return new
    else:
        return intcomma_force(new)


@register.filter
def getphonecode(phone):
    if not phone:
        return ''
    return phone.replace('-', '')[0:3]


@register.filter
def getphonemiddle(phone):
    if not phone:
        return ''
    return phone.replace('-', '')[3:6]


@register.filter
def getphonelast(phone):
    # returns only last group (4 digits)
    if not phone:
        return ''
    return phone.replace('-', '')[6:]


@register.filter
def getphoneremain(phone):
    # returns all except code
    if not phone:
        return ''
    return phone.replace('-', '')[3:]


@register.filter
def ssnpart(value, part):
    raw = value.replace('-', '')
    if raw:
        if part == 1:
            # returns first 3 digits of SSN
            return raw[0:3]
        if part == 2:
            # returns middle 2 digits of SSN
            return raw[3:5]
        if part == 3:
            # returns last 4 digits of SSN
            return raw[5:]
    return ''


@register.filter
def floatfract(value):
    if not value:
        return value
    sf = "%.2f" % value
    return sf.split('.')[1]


@register.filter
def getline(fulltext, prevlines):
    # prevlines: text "10:20" - offset:length
    if not fulltext:
        return ''
    offset, length = prevlines.split(':')
    return fulltext[int(offset):int(offset) + int(length)]
