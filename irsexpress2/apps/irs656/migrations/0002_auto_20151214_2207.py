# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irs656', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessTaxDebt',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('is_1120_incometax', models.BooleanField(default=False, verbose_name='1120 Income Tax', help_text='If you owe income taxes to the IRS, check the box and record every year in which you owe tax to the IRS.')),
                ('years_1120', models.CharField(default='', verbose_name='Year(s)', blank=True, null=True, max_length=128)),
                ('is_941_qtaxreturn_bus', models.BooleanField(default=False, verbose_name="941 Employer's Quarterly Federal Tax Return", help_text='If you have employees and are delinquent with your payroll tax, your problem may be complex and we recommend that you consult with our office or a tax professional. If you proceed with your offer, then be sure to record every quarter that you are delinquent with employment federal tax deposits.')),
                ('qtaxreturn_941_periods_bus', models.CharField(default='', verbose_name='Quarterly period(s)', blank=True, null=True, max_length=128)),
                ('is_940_afuta_bus', models.BooleanField(default=False, verbose_name="940 Employer's Annual Federal Unemployment (FUTA) Tax Return", help_text='If you have employees and are delinquent with your payroll tax, your problem may be complex and we recommend that you consult with our office or a tax professional. If you proceed with your offer, then be sure to record every quarter that you are delinquent with employment federal tax deposits.')),
                ('years_940_bus', models.CharField(default='', verbose_name='Years', blank=True, null=True, max_length=128)),
                ('is_other_taxes_bus', models.BooleanField(default=False, verbose_name='Other Federal Tax(es)', help_text='This is exceedingly rare and usually applies to individuals who owe excise taxes')),
                ('othertaxes_types_periods_bus', models.CharField(default='', verbose_name='Type(s) and Period(s)', blank=True, null=True, max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='f656page2',
            name='attachment_date',
            field=models.DateField(default=None, verbose_name='If you need more space, use attachment and title it "Attachment to Form 656 dated (this date)"', help_text='Make sure to sign and date the attachment', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='f656page2',
            name='is_1040_incometax',
            field=models.BooleanField(default=False, verbose_name='1040 Income Tax', help_text='Most likely you will be using this option. 95% of offers are for delinquent income tax. If you owe income taxes to the IRS, check the box and record every year in which you owe tax to the IRS.'),
        ),
        migrations.AddField(
            model_name='f656page2',
            name='is_940_afuta',
            field=models.BooleanField(default=False, verbose_name="940 Employer's Annual Federal Unemployment (FUTA) Tax Return", help_text='If you have employees and are delinquent with your payroll tax, your problem may be complex and we recommend that you consult with our office or a tax professional. If you proceed with your offer, then be sure to record every quarter that you are delinquent with employment federal tax deposits.'),
        ),
        migrations.AddField(
            model_name='f656page2',
            name='is_941_qtaxreturn',
            field=models.BooleanField(default=False, verbose_name="941 Employer's Quarterly Federal Tax Return", help_text='If you have employees and are delinquent with your payroll tax, your problem may be complex and we recommend that you consult with our office or a tax professional. If you proceed with your offer, then be sure to record every quarter that you are delinquent with employment federal tax deposits.'),
        ),
        migrations.AddField(
            model_name='f656page2',
            name='is_other_taxes',
            field=models.BooleanField(default=False, verbose_name='Other Federal Tax(es)', help_text='This is exceedingly rare and usually applies to individuals who owe excise taxes'),
        ),
        migrations.AddField(
            model_name='f656page2',
            name='is_trustfund_recovery_penalty',
            field=models.BooleanField(default=False, verbose_name='Trust Fund Recovery Penalty', help_text='This only applies if you had employees or were responsible for employee payroll in a business that you worked at. If you have had employees and failed to full pay your federal tax deposits, the IRS may have asserted a portion of that delinquency against you personally. If so, you need to include every quarter that the IRS asserted the Trust Fund Recovery Penalty against you. Each quarter you are responsible for is recorded on the tax lien that the IRS has previously sent you. If you do not have a copy of your tax lien, the IRS can provide each quarter you are responsible for by merely calling them at 1-800-829-1040.'),
        ),
        migrations.AddField(
            model_name='f656page2',
            name='othertaxes_types_periods',
            field=models.CharField(default='', verbose_name='Type(s) and Period(s)', blank=True, null=True, max_length=128),
        ),
        migrations.AddField(
            model_name='f656page2',
            name='qtaxreturn_941_periods',
            field=models.CharField(default='', verbose_name='Quarterly period(s)', blank=True, null=True, max_length=128),
        ),
        migrations.AddField(
            model_name='f656page2',
            name='trustfund_periods',
            field=models.CharField(max_length=128, verbose_name='For failure to pay withholding and Federal Insurance Contributions Act taxes (Social Security taxes), for period(s) ending', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='f656page2',
            name='trustfund_person',
            field=models.CharField(default='', help_text='enter corporation name', blank=True, null=True, max_length=128, verbose_name='As a responsible person of'),
        ),
        migrations.AddField(
            model_name='f656page2',
            name='years_1040',
            field=models.CharField(default='', verbose_name='Year(s)', blank=True, null=True, max_length=128),
        ),
        migrations.AddField(
            model_name='f656page2',
            name='years_940',
            field=models.CharField(default='', verbose_name='Years', blank=True, null=True, max_length=128),
        ),
        migrations.AddField(
            model_name='f656page2',
            name='businesstaxdebt',
            field=models.OneToOneField(to='irs656.BusinessTaxDebt', null=True, related_name='page'),
        ),
    ]
