# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import utils.widgets


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='F8821Page1',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('first_name', models.CharField(max_length=32, default='')),
                ('middle_name', models.CharField(blank=True, max_length=32, default='')),
                ('last_name', models.CharField(max_length=32, default='')),
                ('apt', models.CharField(blank=True, max_length=8, default='')),
                ('street', models.CharField(blank=True, max_length=128, default='')),
                ('city', models.CharField(blank=True, max_length=64, default='')),
                ('state_name', models.CharField(blank=True, max_length=64, verbose_name='State', choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('PUER', 'Puerto Rico')], default='')),
                ('zipcode', models.CharField(blank=True, max_length=10, verbose_name='Zip', default='')),
                ('phone', utils.widgets.PhoneNumberField(blank=True, max_length=20, verbose_name='Daytime telephone number', default='')),
                ('ssn', models.CharField(max_length=128, verbose_name='Taxpayer identification number(s)', default='')),
                ('plan_number', models.CharField(blank=True, max_length=64, default='', help_text='If applicable')),
                ('additional_appointees', models.BooleanField(help_text='If you wish to name more than one appointee, attach a list to this form', verbose_name='Would you like to name more than one appointee?', default=False)),
                ('app_name', models.CharField(max_length=128, verbose_name='Appointee Name', default='')),
                ('app_apt', models.CharField(max_length=8, verbose_name='Appointee Apt No', default='')),
                ('app_street', models.CharField(max_length=128, verbose_name='Appointee Street', default='')),
                ('app_city', models.CharField(max_length=64, verbose_name='Appointee City', default='')),
                ('app_state_name', models.CharField(max_length=64, verbose_name='Appointee State', choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('PUER', 'Puerto Rico')], default='')),
                ('app_zipcode', models.CharField(max_length=10, verbose_name='Appointee Zip', default='')),
                ('app_caf', models.CharField(max_length=12, default='', verbose_name='Appointee CAF No', help_text='Nine-digits code')),
                ('app_ptin', models.CharField(max_length=10, default='', verbose_name='Appointee PTIN', help_text='Eight-digits code')),
                ('app_phone', utils.widgets.PhoneNumberField(blank=True, max_length=20, verbose_name='Appointee Telephone', default='')),
                ('app_fax', utils.widgets.PhoneNumberField(blank=True, max_length=20, verbose_name='Appointee Fax', default='')),
                ('app_addr_new', models.BooleanField(verbose_name="Is Appointee's address new?", default=False)),
                ('app_phone_new', models.BooleanField(verbose_name="Is Appointee's telephone new?", default=False)),
                ('app_fax_new', models.BooleanField(verbose_name="Is Appointee's fax new?", default=False)),
                ('specific_use_caf_recorded', models.BooleanField(help_text='If the tax information authorization is for a specific use was recorded on CAF, check this box. See the instructions.', verbose_name='Is specific use recorded on Centralized Authorization File (CAF)?', default=False)),
                ('county', models.ForeignKey(to='repository.County')),
            ],
        ),
        migrations.CreateModel(
            name='F8821Page2',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Form8821',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('client', models.OneToOneField(related_name='form8821', to='clients.Client')),
            ],
        ),
        migrations.CreateModel(
            name='SpecificUse',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('copies', models.BooleanField(help_text='If you want copies of tax information, notices, and other written communications sent to the appointee on an ongoing basis, check this item. Note: Appointees will no longer receive forms, publications, and other related materials with the notices.', verbose_name='Do you want copies sent to the appointee?', default=False)),
                ('revocation', models.BooleanField(verbose_name='Retention/revocation of prior tax information authorizations', default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TaxInformation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('tax_information_type', models.CharField(max_length=32, default='', help_text='(Income, Employment, Payroll, Excise, Estate, Gift, Civil Penalty, Sec. 4980H Payments, etc.')),
                ('tax_form_number', models.CharField(max_length=16, default='', help_text='1040, 941, 720, etc.')),
                ('years', models.CharField(max_length=128, verbose_name='Year(s) or Period(s)', default='')),
                ('details', models.CharField(max_length=128, verbose_name='Specific Tax Matters', default='')),
                ('formpage', models.ForeignKey(null=True, related_name='tax_infos', to='irs8821.F8821Page2', related_query_name='tax_info')),
            ],
        ),
        migrations.AddField(
            model_name='f8821page2',
            name='form',
            field=models.OneToOneField(related_name='page2', to='irs8821.Form8821'),
        ),
        migrations.AddField(
            model_name='f8821page1',
            name='form',
            field=models.OneToOneField(related_name='page1', to='irs8821.Form8821'),
        ),
        migrations.AddField(
            model_name='f8821page1',
            name='specific_use_details',
            field=models.OneToOneField(null=True, to='irs8821.SpecificUse', related_name='page'),
        ),
    ]
