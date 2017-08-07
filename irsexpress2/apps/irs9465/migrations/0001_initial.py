# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import utils.widgets
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientSpouse',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('first_name', models.CharField(max_length=32, verbose_name='Spouse First Name')),
                ('middle_name', models.CharField(blank=True, max_length=32, verbose_name='Spouse Middle Name', default='')),
                ('last_name', models.CharField(max_length=32, verbose_name='Spouse Last Name')),
                ('ssn', localflavor.us.models.USSocialSecurityNumberField(max_length=11, verbose_name='Social Security Number on IRS Account')),
            ],
        ),
        migrations.CreateModel(
            name='F9465Page1',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('request_for_form', models.CharField(max_length=128, verbose_name='This request is for Form(s)', help_text='for example, Form 1040 or Form 941')),
                ('request_for_years', models.CharField(max_length=128, verbose_name='What tax year(s) is this Installment Arrangement for', help_text='For example, 2014 and 2015')),
                ('first_name', models.CharField(max_length=32)),
                ('middle_name', models.CharField(blank=True, max_length=32, default='')),
                ('last_name', models.CharField(max_length=32)),
                ('ssn', localflavor.us.models.USSocialSecurityNumberField(max_length=11, verbose_name='Social Security Number on IRS Account')),
                ('street', models.CharField(blank=True, max_length=128, default='')),
                ('apt', models.CharField(blank=True, max_length=8, default='')),
                ('city', models.CharField(blank=True, max_length=64, default='')),
                ('state_name', models.CharField(blank=True, max_length=64, verbose_name='State', choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('PUER', 'Puerto Rico')], default='')),
                ('zipcode', models.CharField(blank=True, max_length=10, verbose_name='Zip', default='')),
                ('country', models.CharField(null=True, max_length=32, default='', verbose_name='Foreign Country', blank=True)),
                ('foreign_county', models.CharField(null=True, max_length=32, default='', verbose_name='Foreign province/state/county', blank=True)),
                ('foreign_zip', models.CharField(null=True, max_length=8, default='', verbose_name='Foreign postal code', blank=True)),
                ('address_new', models.BooleanField(verbose_name='Is this address new since you filed your last tax return?', default=False)),
                ('county', models.ForeignKey(to='repository.County')),
            ],
        ),
        migrations.CreateModel(
            name='F9465Page2',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('business_name', models.CharField(blank=True, max_length=128, default='', verbose_name='Name of your business', help_text='Must be no longer operating')),
                ('ein', models.CharField(null=True, max_length=32, default='', verbose_name='Employer Identification Number', blank=True)),
                ('phone_home', utils.widgets.PhoneNumberField(blank=True, max_length=20, verbose_name='Home Phone', default='')),
                ('phone_home_bttc', models.CharField(blank=True, max_length=32, verbose_name='Home: Best Time to Call', default='')),
                ('phone_work', utils.widgets.PhoneNumberField(blank=True, max_length=20, verbose_name='Work Phone', default='')),
                ('phone_work_ext', models.CharField(blank=True, max_length=6, verbose_name='Work Phone Ext', default='')),
                ('phone_work_bttc', models.CharField(blank=True, max_length=32, verbose_name='Work: Best Time to Call', default='')),
                ('employer_name', models.CharField(null=True, max_length=64, default='', blank=True)),
                ('employer_street', models.CharField(blank=True, max_length=128, verbose_name='Employer Address', default='')),
                ('employer_city', models.CharField(blank=True, max_length=64, default='')),
                ('employer_state_name', models.CharField(blank=True, max_length=64, verbose_name='Employer State', choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('PUER', 'Puerto Rico')], default='')),
                ('employer_zipcode', models.CharField(blank=True, max_length=10, verbose_name='Employer Zip', default='')),
                ('bank_name', models.CharField(blank=True, max_length=128, verbose_name='Name of your bank or other financial institution', default='')),
                ('bank_street', models.CharField(blank=True, max_length=128, default='')),
                ('bank_city', models.CharField(blank=True, max_length=64, default='')),
                ('bank_state_name', models.CharField(blank=True, max_length=64, verbose_name='Bank State', choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('PUER', 'Puerto Rico')], default='')),
                ('bank_zipcode', models.CharField(blank=True, max_length=10, verbose_name='Bank Zip', default='')),
            ],
        ),
        migrations.CreateModel(
            name='F9465Page3',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('amount_owed', models.FloatField(help_text='as shown on your tax return(s) (or notice(s))', verbose_name='Total amount you owe', default=0)),
                ('amount_paid', models.FloatField(help_text='Enter the amount of any payment you are making with your tax return(s) (or notice(s)).', verbose_name='Payment Amount', default=0)),
                ('can_pay', models.FloatField(help_text='Make your payments as large as possible to limit interest and penalty charges. The charges will continue until you pay in full. If no payment amount is listed here, a payment will be determined for you by dividing the balance due by 72 months', verbose_name='Amount you can pay each month', default=0)),
                ('payment_day', models.CharField(max_length=3, verbose_name='Day you want to make your payment each month', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26')])),
                ('routing_number', models.CharField(null=True, max_length=32, default='', blank=True)),
                ('account_number', models.CharField(null=True, max_length=32, default='', blank=True)),
                ('pay_payroll', models.BooleanField(help_text='Attach a completed Form 2159, Payroll Deduction Agreement', verbose_name='Do you want to make your payments by payroll deduction?')),
            ],
        ),
        migrations.CreateModel(
            name='F9465Page4',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('married', models.BooleanField(verbose_name='Martial Status')),
                ('expenses_shared', models.BooleanField(verbose_name='Do you share household expenses with your spouse?')),
                ('dependents_cnt', models.PositiveIntegerField(blank=True, verbose_name="How many dependents will you be able to claim on this year's tax return?", default=0)),
                ('has_older65', models.PositiveIntegerField(blank=True, verbose_name='How many people in your household are 65 or older?', default=0)),
                ('pay_period', models.CharField(max_length=16, verbose_name='How often are you paid?', choices=[('weekly', 'Weekly'), ('monthly', 'Monthly'), ('bi-weekly', 'Bi-Weekly'), ('twice-a-month', 'Twice a Month')], help_text='Indicate if you get paid weekly, biweekly or monthly.')),
                ('net_income_day', models.FloatField(help_text='Take home pay', verbose_name='Net income per pay period', default=0)),
                ('spouse_pay_period', models.CharField(null=True, max_length=16, verbose_name='How often is your spouse paid?', choices=[('weekly', 'Weekly'), ('monthly', 'Monthly'), ('bi-weekly', 'Bi-Weekly'), ('twice-a-month', 'Twice a Month')], blank=True)),
                ('spouse_net_income_day', models.FloatField(help_text='Take home pay', verbose_name="Spouse's Net income per pay period", default=0)),
                ('vehicles', models.PositiveIntegerField(verbose_name='How many vehicles do you own?', default=0)),
                ('car_payments', models.PositiveIntegerField(verbose_name='How many car payments do you have each month?', default=0)),
                ('has_health_insurance', models.BooleanField(verbose_name='Do you have health insurance?')),
                ('premiums_deducted', models.BooleanField(verbose_name='Are your premiums deducted from your paycheck?')),
                ('premiums', models.FloatField(verbose_name='How much are your monthly premiums?', default=0)),
                ('has_court_payments', models.BooleanField(verbose_name='Do you make court-ordered payments?')),
                ('court_payments_deducted', models.BooleanField(verbose_name='Are your court-ordered payments deducted from your paycheck?')),
                ('court_payments', models.FloatField(verbose_name='How much are your court-ordered payments each month?', default=0)),
                ('child_care', models.FloatField(verbose_name='Not including any court-ordered payments for child and dependent support, how much do you pay for child or dependent care each month?', default=0)),
                ('county', models.ForeignKey(verbose_name='Your primary county', to='repository.County')),
            ],
        ),
        migrations.CreateModel(
            name='Form9465',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('client', models.OneToOneField(related_name='form9465', to='clients.Client')),
            ],
        ),
        migrations.AddField(
            model_name='f9465page4',
            name='form',
            field=models.OneToOneField(related_name='page4', to='irs9465.Form9465'),
        ),
        migrations.AddField(
            model_name='f9465page3',
            name='form',
            field=models.OneToOneField(related_name='page3', to='irs9465.Form9465'),
        ),
        migrations.AddField(
            model_name='f9465page2',
            name='form',
            field=models.OneToOneField(related_name='page2', to='irs9465.Form9465'),
        ),
        migrations.AddField(
            model_name='f9465page1',
            name='form',
            field=models.OneToOneField(related_name='page1', to='irs9465.Form9465'),
        ),
        migrations.AddField(
            model_name='f9465page1',
            name='jointoffer',
            field=models.OneToOneField(null=True, to='irs9465.ClientSpouse', related_name='page'),
        ),
    ]
