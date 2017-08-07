
from django import template

register = template.Library()


@register.filter
def can_edit(obj, user):
    if not obj or not user:
        return False
    return obj.can_be_edited(user)
