# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irs656', '0008_auto_20151228_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessinformation',
            name='name',
            field=models.CharField(max_length=128, default='', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='f656page1',
            name='county',
            field=models.ForeignKey(to='repository.County', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mailingaddress',
            name='county',
            field=models.ForeignKey(to='repository.County', null=True, blank=True),
        ),
    ]
