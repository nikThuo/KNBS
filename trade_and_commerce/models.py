from django.db import models

# Create your models here.'
from health.models import Counties


class Revenue_Collection_By_Title(models.Model):
    tradeandcommerce_by_title_id = models.AutoField(primary_key=True)
    tradeandcommerce_title = models.CharField(max_length=100)

class Revenue_Collection_By_Id(models.Model):
    revenuecollection_id = models.AutoField(primary_key=True)
    revenuecollection_title = models.CharField(max_length=100)

class Revenue_Collection_By_Amount(models.Model):
    tradeandcommerce_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    revenuecollection = models.ForeignKey(Revenue_Collection_By_Id)
    amount = models.IntegerField()
    year = models.IntegerField()

class Trading_Centres_Ids(models.Model):
    trading_centre_id = models.AutoField(primary_key=True)
    trading_centre = models.CharField(max_length=100)

class Trading_Centres(models.Model):
    tradeandcommerce_centre_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    trading_centre = models.ForeignKey(Trading_Centres_Ids)
    number = models.IntegerField()
    year  = models.IntegerField()

class Balance_Of_Trade(models.Model):
    trade_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    amount_in_millions = models.IntegerField()
    year = models.IntegerField()

class Import_Trade_Africa_Countries(models.Model):
    import_id = models.AutoField(primary_key=True)
    zones = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    values = models.IntegerField()
    year = models.IntegerField()

class Quantities_Principal_Domestic_Exports(models.Model):
    trade_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    year = models.IntegerField()

class Quantities_Principal_Imports(models.Model):
    trade_id = models.AutoField(primary_key=True)
    commodity = models.CharField(max_length=100)
    unit_of_quantity = models.CharField(max_length=100)
    quantity = models.IntegerField()
    year = models.IntegerField()

class Values_Of_Principal_Domestic_Exports(models.Model):
    trade_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    values = models.IntegerField()
    year = models.IntegerField()

class Values_Of_Principal_Imports(models.Model):
    trade_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    year = models.IntegerField()

class Value_Of_Total_Exports_All_Destinations(models.Model):
    export_id = models.AutoField(primary_key=True)
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    value_in_millions = models.DecimalField(max_digits=65, decimal_places=2)
    year = models.IntegerField()

class Value_of_Total_Exports_European_Union(models.Model):
    export_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=100)
    value_in_millions = models.DecimalField(max_digits=65, decimal_places=2)
    year = models.IntegerField()

class Value_Total_Exports_East_Africa_Communities(models.Model):
    export_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=100)
    value_in_millions = models.DecimalField(max_digits=65, decimal_places=2)
    year = models.IntegerField()