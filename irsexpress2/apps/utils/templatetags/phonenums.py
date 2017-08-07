
from django import template

import phonenumbers

register = template.Library()


@register.filter
def phonenum(raw_num):
    try:
        obj = phonenumbers.parse(raw_num, 'US')
        retval = phonenumbers.format_number(obj, phonenumbers.PhoneNumberFormat.NATIONAL)
        return retval
    except:
        return raw_num
