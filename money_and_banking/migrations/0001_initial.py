# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-28 07:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('health', '0011_months'),
    ]

    operations = [
        # migrations.CreateModel(
        #     name='Commercial_Banks_Bills_Loans_Advances',
        #     fields=[
        #         ('bills_loans_advances_id', models.AutoField(primary_key=True, serialize=False)),
        #         ('sector', models.CharField(max_length=100)),
        #         ('sub_sector', models.CharField(max_length=100)),
        #         ('amount', models.IntegerField()),
        #         ('month_id', models.IntegerField()),
        #         ('year', models.DateField()),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='Interest_Rates',
        #     fields=[
        #         ('interest_rates_id', models.AutoField(primary_key=True, serialize=False)),
        #         ('rates', models.DecimalField(decimal_places=2, max_digits=10)),
        #         ('average_deposit_rate', models.DecimalField(decimal_places=2, max_digits=10)),
        #         ('year', models.DateField()),
        #         ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Months')),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='Monetary_Indicators_Broad_Money_Supply',
        #     fields=[
        #         ('broad_money_supply_id', models.AutoField(primary_key=True, serialize=False)),
        #         ('year', models.DateField()),
        #         ('broad_money_supply', models.IntegerField()),
        #         ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Months')),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='Monetary_Indicators_Domestic_Credit',
        #     fields=[
        #         ('domestic_credit_id', models.AutoField(primary_key=True, serialize=False)),
        #         ('year', models.DateField()),
        #         ('private_public_bodies', models.IntegerField()),
        #         ('national_government', models.IntegerField()),
        #         ('total', models.IntegerField()),
        #         ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Months')),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='Nairobi_Securities_Exchange',
        #     fields=[
        #         ('nse_id', models.AutoField(primary_key=True, serialize=False)),
        #         ('nse_20_share_index', models.IntegerField()),
        #         ('year', models.DateField()),
        #         ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Months')),
        #     ],
        # ),
    ]