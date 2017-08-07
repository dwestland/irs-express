# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0002_remove_preparer_date'),
        ('irs8821', '0006_auto_20151216_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='f8821page1',
            name='app_addr_new',
        ),
        migrations.RemoveField(
            model_name='f8821page1',
            name='app_apt',
        ),
        migrations.RemoveField(
            model_name='f8821page1',
            name='app_caf',
        ),
        migrations.RemoveField(
            model_name='f8821page1',
            name='app_city',
        ),
        migrations.RemoveField(
            model_name='f8821page1',
            name='app_fax',
        ),
        migrations.RemoveField(
            model_name='f8821page1',
            name='app_fax_new',
        ),
        migrations.RemoveField(
            model_name='f8821page1',
            name='app_name',
        ),
        migrations.RemoveField(
            model_name='f8821page1',
            name='app_phone',
        ),
        migrations.RemoveField(
            model_name='f8821page1',
            name='app_phone_new',
        ),
        migrations.RemoveField(
            model_name='f8821page1',
            name='app_ptin',
        ),
        migrations.RemoveField(
            model_name='f8821page1',
            name='app_state_name',
        ),
        migrations.RemoveField(
            model_name='f8821page1',
            name='app_street',
        ),
        migrations.RemoveField(
            model_name='f8821page1',
            name='app_zipcode',
        ),
        migrations.RemoveField(
            model_name='f8821spousepage1',
            name='app_addr_new',
        ),
        migrations.RemoveField(
            model_name='f8821spousepage1',
            name='app_apt',
        ),
        migrations.RemoveField(
            model_name='f8821spousepage1',
            name='app_caf',
        ),
        migrations.RemoveField(
            model_name='f8821spousepage1',
            name='app_city',
        ),
        migrations.RemoveField(
            model_name='f8821spousepage1',
            name='app_fax',
        ),
        migrations.RemoveField(
            model_name='f8821spousepage1',
            name='app_fax_new',
        ),
        migrations.RemoveField(
            model_name='f8821spousepage1',
            name='app_name',
        ),
        migrations.RemoveField(
            model_name='f8821spousepage1',
            name='app_phone',
        ),
        migrations.RemoveField(
            model_name='f8821spousepage1',
            name='app_phone_new',
        ),
        migrations.RemoveField(
            model_name='f8821spousepage1',
            name='app_ptin',
        ),
        migrations.RemoveField(
            model_name='f8821spousepage1',
            name='app_state_name',
        ),
        migrations.RemoveField(
            model_name='f8821spousepage1',
            name='app_street',
        ),
        migrations.RemoveField(
            model_name='f8821spousepage1',
            name='app_zipcode',
        ),
        migrations.AddField(
            model_name='f8821page1',
            name='appointee',
            field=models.ForeignKey(to='agents.Appointee', verbose_name='Appointee', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='f8821spousepage1',
            name='appointee',
            field=models.ForeignKey(to='agents.Appointee', verbose_name='Appointee', blank=True, null=True),
        ),
    ]
