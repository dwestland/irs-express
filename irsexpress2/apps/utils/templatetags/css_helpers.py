
from django import template

register = template.Library()


@register.filter
def commajoin(lll):
    return ", ".join(lll)


@register.filter
def yamlescape(value):
    # escape value to be used in YAML
    newvalue = value.replace("'", "\\'")
    return newvalue
