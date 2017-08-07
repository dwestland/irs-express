# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irs656', '0003_auto_20151215_1945'),
    ]

    operations = [
        migrations.CreateModel(
            name='F656Page5',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('offer_amount', models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name='Total amount of your offer')),
                ('lump_sum_cash', models.BooleanField(help_text='Check here if you will pay your offer in 5 or fewer payments in 5 or fewer months from the date of acceptance', verbose_name='Lump Sum Cash')),
                ('periodic_payment', models.BooleanField(help_text='Check here if you will pay your offer in full in 6 to 24 months', verbose_name='Lump Sum Cash')),
                ('offer_included', models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name='Included with this offer')),
                ('monthly_payment', models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name='Monthly payment')),
                ('payment_day', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28')], verbose_name='Day you want to make your payment each month', max_length=3)),
                ('pay_months', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23')], verbose_name='Total months', max_length=3)),
                ('final_payment', models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name='Final payment')),
                ('final_payment_day', models.CharField(verbose_name='Final payment day', max_length=3)),
                ('final_pay_month', models.CharField(verbose_name='Final payment month', max_length=3)),
                ('form', models.OneToOneField(related_name='page5', to='irs656.Form656')),
            ],
        ),
        migrations.CreateModel(
            name='F656Page6',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('tax_form', models.CharField(blank=True, null=True, default='', max_length=20)),
                ('tax_year', models.CharField(blank=True, null=True, default='', verbose_name='Tax year/quarter', max_length=20)),
                ('has_deposit', models.BooleanField(verbose_name='Would you like to treat any part of the payment as a deposit?')),
                ('total_payment', models.PositiveIntegerField(blank=True, null=True, default=0)),
                ('initial_payment', models.PositiveIntegerField(blank=True, null=True, default=0)),
                ('deposit_payment', models.PositiveIntegerField(blank=True, null=True, default=0)),
                ('funds_source', models.TextField(blank=True, null=True, default='', help_text='Tell us where you will obtain the funds to pay your offer. You may consider borrowing from friends and/or family, taking out a loan, or selling assets.', verbose_name='Source of Funds')),
                ('all_taxreturns_filed', models.BooleanField(default=True, verbose_name='I certify that I have filed all required tax returns')),
                ('noreturn_for', models.BooleanField(default=True, verbose_name='I certify that I was not required to file a tax return for the following years')),
                ('noreturn_for_years', models.CharField(blank=True, null=True, default='', verbose_name='Years', max_length=64)),
                ('form', models.OneToOneField(related_name='page6', to='irs656.Form656')),
            ],
        ),
        migrations.CreateModel(
            name='F656Page7',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('form', models.OneToOneField(related_name='page7', to='irs656.Form656')),
            ],
        ),
        migrations.AlterField(
            model_name='f656page3',
            name='exceptional_circumstances',
            field=models.BooleanField(default=False, help_text='I owe this amount and have sufficient assets to pay the full amount, but due to my exceptional circumstances, requiring full payment would cause an economic hardship or would be unfair and inequitable. I am submitting a written narrative explaining my circumstances.', verbose_name='Exceptional Circumstances (Effective Tax Administration)'),
        ),
    ]
