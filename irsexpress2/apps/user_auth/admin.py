# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Account
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from registration.models import RegistrationProfile

admin.site.register(Account)
admin.site.unregister(Group)
admin.site.unregister(Site)
admin.site.unregister(RegistrationProfile)
