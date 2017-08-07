# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import utils.widgets


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone_cell',
            field=utils.widgets.PhoneNumberField(blank=True, default='', max_length=20, verbose_name='Cell Phone'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_home',
            field=utils.widgets.PhoneNumberField(blank=True, default='', max_length=20, verbose_name='Home Phone'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_work',
            field=utils.widgets.PhoneNumberField(blank=True, default='', max_length=20, verbose_name='Work Phone'),
        ),
    ]
