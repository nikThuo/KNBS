from django.db import models

# Create your models here.
from health.models import Counties


class Sectors(models.Model):
    sector_id = models.AutoField(primary_key=True)
    sector_name = models.CharField(max_length=100)

class Employment_Public_Sector(models.Model):
    wage_employment_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    year = models.IntegerField()
    sector = models.ForeignKey(Sectors)
    wage_employment = models.IntegerField()

class Average_Wage_Earnings_Per_Employee_Private_Sector(models.Model):
    wage_earnings_id = models.AutoField(primary_key=True)
    private_sector = models.CharField(max_length=120)
    wage_earnings = models.DecimalField(max_digits=20, decimal_places=2)
    year = models.IntegerField()

class Average_Wage_Earnings_Per_Employee_Public_Sector(models.Model):
    wage_earnings_id = models.AutoField(primary_key=True)
    public_sector = models.CharField(max_length=120)
    wage_earnings = models.DecimalField(max_digits=20, decimal_places=2)
    year = models.IntegerField()

class Memorandum_Items_In_Public_Sector(models.Model):
    memorandum_item_id = models.AutoField(primary_key=True)
    memorandum_item = models.CharField(max_length=100)
    wage_earnings = models.DecimalField(max_digits=20, decimal_places=2)
    year = models.IntegerField()

class Total_Recorded_Employment(models.Model):
    total_employment_id = models.AutoField(primary_key=True)
    sector_category = models.CharField(max_length=100)
    total_employment = models.IntegerField()
    year = models.IntegerField()

class Wage_Employment_By_Industry_And_Sex(models.Model):
    wage_employment_id = models.AutoField(primary_key=True)
    industry = models.CharField(max_length=120)
    wage_employment = models.IntegerField()
    gender = models.CharField(max_length=10)
    year = models.IntegerField()

class Wage_Employment_By_Industry_In_Private_Sector(models.Model):
    wage_employment_id = models.AutoField(primary_key=True)
    private_sector = models.CharField(max_length=120)
    wage_employment = models.IntegerField()
    year = models.IntegerField()

class Wage_Employment_By_Industry_In_Public_Sector(models.Model):
    wage_employment_id = models.AutoField(primary_key=True)
    public_sector = models.CharField(max_length=100)
    wage_employment = models.IntegerField()
    year = models.IntegerField()

















