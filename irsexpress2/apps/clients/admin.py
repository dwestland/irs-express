from django.contrib import admin

from .models import Client, ClientNote, ClientDocument
# Register your models here.

admin.site.register((Client, ClientNote, ClientDocument))
