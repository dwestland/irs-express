# -*- coding: utf-8 -*-

import os
import uuid
import mimetypes
import datetime

from django.db import models
from django.conf import settings
from django.utils import timezone

from repository.const import US_STATES, STATES_EXTENDED, CLIENT_STATUS
from repository.models import County

from utils.widgets import PhoneNumberField
from irs433a.models import Form433a
from irs656.models import Form656
from irs8821.models import Form8821, Form8821Spouse
from irs9465.models import Form9465


PHONE_TYPES = (
    ('home', 'home'),
    ('cell', 'cell'),
    ('work', 'work')
)

CLIENT_STAGES = {
    1: {'days': 2, 'name': 'Sign up Client'},
    2: {'days': 5, 'name': 'Request Records from IRS and Start entering Data into the 433'},
    3: {'days': 5, 'name': 'Get Preliminary Information and Email Client Questionnaire'},
    4: {'days': 5, 'name': 'Start Assembling 433 and Create List of Additional Information'},
    5: {'days': 4, 'name': 'Client Conference to Finalize 433'},
    6: {'days': 4, 'name': 'Assemble all documents and create 656 or 9465'},
    7: {'days': 4, 'name': 'Send Documents and Instructions to Client'},
    8: {'days': 0, 'name': 'Follow up with Closing Phone Call to Client'},
}
CLIENT_STAGES_CHOICES = ((s, stage['name']) for s, stage in CLIENT_STAGES.items())


class Client(models.Model):
    MAX_STAGE = max(CLIENT_STAGES.keys())

    first_name = models.CharField(max_length=32, null=False)
    middle_name = models.CharField(max_length=32, null=True, blank=True, default='')
    last_name = models.CharField(max_length=32, null=False)
    email = models.EmailField(max_length=128, null=True, blank=True, default='')
    phone_home = PhoneNumberField('Home Phone', max_length=20, null=False, blank=True, default='')
    phone_cell = PhoneNumberField('Cell Phone', max_length=20, null=False, blank=True, default='')
    phone_work = PhoneNumberField('Work Phone', max_length=20, null=False, blank=True, default='')
    primary_phone_type = models.CharField(max_length=5, choices=PHONE_TYPES, default='home')
    apt = models.CharField('Apt No', max_length=8, null=False, blank=True, default='')
    street = models.CharField(max_length=128, null=False, blank=True, default='')
    city = models.CharField(max_length=64, null=False, blank=True, default='')
    county = models.ForeignKey(County, null=True, blank=True)
    state_name = models.CharField('State', choices=STATES_EXTENDED, max_length=64, null=False, blank=True, default='')
    zipcode = models.CharField('Zip', max_length=10, null=False, blank=True, default='')

    taxyearsmissing = models.CharField('Years Missing Tax Return', max_length=100,
                                       null=False, blank=True, default='')
    stage = models.IntegerField(default=1, blank=True)
    stage_change_date = models.DateField(auto_now_add=True, editable=True)
    status = models.CharField(max_length=10, choices=CLIENT_STATUS, default='active', blank=True)
    summary = models.TextField(blank=True, null=False, default='')
    case_opened = models.DateField(auto_now_add=True, editable=True)

    def title(self):
        return "{0} {1}".format(self.first_name, self.last_name).title()

    def address(self):
        addr = [self.apt, self.street, self.city, self.state_name, self.zipcode, self.county]
        return ', '.join(str(v) for v in addr if v)

    def stage_title(self):
        return CLIENT_STAGES.get(self.stage, {}).get('name', 'Unknown')

    def get_taxreturn_years_list(self):
        return sorted(self.taxyearsmissing.split(','))

    def is_stage_correct(self, stage):
        if 1 <= stage <= self.MAX_STAGE:
            return True
        return False

    def get_new_stage(self, modifier):
        new_stage = self.stage + modifier
        if self.is_stage_correct(new_stage):
            return new_stage
        return self.stage

    def set_stage(self, new_stage, user_id, save=True):
        self.stage = new_stage
        self.add_note("Move client to the stage %s" % new_stage, user_id)
        self.stage_change_date = timezone.now()
        if save:
            self.save()

    def __str__(self):
        return "Client <%s>" % (self.title())

    def past_due(self):
        if not hasattr(self, '_pastdue'):
            changed_ago = (datetime.date.today() - self.stage_change_date).days
            self._pastdue = changed_ago - CLIENT_STAGES[self.stage]['days']
        return self._pastdue

    def case_days(self):
        # days since signup
        return (datetime.date.today() - self.case_opened).days

    def add_note(self, text: str, author_id: int):
        self.notes.create(author_id=author_id, text=text, date=timezone.now())

    def get_form_433a(self, create=True):
        if not hasattr(self, 'form433a'):
            if not create:
                return None
            self.form433a = Form433a.objects.create(client_id=self.id)
        return self.form433a

    def get_form_656(self, create=True):
        if not hasattr(self, 'form656'):
            if not create:
                return None
            self.form656 = Form656.objects.create(client_id=self.id)
        return self.form656

    def get_form_8821(self, create=True):
        if not hasattr(self, 'form8821'):
            if not create:
                return None
            self.form8821 = Form8821.objects.create(client_id=self.id)
        return self.form8821

    def get_form_8821spouse(self, create=True):
        if not hasattr(self, 'form8821spouse'):
            if not create:
                return None
            self.form8821spouse = Form8821Spouse.objects.create(client_id=self.id)
        return self.form8821spouse

    def get_form_9465(self, create=True):
        if not hasattr(self, 'form9465'):
            if not create:
                return None
            self.form9465 = Form9465.objects.create(client_id=self.id)
        return self.form9465


