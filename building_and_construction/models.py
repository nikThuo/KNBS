from django.db import models

# Create your models here.
from health.models import Counties


class Industry_Id(models.Model):
    industry_id = models.AutoField(primary_key=True)
    industry = models.CharField(max_length=100)

class Amount(models.Model):
    buildingandconstruction_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    industry = models.ForeignKey(Industry_Id)
    amount = models.IntegerField()
    year = models.IntegerField()

class Quarterly_Civil_Engineering_Cost_Index(models.Model):
    cost_index_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    march = models.DecimalField(max_digits=15, decimal_places=2)
    june = models.DecimalField(max_digits=15, decimal_places=2)
    sept = models.DecimalField(max_digits=15, decimal_places=2)
    december = models.DecimalField(max_digits=15, decimal_places=2)
    year = models.IntegerField()

class Quarterly_Non_Residential_Build_Cost(models.Model):
    cost_index_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    march = models.DecimalField(max_digits=15, decimal_places=2)
    june = models.DecimalField(max_digits=15, decimal_places=2)
    sept = models.DecimalField(max_digits=15, decimal_places=2)
    december = models.DecimalField(max_digits=15, decimal_places=2)
    year = models.IntegerField()

class Quarterly_Overal_Construction_Cost(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    march = models.DecimalField(max_digits=15, decimal_places=2)
    june = models.DecimalField(max_digits=15, decimal_places=2)
    sept = models.DecimalField(max_digits=15, decimal_places=2)
    december = models.DecimalField(max_digits=15, decimal_places=2)
    year = models.IntegerField()

class Quarterly_Residential_Bulding_Cost(models.Model):
    building_construction_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    march = models.DecimalField(max_digits=15, decimal_places=2)
    june = models.DecimalField(max_digits=15, decimal_places=2)
    september = models.DecimalField(max_digits=15, decimal_places=2)
    december = models.DecimalField(max_digits=15, decimal_places=2)
    year = models.IntegerField()