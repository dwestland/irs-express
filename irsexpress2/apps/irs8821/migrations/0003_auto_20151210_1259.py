# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irs8821', '0002_auto_20151209_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='f8821page1',
            name='phone_ext',
            field=models.CharField(default='', max_length=7, verbose_name='Daytime telephone extension', blank=True),
        ),
        migrations.AddField(
            model_name='f8821spousepage1',
            name='phone_ext',
            field=models.CharField(default='', max_length=7, verbose_name='Daytime telephone extension', blank=True),
        ),
    ]
