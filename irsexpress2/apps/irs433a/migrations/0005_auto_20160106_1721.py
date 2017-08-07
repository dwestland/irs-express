# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irs433a', '0004_auto_20151228_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsreceivableinfo',
            name='contract_number',
            field=models.CharField(default='', help_text='Invoice Number or Government Grant or Contract Number', null=True, max_length=64, blank=True),
        ),
        migrations.AlterField(
            model_name='accountsreceivableinfo',
            name='status',
            field=models.CharField(default='', help_text='e.g., age, factored, other', null=True, max_length=32, blank=True),
        ),
        migrations.AlterField(
            model_name='assettransferdetails',
            name='assetlist',
            field=models.CharField(default='', max_length=128, null=True, verbose_name='List Asset(s)', blank=True),
        ),
        migrations.AlterField(
            model_name='assettransferdetails',
            name='date',
            field=models.DateField(default=None, null=True, verbose_name='Date Transferred', blank=True),
        ),
        migrations.AlterField(
            model_name='assettransferdetails',
            name='recipient',
            field=models.CharField(default='', max_length=128, null=True, verbose_name='To Whom or Where was it Transferred', blank=True),
        ),
        migrations.AlterField(
            model_name='bankaccountinfo',
            name='account_number',
            field=models.CharField(default='', max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='bankaccountinfo',
            name='account_type',
            field=models.CharField(default='', max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='bankaccountinfo',
            name='bank_name',
            field=models.CharField(default='', max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='bankruptcyinfo',
            name='discharged',
            field=models.DateField(default=None, null=True, verbose_name='Date Discharged', blank=True),
        ),
        migrations.AlterField(
            model_name='bankruptcyinfo',
            name='dismissed',
            field=models.DateField(default=None, null=True, verbose_name='Date Dismissed', blank=True),
        ),
        migrations.AlterField(
            model_name='bankruptcyinfo',
            name='filed',
            field=models.DateField(default=None, null=True, verbose_name='Date Filed', blank=True),
        ),
        migrations.AlterField(
            model_name='bankruptcyinfo',
            name='location',
            field=models.CharField(default='', max_length=128, null=True, verbose_name='Location', blank=True),
        ),
        migrations.AlterField(
            model_name='bankruptcyinfo',
            name='petition_number',
            field=models.CharField(default='', max_length=16, null=True, verbose_name='Petition Number', blank=True),
        ),
        migrations.AlterField(
            model_name='beneficiaryinfo',
            name='name',
            field=models.CharField(default='', max_length=128, null=True, verbose_name='Name of the trust, estate, or policy', blank=True),
        ),
        migrations.AlterField(
            model_name='beneficiaryinfo',
            name='place',
            field=models.CharField(default='', max_length=128, null=True, verbose_name='Place where recorded', blank=True),
        ),
        migrations.AlterField(
            model_name='businessassetinfo',
            name='description',
            field=models.CharField(default='', max_length=128, null=True, verbose_name='Property Description', blank=True),
        ),
        migrations.AlterField(
            model_name='businessbankaccountinfo',
            name='account_number',
            field=models.CharField(default='', max_length=64, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='businessbankaccountinfo',
            name='account_type',
            field=models.CharField(default='', max_length=64, null=True, verbose_name='Type of Account', blank=True),
        ),
        migrations.AlterField(
            model_name='businessbankaccountinfo',
            name='bank_name',
            field=models.CharField(default='', max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='businesscreditcardinfo',
            name='bank_name',
            field=models.CharField(default='', max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='businesscreditcardinfo',
            name='credit_card',
            field=models.CharField(default='', max_length=64, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='clientdependent',
            name='age',
            field=models.PositiveIntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='clientdependent',
            name='relationship',
            field=models.CharField(default='', max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='creditinfo',
            name='account_number',
            field=models.CharField(default='', max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='creditinfo',
            name='name',
            field=models.CharField(default='', max_length=128, null=True, verbose_name='Name of Institution', blank=True),
        ),
        migrations.AlterField(
            model_name='employmentinfo',
            name='contact_at_work_allowed',
            field=models.BooleanField(default=False, verbose_name='Does employer allow contact at work?'),
        ),
        migrations.AlterField(
            model_name='employmentinfo',
            name='employer_name',
            field=models.CharField(default='', help_text='If your self employed and do not have a business name, write "self"', null=True, max_length=64, blank=True),
        ),
        migrations.AlterField(
            model_name='employmentinfo',
            name='occupation',
            field=models.CharField(default='', max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='f433apage4',
            name='bank_balance_date',
            field=models.DateField(default=None, help_text='This is the date you are preparing the form', null=True, verbose_name='Bank Account Balance As of', blank=True),
        ),
        migrations.AlterField(
            model_name='f433apage4',
            name='banking_additional_info',
            field=models.TextField(default='', help_text='If you have additional checking, online bank accounts, money market accounts, savings accounts, stored value cards (e.g., payroll cards, government benefit cards, etc.) List safe deposit boxes including location and contents, enter the information here', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='f433apage4',
            name='cc_amount_owed_date',
            field=models.DateField(default=None, null=True, verbose_name=' Amount Owed as of', blank=True),
        ),
        migrations.AlterField(
            model_name='f433apage4',
            name='cc_available_credit_date',
            field=models.DateField(default=None, help_text='The IRS trying to determine unused credit that you may still have access to. Generally this section applies to credit cards', null=True, verbose_name='Available Credit as of', blank=True),
        ),
        migrations.AlterField(
            model_name='f433apage4',
            name='credit_additional_info',
            field=models.TextField(default='', help_text='If you have additional credit available, enter the information here', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='f433apage4',
            name='insurance_additional_info',
            field=models.TextField(default='', help_text='If you have additional Life Insurance, enter the information here', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='f433apage4',
            name='investment_additional_info',
            field=models.TextField(default='', help_text='If you have additional investments, enter the information here', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='f433apage4',
            name='loan_balance_date',
            field=models.DateField(default=None, help_text='This is the date you are preparing the form', null=True, verbose_name='Loan Balance As of', blank=True),
        ),
        migrations.AlterField(
            model_name='f433apage6',
            name='other_1_name',
            field=models.CharField(default='', max_length=64, verbose_name='Other Income 1: Description', blank=True, help_text='Include agricultural subsidies, unemployment compensation, gambling income,\noil credits, rent subsidies, etc.', null=True),
        ),
        migrations.AlterField(
            model_name='f433apage6',
            name='other_2_name',
            field=models.CharField(default='', max_length=64, verbose_name='Other Income 2: Description', blank=True, help_text='Include agricultural subsidies, unemployment compensation, gambling income,\noil credits, rent subsidies, etc.', null=True),
        ),
        migrations.AlterField(
            model_name='f433apage6',
            name='taxes',
            field=models.PositiveIntegerField(default=0, help_text='Include state and Federal taxes withheld from salary or wages, or paid as estimated taxes.', verbose_name='Current year taxes (Income/FICA)', blank=True),
        ),
        migrations.AlterField(
            model_name='f433apage7',
            name='bank_balance_date',
            field=models.DateField(default=None, help_text='This is the date you are preparing the form', null=True, verbose_name='Bank Account Balance As of', blank=True),
        ),
        migrations.AlterField(
            model_name='f433apage7',
            name='business_name',
            field=models.CharField(default='', max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='f433apage7',
            name='business_type',
            field=models.CharField(default='', max_length=128, null=True, verbose_name='Type of Business', blank=True),
        ),
        migrations.AlterField(
            model_name='f433apage7',
            name='tax_deposit_freq',
            field=models.CharField(default='', max_length=64, null=True, verbose_name='Frequency of Tax Deposits', blank=True),
        ),
        migrations.AlterField(
            model_name='f433apage8',
            name='period_end',
            field=models.DateField(default=None, null=True, verbose_name='Income and Expenses period end date', blank=True),
        ),
        migrations.AlterField(
            model_name='f433apage8',
            name='period_start',
            field=models.DateField(default=None, null=True, verbose_name='Income and Expenses period start date', blank=True),
        ),
        migrations.AlterField(
            model_name='insuranceinfo',
            name='name',
            field=models.CharField(default='', max_length=128, null=True, verbose_name='Name', blank=True),
        ),
        migrations.AlterField(
            model_name='insuranceinfo',
            name='policy_number',
            field=models.CharField(default='', max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='insuranceinfo',
            name='policy_owner',
            field=models.CharField(default='', max_length=64, null=True, verbose_name='owner of the Policy', blank=True),
        ),
        migrations.AlterField(
            model_name='investmentinfo',
            name='full_name',
            field=models.CharField(default='', max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='investmentinfo',
            name='investment_type',
            field=models.CharField(default='', max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='lawsuitpartyinfo',
            name='case_number',
            field=models.CharField(default='', max_length=16, null=True, verbose_name='Case Number', blank=True),
        ),
        migrations.AlterField(
            model_name='lawsuitpartyinfo',
            name='completion_date',
            field=models.DateField(default=None, help_text='Sometimes, this information is not available or unknown at this time', null=True, verbose_name='Possible Completion Date', blank=True),
        ),
        migrations.AlterField(
            model_name='lawsuitpartyinfo',
            name='location',
            field=models.CharField(default='', max_length=128, null=True, verbose_name='Location of Filing', blank=True),
        ),
        migrations.AlterField(
            model_name='lawsuitpartyinfo',
            name='representer',
            field=models.CharField(default='', max_length=128, verbose_name='Represented by', blank=True, help_text='Who is the lawyer handling your law suit.', null=True),
        ),
        migrations.AlterField(
            model_name='lawsuitpartyinfo',
            name='subject',
            field=models.CharField(default='', max_length=256, verbose_name='Subject of Suit', blank=True, help_text='What is the cause of action? Ie. car accident, etc', null=True),
        ),
        migrations.AlterField(
            model_name='liveabroaddetails',
            name='date_from',
            field=models.DateField(default=None, null=True, verbose_name='From', blank=True),
        ),
        migrations.AlterField(
            model_name='liveabroaddetails',
            name='date_to',
            field=models.DateField(default=None, null=True, verbose_name='To', blank=True),
        ),
        migrations.AlterField(
            model_name='paymentprocessorinfo',
            name='account_number',
            field=models.CharField(default='', max_length=64, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='paymentprocessorinfo',
            name='name',
            field=models.CharField(default='', max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='personalassetinfo',
            name='description',
            field=models.CharField(default='', max_length=128, null=True, verbose_name='Property Description', blank=True),
        ),
        migrations.AlterField(
            model_name='realpropertyinfo',
            name='description',
            field=models.CharField(default='', max_length=128, null=True, verbose_name='Property Description', blank=True),
        ),
        migrations.AlterField(
            model_name='safedetails',
            name='contents',
            field=models.CharField(default='', max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='safedetails',
            name='location',
            field=models.CharField(default='', max_length=256, null=True, verbose_name='Location (Name, address and box number(s))', blank=True),
        ),
        migrations.AlterField(
            model_name='trusteedetails',
            name='name',
            field=models.CharField(default='', max_length=128, null=True, verbose_name='Name of the trust', blank=True),
        ),
        migrations.AlterField(
            model_name='vehicleinfo',
            name='make',
            field=models.CharField(default='', max_length=128, null=True, blank=True),
        ),
    ]
