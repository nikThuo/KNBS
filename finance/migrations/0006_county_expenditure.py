# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-14 07:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0009_registered_active_nhif_members_by_county_registered_active_nhif_members_nationally'),
        ('finance', '0005_allocation_and_disbursement_of_funds_social_protection'),
    ]

    operations = [
        # migrations.CreateModel(
        #     name='County_Expenditure',
        #     fields=[
        #         ('countyexpenditure_id', models.AutoField(primary_key=True, serialize=False)),
        #         ('compensation_employees', models.DecimalField(decimal_places=2, max_digits=15)),
        #         ('goods_services', models.DecimalField(decimal_places=2, max_digits=15)),
        #         ('subsidies', models.DecimalField(decimal_places=2, max_digits=15)),
        #         ('grants_internationalorganisation', models.DecimalField(decimal_places=2, max_digits=15)),
        #         ('grants_governmentunits', models.DecimalField(decimal_places=2, max_digits=15)),
        #         ('othergrants', models.DecimalField(decimal_places=2, max_digits=15)),
        #         ('capitalgrants', models.DecimalField(decimal_places=2, max_digits=15)),
        #         ('socialbenefits', models.DecimalField(decimal_places=2, max_digits=15)),
        #         ('otherexpense', models.DecimalField(decimal_places=2, max_digits=15)),
        #         ('buildingstructures', models.DecimalField(decimal_places=2, max_digits=15)),
        #         ('plantmachinery_equipment', models.DecimalField(decimal_places=2, max_digits=15)),
        #         ('inventories', models.DecimalField(decimal_places=2, max_digits=15)),
        #         ('otherassets', models.DecimalField(decimal_places=2, max_digits=15)),
        #         ('acquisition_financialassets', models.DecimalField(decimal_places=2, max_digits=15)),
        #         ('interest_debt', models.DecimalField(decimal_places=2, max_digits=15)),
        #         ('total', models.DecimalField(decimal_places=2, max_digits=15)),
        #         ('year', models.CharField(max_length=50)),
        #         ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
        #     ],
        # ),
    ]