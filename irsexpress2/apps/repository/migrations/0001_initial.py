# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import repository.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('state_name', models.CharField(blank=True, max_length=64, verbose_name='State', choices=[('Alabama', 'Alabama'), ('Alaska', 'Alaska'), ('Arizona', 'Arizona'), ('Arkansas', 'Arkansas'), ('California', 'California'), ('Colorado', 'Colorado'), ('Connecticut', 'Connecticut'), ('Delaware', 'Delaware'), ('District of Columbia', 'District of Columbia'), ('Florida', 'Florida'), ('Georgia', 'Georgia'), ('Hawaii', 'Hawaii'), ('Idaho', 'Idaho'), ('Illinois', 'Illinois'), ('Indiana', 'Indiana'), ('Iowa', 'Iowa'), ('Kansas', 'Kansas'), ('Kentucky', 'Kentucky'), ('Louisiana', 'Louisiana'), ('Maine', 'Maine'), ('Maryland', 'Maryland'), ('Massachusetts', 'Massachusetts'), ('Michigan', 'Michigan'), ('Minnesota', 'Minnesota'), ('Mississippi', 'Mississippi'), ('Missouri', 'Missouri'), ('Montana', 'Montana'), ('Nebraska', 'Nebraska'), ('Nevada', 'Nevada'), ('New Hampshire', 'New Hampshire'), ('New Jersey', 'New Jersey'), ('New Mexico', 'New Mexico'), ('New York', 'New York'), ('North Carolina', 'North Carolina'), ('North Dakota', 'North Dakota'), ('Ohio', 'Ohio'), ('Oklahoma', 'Oklahoma'), ('Oregon', 'Oregon'), ('Pennsylvania', 'Pennsylvania'), ('Puerto Rico', 'Puerto Rico'), ('Rhode Island', 'Rhode Island'), ('South Carolina', 'South Carolina'), ('South Dakota', 'South Dakota'), ('Tennessee', 'Tennessee'), ('Texas', 'Texas'), ('Utah', 'Utah'), ('Vermont', 'Vermont'), ('Virginia', 'Virginia'), ('Washington', 'Washington'), ('West Virginia', 'West Virginia'), ('Wisconsin', 'Wisconsin'), ('Wyoming', 'Wyoming')], default='')),
                ('name', models.CharField(blank=True, max_length=64, verbose_name='County', default='')),
            ],
            options={
                'ordering': ('state_name', 'name'),
                'verbose_name_plural': 'Counties',
            },
        ),
        migrations.CreateModel(
            name='DocumentStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('document_name', models.CharField(max_length=24, unique=True, choices=[('HousingUtilitiesStandard', 'Allowable Living Expense Housing and Utilities Standards'), ('FoodClothingStandard', 'National Standards: Food, Clothing and Other Items'), ('OutOfPocketHealthCare', 'National Standards: Out-of-Pocket Health Care'), ('TransportationStandard', 'Allowable Living Expense Transportation Standards')])),
                ('success_time', models.DateTimeField(blank=True, verbose_name='Time of last successful update', default=repository.models.longlongago)),
                ('error_time', models.DateTimeField(blank=True, verbose_name='Time of last error', default=repository.models.longlongago)),
                ('lasterror', models.CharField(blank=True, max_length=256, default='')),
                ('scheduled', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('document_name',),
                'verbose_name_plural': 'DocumentStatuses',
            },
        ),
        migrations.CreateModel(
            name='FoodClothingStandard',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('expense', models.CharField(max_length=64)),
                ('family1', models.IntegerField(verbose_name='1 Person', default=0)),
                ('family2', models.IntegerField(verbose_name='2 Persons', default=0)),
                ('family3', models.IntegerField(verbose_name='3 Persons', default=0)),
                ('family4', models.IntegerField(verbose_name='4 Persons', default=0)),
                ('additional_person', models.IntegerField(verbose_name='Additional Person', default=0)),
            ],
            options={
                'verbose_name': 'National Standards: Food, Clothing and Other Items',
                'verbose_name_plural': 'National Standards: Food, Clothing and Other Items',
            },
        ),
        migrations.CreateModel(
            name='OutOfPocketHealthCare',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('max_age', models.IntegerField()),
                ('cost', models.IntegerField()),
            ],
            options={
                'verbose_name': 'National Standards: Out-of-Pocket Health Care',
                'verbose_name_plural': 'National Standards: Out-of-Pocket Health Care',
            },
        ),
        migrations.CreateModel(
            name='TransportationStandard',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('tax_type', models.CharField(null=True, max_length=20, default=None, choices=[('publictrans', 'Public Transportation'), ('ownership', 'Ownership Costs'), ('operating', 'Operating Costs')], blank=True)),
                ('cost_car1', models.IntegerField(default=0)),
                ('cost_car2', models.IntegerField(default=0)),
                ('apply_by', models.CharField(max_length=10, choices=[('national', 'National'), ('msa', 'MSA'), ('region', 'Region')], default='national')),
            ],
            options={
                'verbose_name': 'Allowable Living Expense Transportation Standards',
                'verbose_name_plural': 'Allowable Living Expense Transportation Standards',
            },
        ),
        migrations.CreateModel(
            name='HousingUtilitiesStandard',
            fields=[
                ('county', models.OneToOneField(primary_key=True, to='repository.County', serialize=False)),
                ('family1', models.IntegerField(verbose_name='Family of 1', default=0)),
                ('family2', models.IntegerField(verbose_name='Family of 2', default=0)),
                ('family3', models.IntegerField(verbose_name='Family of 3', default=0)),
                ('family4', models.IntegerField(verbose_name='Family of 4', default=0)),
                ('family_more', models.IntegerField(verbose_name='Family of 5 or more', default=0)),
            ],
            options={
                'verbose_name': 'Allowable Living Expense Housing and Utilities Standards',
                'verbose_name_plural': 'Allowable Living Expense Housing and Utilities Standards',
            },
        ),
        migrations.AddField(
            model_name='transportationstandard',
            name='county',
            field=models.OneToOneField(null=True, to='repository.County'),
        ),
    ]
