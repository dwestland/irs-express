# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irs9465', '0002_auto_20151211_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f9465page4',
            name='married',
            field=models.BooleanField(verbose_name='Marital Status'),
        ),
    ]
