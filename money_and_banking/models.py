from django.db import models

# Create your models here.
from health.models import Months, Counties


class Commercial_Banks_Bills_Loans_Advances(models.Model):
    bills_loans_advances_id = models.AutoField(primary_key=True)
    sector = models.CharField(max_length=100)
    sub_sector = models.CharField(max_length=100)
    amount = models.IntegerField()
    month = models.ForeignKey(Months)
    year = models.IntegerField()

class Interest_Rates(models.Model):
    interest_rates_id = models.AutoField(primary_key=True)
    bank_loans_and_advances_weighted_average_rates = models.DecimalField(max_digits=10, decimal_places=2)
    average_deposit_rate = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.ForeignKey(Months)
    year = models.IntegerField()

class Monetary_Indicators_Broad_Money_Supply(models.Model):
    broad_money_supply_id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    broad_money_supply = models.IntegerField()

class Monetary_Indicators_Domestic_Credit(models.Model):
    domestic_credit_id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    private_and_other_public_bodies = models.IntegerField()
    national_government = models.IntegerField()
    total = models.IntegerField()

class Nairobi_Securities_Exchange(models.Model):
    nse_id = models.AutoField(primary_key=True)
    month = models.ForeignKey(Months)
    nse_20_share_index = models.IntegerField()
    year = models.IntegerField()

class Inflation_Rates(models.Model):
    inflation_rate_id = models.AutoField(primary_key=True)
    inflation_rate = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()

class Index(models.Model):
    institution_id = models.AutoField(primary_key=True)
    financial_institution = models.CharField(max_length=100)

class Institutions(models.Model):
    moneybanking_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    subcounty_id = models.IntegerField()
    institution = models.ForeignKey(Index)
    number = models.IntegerField()

