# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irs8821', '0007_auto_20151218_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f8821page1',
            name='ssn',
            field=models.CharField(null=True, verbose_name='Taxpayer identification number(s)', max_length=128, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='f8821spousepage1',
            name='ssn',
            field=models.CharField(null=True, verbose_name='Taxpayer identification number(s)', max_length=128, blank=True, default=''),
        ),
    ]