class ClientNote(models.Model):
    client = models.ForeignKey(Client, related_name="notes", related_query_name="note")
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    date = models.DateTimeField()
    text = models.TextField(blank=True, null=False, default='')

    class Meta:
        ordering = ('-date', )

    def __str__(self):
        return "Note for %s by %s" % (self.client, self.author)

    def can_be_edited(self, user):
        if user.is_admin or self.author == user:
            return True
        return False


def get_clientdoc_path(instance, filename):
    ext = filename.split('.')[-1]
    pathtpl = 'clientdocs/{uuid}-{client_id}-{filename}'
    return pathtpl.format(uuid=uuid.uuid4().hex, client_id=instance.client.pk,
                          filename=filename, ext=ext)


class ClientDocument(models.Model):
    uuid = models.CharField(max_length=32, blank=False, null=False)
    client = models.ForeignKey(Client, related_name="documents", related_query_name="document")
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    upload_date = models.DateTimeField(auto_now_add=True)
    file_name = models.CharField(max_length=64, blank=False, null=False)
    title = models.CharField(max_length=128, blank=False, null=False)

    document = models.FileField(upload_to=get_clientdoc_path)

    class Meta:
        ordering = ('-upload_date', 'file_name', )

    def mime_type(self):
        ext = self.file_name.split('.')[-1]
        return mimetypes.types_map.get(".%s" % ext) or "application/octet-stream"

    def get_filename(self):
        return "%s - %s" % (self.client.title(), self.file_name)

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid4().hex
        if not self.file_name:
            self.file_name = self.document.name
        self.upload_date = timezone.now()
        super().save(*args, **kwargs)
        # delete document in some time
        if settings.DOCUMENT_LIFE_TIME:
            from .tasks import delete_document
            delete_document.apply_async(countdown=settings.DOCUMENT_LIFE_TIME, kwargs={'document_id': self.id})

    def expire_in(self):
        exptime = (timezone.now() - self.upload_date).seconds
        if settings.DOCUMENT_LIFE_TIME and exptime < settings.DOCUMENT_LIFE_TIME:
            return "%s sec" % exptime
        return "Never"

    def delete(self, *args, **kwargs):
        try:
            self.document.delete()
        except Exception as ee:
            print("Exception on deleting document %s" % self.id)
        super().delete(*args, **kwargs)

    def __str__(self):
        return "Document '%s' of %s" % (self.title, self.client)
