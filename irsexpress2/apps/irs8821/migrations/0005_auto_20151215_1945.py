# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irs8821', '0004_auto_20151211_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f8821page1',
            name='app_caf',
            field=models.CharField(blank=True, verbose_name='Appointee CAF No', help_text='Nine-digits code', default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='f8821spousepage1',
            name='app_caf',
            field=models.CharField(blank=True, verbose_name='Appointee CAF No', help_text='Nine-digits code', default='', max_length=12),
        ),
    ]
