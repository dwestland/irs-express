# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import utils.widgets


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0002_remove_preparer_date'),
        ('irs656', '0005_auto_20151217_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='f656page7',
            name='allow_designee',
            field=models.BooleanField(default=False, verbose_name='Do you want to allow another person to discuss this offer with the IRS?'),
        ),
        migrations.AddField(
            model_name='f656page7',
            name='designee_name',
            field=models.CharField(null=True, default='', blank=True, max_length=64, verbose_name="Designee's name"),
        ),
        migrations.AddField(
            model_name='f656page7',
            name='designee_phone',
            field=utils.widgets.PhoneNumberField(default='', blank=True, max_length=20, verbose_name="Designee's phone"),
        ),
        migrations.AddField(
            model_name='f656page7',
            name='preparer',
            field=models.ForeignKey(blank=True, verbose_name='Paid Preparer', null=True, help_text='To add a Preparer - go to Management -> Preparers', to='agents.Preparer'),
        ),
        migrations.AddField(
            model_name='f656page7',
            name='preparer_date',
            field=models.DateField(null=True, blank=True, verbose_name='Paid Preparer Date'),
        ),
    ]
