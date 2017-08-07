# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irs656', '0004_auto_20151216_2052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='f656page5',
            old_name='offer_amount',
            new_name='offer_amount_lumpsum',
        ),
        migrations.AddField(
            model_name='f656page5',
            name='assessed_date',
            field=models.DateField(blank=True, null=True, verbose_name='IRS Assessed Date'),
        ),
        migrations.AddField(
            model_name='f656page5',
            name='debt_total',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Total debt owed to the IRS'),
        ),
        migrations.AddField(
            model_name='f656page5',
            name='initial_payment',
            field=models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name='20% Initial Payment'),
        ),
        migrations.AddField(
            model_name='f656page5',
            name='monthly_income',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name="The Tax Payer's available monthly income"),
        ),
        migrations.AddField(
            model_name='f656page5',
            name='offer_amount_period',
            field=models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name='Total amount of your offer'),
        ),
        migrations.AddField(
            model_name='f656page5',
            name='payment_1',
            field=models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name='Payment within 1 month'),
        ),
        migrations.AddField(
            model_name='f656page5',
            name='payment_2',
            field=models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name='Payment within 2 months'),
        ),
        migrations.AddField(
            model_name='f656page5',
            name='payment_3',
            field=models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name='Payment within 3 months'),
        ),
        migrations.AddField(
            model_name='f656page5',
            name='payment_4',
            field=models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name='Payment within 4 months'),
        ),
        migrations.AddField(
            model_name='f656page5',
            name='payment_5',
            field=models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name='Payment within 5 months'),
        ),
        migrations.AlterField(
            model_name='f656page5',
            name='final_pay_month',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23')], null=True, max_length=3, verbose_name='Final payment month', blank=True),
        ),
        migrations.AlterField(
            model_name='f656page5',
            name='final_payment_day',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28')], null=True, max_length=3, verbose_name='Final payment day', blank=True),
        ),
        migrations.AlterField(
            model_name='f656page5',
            name='pay_months',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23')], null=True, max_length=3, verbose_name='Total months', blank=True),
        ),
        migrations.AlterField(
            model_name='f656page5',
            name='payment_day',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28')], null=True, max_length=3, verbose_name='Day you want to make your payment each month', blank=True),
        ),
        migrations.AlterField(
            model_name='f656page5',
            name='periodic_payment',
            field=models.BooleanField(help_text='Check here if you will pay your offer in full in 6 to 24 months', verbose_name='Periodic Payment'),
        ),
    ]
