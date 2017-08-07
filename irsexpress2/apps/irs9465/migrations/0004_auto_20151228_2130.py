# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('irs9465', '0003_auto_20151221_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientspouse',
            name='ssn',
            field=localflavor.us.models.USSocialSecurityNumberField(null=True, verbose_name='Social Security Number on IRS Account', max_length=11, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='f9465page1',
            name='ssn',
            field=localflavor.us.models.USSocialSecurityNumberField(null=True, verbose_name='Social Security Number on IRS Account', max_length=11, blank=True, default=''),
        ),
    ]
