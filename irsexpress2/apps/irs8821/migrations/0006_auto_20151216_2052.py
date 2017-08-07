# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irs8821', '0005_auto_20151215_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f8821page1',
            name='app_apt',
            field=models.CharField(blank=True, default='', verbose_name='Appointee Apt No', max_length=8),
        ),
        migrations.AlterField(
            model_name='f8821spousepage1',
            name='app_apt',
            field=models.CharField(blank=True, default='', verbose_name='Appointee Apt No', max_length=8),
        ),
    ]
