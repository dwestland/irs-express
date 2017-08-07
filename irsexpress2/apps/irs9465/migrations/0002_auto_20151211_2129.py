# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irs9465', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f9465page3',
            name='account_number',
            field=models.CharField(blank=True, max_length=32, help_text='17 digits', default='', null=True),
        ),
        migrations.AlterField(
            model_name='f9465page3',
            name='routing_number',
            field=models.CharField(blank=True, max_length=32, help_text='9 digits', default='', null=True),
        ),
    ]
