# -*- coding: utf-8 -*-

import logging

from django import forms
from django.utils import timezone

from utils.forms import ImprovedForm

from .models import Client, ClientNote, ClientDocument


class ClientEditForm(ImprovedForm, forms.ModelForm):

    class Meta:
        model = Client
        exclude = ('summary', 'taxyearsmissing', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        yvals = [''] * 10
        if self.instance.pk:
            yvals = self.instance.get_taxreturn_years_list()
        max_year = timezone.now().year
        for rym in range(10):
            yval = ""
            if len(yvals) > rym:
                yval = yvals[rym]
            self.fields['taxmiss_y%s' % rym] = forms.IntegerField(required=False, initial=yval,
                                                                  min_value=1950, max_value=max_year)
        self.reinit_widgets()
        for rym in range(10):
            self.fields['taxmiss_y%s' % rym].widget.unset_class('number-field')

    def save(self):
        yearsmissing = []
        for rym in range(10):
            year = self.cleaned_data.get('taxmiss_y%s' % rym)
            if year:
                yearsmissing.append(str(year))
        self.instance.stage = self.instance.stage or 1
        self.instance.status = self.instance.status or 'active'
        self.instance.taxyearsmissing = ",".join(set(yearsmissing))
        super().save()
        return self.instance


class ClientNoteEditForm(ImprovedForm, forms.ModelForm):

    class Meta:
        model = ClientNote
        exclude = ('client', 'author', 'date')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.client_id = kwargs.pop('client_id')
        super().__init__(*args, **kwargs)

    def save(self):
        self.instance.author = self.user
        self.instance.client_id = self.client_id
        self.instance.date = timezone.now()
        super().save()


class ClientDocumentUploadForm(ImprovedForm, forms.ModelForm):

    class Meta:
        model = ClientDocument
        exclude = ('uuid', 'client', 'author', 'upload_date', 'file_name')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.client_id = kwargs.pop('client_id')
        super().__init__(*args, **kwargs)

    def save(self):
        self.instance.author = self.user
        self.instance.client_id = self.client_id
        self.instance.upload_date = timezone.now()
        super().save()
