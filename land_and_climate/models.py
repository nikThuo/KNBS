from django.db import models

# Create your models here.
from health.models import Counties


class Rainfall_Ids(models.Model):
    rainfall_id = models.AutoField(primary_key=True)
    rainFall = models.CharField(max_length=100)

class Rainfall(models.Model):
    climate_rainfall_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    rainfall = models.ForeignKey(Rainfall_Ids)
    rainfall_in_mm = models.FloatField()
    year = models.IntegerField()

    # def save(self, *args, **kwargs):
    #     self.rainfall_in_mm = round(self.value, 2)
    #     super(Rainfall, self).save(*args, **kwargs)

class Surface_Area_By_Category_Ids(models.Model):
    category_id = models.AutoField(primary_key=True)
    categories = models.CharField(max_length=100)

class Surface_Area_By_Category(models.Model):
    surface_area_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    category = models.ForeignKey(Surface_Area_By_Category_Ids)
    area_sq_km = models.FloatField()

    # def save(self, *args, **kwargs):
    #     self.area_sq_km = round(self.value, 2)
    #     super(Surface_Area_By_Category, self).save(*args, **kwargs)

class Temperature_Ids(models.Model):
    temperature_id = models.AutoField(primary_key=True)
    temperatures = models.CharField(max_length=100)

class Temperature(models.Model):
    climate_temperature_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    temperature = models.ForeignKey(Temperature_Ids)
    temp_celsius_degrees = models.FloatField()
    year = models.IntegerField()

    # def save(self, *args, **kwargs):
    #     self.temp_celsius_degrees = round(self.value, 2)
    #     super(Temperature, self).save(*args, **kwargs)

class Topography_Altitude(models.Model):
    altitude_topography_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    geography_type = models.CharField(max_length=100)
    altitude_in_metres = models.IntegerField()
    year = models.IntegerField()

class Environment_Impact_Assessments_By_Sector(models.Model):
    sector_id = models.AutoField(primary_key=True)
    sector = models.CharField(max_length=100)
    environmental_impact = models.IntegerField()
    year = models.IntegerField()

class Trends_In_Environment_And_Natural_Resources(models.Model):
    industry_id = models.AutoField(primary_key=True)
    industry = models.CharField(max_length=100)
    value_added = models.BigIntegerField()
    year = models.IntegerField()

class Wildlife_Population_Estimates_Kenya_Rangelands(models.Model):
    species_id  = models.AutoField(primary_key=True)
    animal = models.CharField(max_length=100)
    no_estimate = models.IntegerField()
    year = models.IntegerField()


