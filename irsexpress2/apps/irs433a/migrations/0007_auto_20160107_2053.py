# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irs433a', '0006_auto_20160106_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f433apage5',
            name='personal_assets_total_equity',
            field=models.IntegerField(help_text='Auto-calculated, correct the amounts from any attachments', verbose_name='Total Equity', default=0),
        ),
        migrations.AlterField(
            model_name='f433apage5',
            name='real_property_total_equity',
            field=models.IntegerField(help_text='Auto-calculated, correct the amounts from any attachments', verbose_name='Total Equity', default=0),
        ),
        migrations.AlterField(
            model_name='f433apage5',
            name='vehicles_total_equity',
            field=models.IntegerField(help_text='Auto-calculated, correct the amounts from any attachments', verbose_name='Total Equity', default=0),
        ),
    ]
