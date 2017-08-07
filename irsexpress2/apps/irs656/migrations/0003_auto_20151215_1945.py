# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irs656', '0002_auto_20151214_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='F656Page4',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('low_income_qualify', models.BooleanField(verbose_name='Do you qualify for Low-Income Certification?', default=False)),
                ('form', models.OneToOneField(to='irs656.Form656', related_name='page4')),
            ],
        ),
        migrations.AddField(
            model_name='f656page3',
            name='circumstances',
            field=models.TextField(null=True, blank=True, verbose_name='Explanation of Circumstances', help_text='The IRS understands that there are unplanned events or special circumstances, such as serious illness, where paying the full amount or the minimum offer amount might impair your ability to provide for yourself and your family. If this is the case and you can provide documentation to prove your situation, then your offer may be accepted despite your financial profile. Describe your situation here and attach appropriate documents to this offer application.', default=''),
        ),
        migrations.AddField(
            model_name='f656page3',
            name='doubt_collectibility',
            field=models.BooleanField(verbose_name='Doubt as to Collectibility', help_text='Set if you have insufficient assets and income to pay the full amount', default=False),
        ),
        migrations.AddField(
            model_name='f656page3',
            name='exceptional_circumstances',
            field=models.BooleanField(verbose_name='', default=False),
        ),
    ]
