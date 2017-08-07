# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irs433a', '0005_auto_20160106_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsreceivableinfo',
            name='date_due',
            field=models.DateField(null=True, default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='businessassetinfo',
            name='location_county',
            field=models.ForeignKey(to='repository.County', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='lawsuitpartyinfo',
            name='amount',
            field=models.PositiveIntegerField(help_text='Many times there is no "demanded" amount. If that is the case, place 0 here', default=0, verbose_name='Amount of Suit'),
        ),
        migrations.AlterField(
            model_name='personalassetinfo',
            name='location_county',
            field=models.ForeignKey(to='repository.County', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='realpropertyinfo',
            name='location_county',
            field=models.ForeignKey(to='repository.County', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='vehicleinfo',
            name='year',
            field=models.PositiveIntegerField(default=1999),
        ),
    ]
