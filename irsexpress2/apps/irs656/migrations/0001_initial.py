# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import utils.widgets
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0001_initial'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessInformation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('ein', models.CharField(null=True, max_length=32, default='', verbose_name='Employer Identification Number', blank=True)),
                ('street', models.CharField(blank=True, max_length=128, default='')),
                ('apt', models.CharField(blank=True, max_length=8, default='')),
                ('city', models.CharField(blank=True, max_length=64, default='')),
                ('state_name', models.CharField(blank=True, max_length=64, verbose_name='State', choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('PUER', 'Puerto Rico')], default='')),
                ('zipcode', models.CharField(blank=True, max_length=10, verbose_name='Zip', default='')),
                ('phone', utils.widgets.PhoneNumberField(blank=True, max_length=20, verbose_name='Phone', default='')),
                ('primary_contact', models.CharField(blank=True, max_length=64, default='')),
            ],
        ),
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
            name='F656Page1',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('first_name', models.CharField(max_length=32)),
                ('middle_name', models.CharField(blank=True, max_length=32, default='')),
                ('last_name', models.CharField(max_length=32)),
                ('ssn', localflavor.us.models.USSocialSecurityNumberField(max_length=11, verbose_name='Social Security Number on IRS Account')),
                ('ein', models.CharField(null=True, max_length=32, verbose_name='Employer Identification Number EIN', blank=True, help_text='(For self-employed individuals only)', default='')),
                ('street', models.CharField(blank=True, max_length=128, default='')),
                ('apt', models.CharField(blank=True, max_length=8, default='')),
                ('city', models.CharField(blank=True, max_length=64, default='')),
                ('state_name', models.CharField(blank=True, max_length=64, verbose_name='State', choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('PUER', 'Puerto Rico')], default='')),
                ('zipcode', models.CharField(blank=True, max_length=10, verbose_name='Zip', default='')),
                ('businessinfo', models.OneToOneField(null=True, to='irs656.BusinessInformation', related_name='page')),
                ('county', models.ForeignKey(to='repository.County')),
            ],
        ),
        migrations.CreateModel(
            name='F656Page2',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='F656Page3',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Form656',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('client', models.OneToOneField(related_name='form656', to='clients.Client')),
            ],
        ),
        migrations.CreateModel(
            name='MailingAddress',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('street', models.CharField(blank=True, max_length=128, default='')),
                ('apt', models.CharField(blank=True, max_length=8, default='')),
                ('city', models.CharField(blank=True, max_length=64, default='')),
                ('state_name', models.CharField(blank=True, max_length=64, verbose_name='State', choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('PUER', 'Puerto Rico')], default='')),
                ('zipcode', models.CharField(blank=True, max_length=10, verbose_name='Zip', default='')),
                ('county', models.ForeignKey(to='repository.County')),
            ],
        ),
        migrations.AddField(
            model_name='f656page3',
            name='form',
            field=models.OneToOneField(related_name='page3', to='irs656.Form656'),
        ),
        migrations.AddField(
            model_name='f656page2',
            name='form',
            field=models.OneToOneField(related_name='page2', to='irs656.Form656'),
        ),
        migrations.AddField(
            model_name='f656page1',
            name='form',
            field=models.OneToOneField(related_name='page1', to='irs656.Form656'),
        ),
        migrations.AddField(
            model_name='f656page1',
            name='jointoffer',
            field=models.OneToOneField(null=True, to='irs656.ClientSpouse', related_name='page'),
        ),
        migrations.AddField(
            model_name='f656page1',
            name='mailingaddr',
            field=models.OneToOneField(null=True, to='irs656.MailingAddress', related_name='page'),
        ),
    ]
