# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('irs433a', '0003_auto_20151216_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiaryinfo',
            name='amount',
            field=models.PositiveIntegerField(default=0, verbose_name='Anticipated amount to be received'),
        ),
        migrations.AlterField(
            model_name='beneficiaryinfo',
            name='ein',
            field=models.CharField(null=True, verbose_name='Employer Identification Number (EIN)', max_length=32, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='beneficiaryinfo',
            name='whenreceive',
            field=models.DateField(null=True, verbose_name='When will the amount be received', blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='businessassetinfo',
            name='purchase_date',
            field=models.DateField(null=True, verbose_name='Purchase Lease Date', blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='clientspouse',
            name='birthdate',
            field=models.DateField(null=True, verbose_name='Spouse Birth Date', blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='clientspouse',
            name='ssn',
            field=localflavor.us.models.USSocialSecurityNumberField(null=True, verbose_name='Social Security Number on IRS Account', max_length=11, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='employmentinfo',
            name='long_work_month',
            field=models.PositiveIntegerField(default=0, verbose_name='How long with this employer (Months)'),
        ),
        migrations.AlterField(
            model_name='employmentinfo',
            name='long_work_years',
            field=models.PositiveIntegerField(default=0, verbose_name='How long with this employer (Years)'),
        ),
        migrations.AlterField(
            model_name='employmentinfo',
            name='w4extemptions',
            field=models.PositiveIntegerField(null=True, verbose_name='Number of exemptions claimed on Form W-4', default=0, help_text='This is only if you are a w-2 wage earner and do not receive a "1099".'),
        ),
        migrations.AlterField(
            model_name='f433apage1',
            name='birthdate',
            field=models.DateField(null=True, blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='f433apage1',
            name='county',
            field=models.ForeignKey(null=True, blank=True, to='repository.County'),
        ),
        migrations.AlterField(
            model_name='f433apage1',
            name='ssn',
            field=localflavor.us.models.USSocialSecurityNumberField(null=True, verbose_name='Social Security Number on IRS Account', max_length=11, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='personalassetinfo',
            name='purchase_date',
            field=models.DateField(null=True, verbose_name='Purchase Lease Date', blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='realpropertyinfo',
            name='purchase_date',
            field=models.DateField(null=True, verbose_name='Purchase Lease Date', blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='vehicleinfo',
            name='license_number',
            field=models.CharField(null=True, verbose_name='License/Tag Number', max_length=32, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='vehicleinfo',
            name='model',
            field=models.CharField(null=True, blank=True, max_length=128, default=''),
        ),
        migrations.AlterField(
            model_name='vehicleinfo',
            name='purchase_date',
            field=models.DateField(null=True, verbose_name='Purchase Lease Date', blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='vehicleinfo',
            name='vin',
            field=models.CharField(null=True, verbose_name='Vehicle Identification Number', max_length=32, blank=True, default=''),
        ),
    ]
