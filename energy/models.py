from django.db import models

# Create your models here.
from health.models import Counties


class AverageMonthlyPumpPricesForFuelByCategory(models.Model):
    count_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    month_id = models.IntegerField()
    super_petrol = models.FloatField()
    diesel = models.FloatField()
    kerosene = models.FloatField()
    year = models.IntegerField()

class Average_Retail_Prices_Of_Selected_Petroleum_Products(models.Model):
    retail_price_id = models.AutoField(primary_key=True)
    petroleum_product = models.CharField(max_length=100)
    retail_price_ksh = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.CharField(max_length=20)
    year = models.IntegerField()

class Net_Domestic_Sale_Of_Petroleum_Fuels_By_Consumer_Category(models.Model):
    domestic_sale_id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=100)
    quantity_tonnes = models.IntegerField()
    year = models.IntegerField()

class Value_And_Quantity_Of_Imports_Exports(models.Model):
    petroleum_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    petroleum_product = models.CharField(max_length=100)
    quantity_tonnes = models.IntegerField()
    value_millions = models.DecimalField(max_digits=20, decimal_places=4)
    year = models.IntegerField()

class Petroleum_Supply_And_Demand(models.Model):
    petroleum_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    petroleum_product = models.CharField(max_length=100)
    quantity_tonnes = models.DecimalField(max_digits=20, decimal_places=4)
    year = models.IntegerField()

class Installed_And_Effective_Capacity_Of_Electricity(models.Model):
    capacity_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    electricity_source = models.CharField(max_length=100)
    capacity_megawatts = models.DecimalField(max_digits=20, decimal_places=2)
    year = models.IntegerField()

class Generation_And_Imports_Of_Electricity(models.Model):
    electricity_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    electricity_source = models.CharField(max_length=100)
    capacity_megawatts = models.DecimalField(max_digits=20, decimal_places=2)
    year = models.IntegerField()

class Electricity_Demand_And_Supply(models.Model):
    electricity_id = models.AutoField(primary_key=True)
    demand_supply = models.CharField(max_length=100)
    capacity_megawatts = models.DecimalField(max_digits=20, decimal_places=2)
    year = models.IntegerField()