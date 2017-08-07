# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irs433a', '0002_f433apage7_business_county'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='f433apage7',
            name='business_county',
        ),
        migrations.AlterField(
            model_name='f433apage7',
            name='average_gross_monthly_payroll',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='f433apage7',
            name='business_web',
            field=models.CharField(blank=True, null=True, default='', verbose_name='Business Website', max_length=256),
        ),
    ]
