from django.contrib import admin

from .models import Appointee, Preparer
# Register your models here.

admin.site.register((Appointee, Preparer))
