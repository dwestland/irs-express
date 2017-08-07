# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import clients.models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('first_name', models.CharField(max_length=32)),
                ('middle_name', models.CharField(null=True, max_length=32, default='', blank=True)),
                ('last_name', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=128)),
                ('phone_home', models.CharField(blank=True, max_length=20, verbose_name='Home Phone', default='')),
                ('phone_cell', models.CharField(blank=True, max_length=20, verbose_name='Cell Phone', default='')),
                ('phone_work', models.CharField(blank=True, max_length=20, verbose_name='Work Phone', default='')),
                ('primary_phone_type', models.CharField(max_length=5, choices=[('home', 'home'), ('cell', 'cell'), ('work', 'work')], default='home')),
                ('apt', models.CharField(blank=True, max_length=8, verbose_name='Apt No', default='')),
                ('street', models.CharField(blank=True, max_length=128, default='')),
                ('city', models.CharField(blank=True, max_length=64, default='')),
                ('state_name', models.CharField(blank=True, max_length=64, verbose_name='State', choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('PUER', 'Puerto Rico')], default='')),
                ('zipcode', models.CharField(blank=True, max_length=10, verbose_name='Zip', default='')),
                ('taxyearsmissing', models.CharField(blank=True, max_length=100, verbose_name='Years Missing Tax Return', default='')),
                ('stage', models.IntegerField(blank=True, default=1)),
                ('stage_change_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(blank=True, max_length=10, choices=[('active', 'Active'), ('onhold', 'On Hold'), ('closed', 'Closed')], default='active')),
                ('summary', models.TextField(blank=True, default='')),
                ('case_opened', models.DateField(auto_now_add=True)),
                ('county', models.ForeignKey(null=True, blank=True, to='repository.County')),
            ],
        ),
        migrations.CreateModel(
            name='ClientDocument',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('uuid', models.CharField(max_length=32)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('file_name', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=128)),
                ('document', models.FileField(upload_to=clients.models.get_clientdoc_path)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('client', models.ForeignKey(related_name='documents', to='clients.Client', related_query_name='document')),
            ],
            options={
                'ordering': ('-upload_date', 'file_name'),
            },
        ),
        migrations.CreateModel(
            name='ClientNote',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('text', models.TextField(blank=True, default='')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('client', models.ForeignKey(related_name='notes', to='clients.Client', related_query_name='note')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
