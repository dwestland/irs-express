# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irs8821', '0003_auto_20151210_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f8821page1',
            name='app_ptin',
            field=models.CharField(max_length=10, blank=True, verbose_name='Appointee PTIN', help_text='Eight-digits code', default=''),
        ),
        migrations.AlterField(
            model_name='f8821spousepage1',
            name='app_ptin',
            field=models.CharField(max_length=10, blank=True, verbose_name='Appointee PTIN', help_text='Eight-digits code', default=''),
        ),
    ]
