# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irs8821', '0008_auto_20151228_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f8821page1',
            name='county',
            field=models.ForeignKey(default=None, blank=True, null=True, to='repository.County'),
        ),
        migrations.AlterField(
            model_name='f8821spousepage1',
            name='county',
            field=models.ForeignKey(default=None, blank=True, null=True, to='repository.County'),
        ),
        migrations.AlterField(
            model_name='taxinformation',
            name='details',
            field=models.CharField(default='', max_length=128, null=True, verbose_name='Specific Tax Matters', blank=True),
        ),
        migrations.AlterField(
            model_name='taxinformation',
            name='tax_form_number',
            field=models.CharField(default='', help_text='1040, 941, 720, etc.', null=True, max_length=16, blank=True),
        ),
        migrations.AlterField(
            model_name='taxinformation',
            name='tax_information_type',
            field=models.CharField(default='', help_text='(Income, Employment, Payroll, Excise, Estate, Gift, Civil Penalty, Sec. 4980H Payments, etc.', null=True, max_length=32, blank=True),
        ),
        migrations.AlterField(
            model_name='taxinformation',
            name='years',
            field=models.CharField(default='', max_length=128, null=True, verbose_name='Year(s) or Period(s)', blank=True),
        ),
        migrations.AlterField(
            model_name='taxinformationspouse',
            name='details',
            field=models.CharField(default='', max_length=128, null=True, verbose_name='Specific Tax Matters', blank=True),
        ),
        migrations.AlterField(
            model_name='taxinformationspouse',
            name='tax_form_number',
            field=models.CharField(default='', help_text='1040, 941, 720, etc.', null=True, max_length=16, blank=True),
        ),
        migrations.AlterField(
            model_name='taxinformationspouse',
            name='tax_information_type',
            field=models.CharField(default='', help_text='(Income, Employment, Payroll, Excise, Estate, Gift, Civil Penalty, Sec. 4980H Payments, etc.', null=True, max_length=32, blank=True),
        ),
        migrations.AlterField(
            model_name='taxinformationspouse',
            name='years',
            field=models.CharField(default='', max_length=128, null=True, verbose_name='Year(s) or Period(s)', blank=True),
        ),
    ]
