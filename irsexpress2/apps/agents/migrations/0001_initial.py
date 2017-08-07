# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import utils.widgets


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(default='', verbose_name='Name', max_length=128)),
                ('street', models.CharField(default='', verbose_name='Street', max_length=128)),
                ('apt', models.CharField(default='', blank=True, verbose_name='Apt No', max_length=8)),
                ('city', models.CharField(default='', verbose_name='City', max_length=64)),
                ('state_name', models.CharField(default='', max_length=64, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('PUER', 'Puerto Rico')], verbose_name='State')),
                ('zipcode', models.CharField(default='', verbose_name='Zip', max_length=10)),
                ('caf', models.CharField(help_text='Nine-digits code', default='', blank=True, verbose_name='CAF No', max_length=12)),
                ('ptin', models.CharField(help_text='Eight-digits code', default='', blank=True, verbose_name='PTIN', max_length=10)),
                ('phone', utils.widgets.PhoneNumberField(default='', blank=True, verbose_name='Telephone', max_length=20)),
                ('fax', utils.widgets.PhoneNumberField(default='', blank=True, verbose_name='Fax', max_length=20)),
                ('addr_new', models.BooleanField(default=False, verbose_name="Is Appointee's address new?")),
                ('phone_new', models.BooleanField(default=False, verbose_name="Is Appointee's telephone new?")),
                ('fax_new', models.BooleanField(default=False, verbose_name="Is Appointee's fax new?")),
            ],
            options={
                'ordering': ('id',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Preparer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(default='', verbose_name='Name', max_length=128)),
                ('street', models.CharField(default='', verbose_name='Street', max_length=128)),
                ('apt', models.CharField(default='', blank=True, verbose_name='Apt No', max_length=8)),
                ('city', models.CharField(default='', verbose_name='City', max_length=64)),
                ('state_name', models.CharField(default='', max_length=64, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('PUER', 'Puerto Rico')], verbose_name='State')),
                ('zipcode', models.CharField(default='', verbose_name='Zip', max_length=10)),
                ('caf', models.CharField(help_text='Nine-digits code', default='', blank=True, verbose_name='CAF No', max_length=12)),
                ('ptin', models.CharField(help_text='Eight-digits code', default='', blank=True, verbose_name='PTIN', max_length=10)),
                ('phone', utils.widgets.PhoneNumberField(default='', blank=True, verbose_name='Telephone', max_length=20)),
                ('date', models.DateField(default=None, blank=True, null=True)),
                ('firm_name', models.CharField(default='', blank=True, verbose_name="Firm's name (or taxpayer's if self-employed)", max_length=32, null=True)),
            ],
            options={
                'ordering': ('id',),
                'abstract': False,
            },
        ),
    ]
