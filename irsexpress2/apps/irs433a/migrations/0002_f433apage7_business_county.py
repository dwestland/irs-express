# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0001_initial'),
        ('irs433a', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='f433apage7',
            name='business_county',
            field=models.ForeignKey(null=True, to='repository.County'),
        ),
    ]
