# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irs656', '0006_auto_20151218_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f656page7',
            name='preparer_date',
            field=models.DateField(verbose_name='Paid Preparer Sign Date', null=True, blank=True),
        ),
    ]
