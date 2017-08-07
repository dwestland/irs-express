# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irs9465', '0004_auto_20151228_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f9465page1',
            name='county',
            field=models.ForeignKey(to='repository.County', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='f9465page1',
            name='request_for_years',
            field=models.CharField(verbose_name='What tax year(s) is this Installment Arrangement for', null=True, max_length=128, default=None, blank=True, help_text='For example, 2014 and 2015'),
        ),
        migrations.AlterField(
            model_name='f9465page4',
            name='county',
            field=models.ForeignKey(verbose_name='Your primary county', null=True, to='repository.County', blank=True),
        ),
    ]
