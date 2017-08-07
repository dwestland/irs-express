# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import utils.widgets


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0001_initial'),
        ('clients', '0001_initial'),
        ('irs8821', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='F8821SpousePage1',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=32)),
                ('middle_name', models.CharField(default='', max_length=32, blank=True)),
                ('last_name', models.CharField(default='', max_length=32)),
                ('apt', models.CharField(default='', max_length=8, blank=True)),
                ('street', models.CharField(default='', max_length=128, blank=True)),
                ('city', models.CharField(default='', max_length=64, blank=True)),
                ('state_name', models.CharField(default='', choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('PUER', 'Puerto Rico')], max_length=64, blank=True, verbose_name='State')),
                ('zipcode', models.CharField(default='', max_length=10, blank=True, verbose_name='Zip')),
                ('phone', utils.widgets.PhoneNumberField(default='', max_length=20, blank=True, verbose_name='Daytime telephone number')),
                ('ssn', models.CharField(default='', max_length=128, verbose_name='Taxpayer identification number(s)')),
                ('plan_number', models.CharField(help_text='If applicable', default='', max_length=64, blank=True)),
                ('additional_appointees', models.BooleanField(help_text='If you wish to name more than one appointee, attach a list to this form', default=False, verbose_name='Would you like to name more than one appointee?')),
                ('app_name', models.CharField(default='', max_length=128, verbose_name='Appointee Name')),
                ('app_apt', models.CharField(default='', max_length=8, verbose_name='Appointee Apt No')),
                ('app_street', models.CharField(default='', max_length=128, verbose_name='Appointee Street')),
                ('app_city', models.CharField(default='', max_length=64, verbose_name='Appointee City')),
                ('app_state_name', models.CharField(default='', choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('PUER', 'Puerto Rico')], max_length=64, verbose_name='Appointee State')),
                ('app_zipcode', models.CharField(default='', max_length=10, verbose_name='Appointee Zip')),
                ('app_caf', models.CharField(help_text='Nine-digits code', default='', max_length=12, verbose_name='Appointee CAF No')),
                ('app_ptin', models.CharField(help_text='Eight-digits code', default='', max_length=10, verbose_name='Appointee PTIN')),
                ('app_phone', utils.widgets.PhoneNumberField(default='', max_length=20, blank=True, verbose_name='Appointee Telephone')),
                ('app_fax', utils.widgets.PhoneNumberField(default='', max_length=20, blank=True, verbose_name='Appointee Fax')),
                ('app_addr_new', models.BooleanField(default=False, verbose_name="Is Appointee's address new?")),
                ('app_phone_new', models.BooleanField(default=False, verbose_name="Is Appointee's telephone new?")),
                ('app_fax_new', models.BooleanField(default=False, verbose_name="Is Appointee's fax new?")),
                ('specific_use_caf_recorded', models.BooleanField(help_text='If the tax information authorization is for a specific use was recorded on CAF, check this box. See the instructions.', default=False, verbose_name='Is specific use recorded on Centralized Authorization File (CAF)?')),
                ('county', models.ForeignKey(to='repository.County')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='F8821SpousePage2',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Form8821Spouse',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('client', models.OneToOneField(to='clients.Client', related_name='form8821spouse')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SpecificUseSpouse',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('copies', models.BooleanField(help_text='If you want copies of tax information, notices, and other written communications sent to the appointee on an ongoing basis, check this item. Note: Appointees will no longer receive forms, publications, and other related materials with the notices.', default=False, verbose_name='Do you want copies sent to the appointee?')),
                ('revocation', models.BooleanField(default=False, verbose_name='Retention/revocation of prior tax information authorizations')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaxInformationSpouse',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('tax_information_type', models.CharField(help_text='(Income, Employment, Payroll, Excise, Estate, Gift, Civil Penalty, Sec. 4980H Payments, etc.', default='', max_length=32)),
                ('tax_form_number', models.CharField(help_text='1040, 941, 720, etc.', default='', max_length=16)),
                ('years', models.CharField(default='', max_length=128, verbose_name='Year(s) or Period(s)')),
                ('details', models.CharField(default='', max_length=128, verbose_name='Specific Tax Matters')),
                ('formpage', models.ForeignKey(null=True, related_query_name='tax_info', related_name='tax_infos', to='irs8821.F8821SpousePage2')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='f8821spousepage2',
            name='form',
            field=models.OneToOneField(to='irs8821.Form8821Spouse', related_name='page2'),
        ),
        migrations.AddField(
            model_name='f8821spousepage1',
            name='form',
            field=models.OneToOneField(to='irs8821.Form8821Spouse', related_name='page1'),
        ),
        migrations.AddField(
            model_name='f8821spousepage1',
            name='specific_use_details',
            field=models.OneToOneField(null=True, related_name='page', to='irs8821.SpecificUseSpouse'),
        ),
    ]
