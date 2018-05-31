from django.db import models

# Create your models here.
from health.models import Counties


class Births_And_Deaths_By_Sex(models.Model):
    count_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    births = models.IntegerField()
    deaths = models.IntegerField()
    gender = models.CharField(max_length=100)
    year = models.IntegerField()

class ExpectedAndRegisteredBirthsAndDeaths(models.Model):
    count_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    coverage = models.CharField(max_length=100)
    births = models.FloatField()
    deaths = models.FloatField()
    year = models.IntegerField()

class Death_Causes(models.Model):
    cause_id = models.AutoField(primary_key=True)
    cause = models.CharField(max_length=100)

class Top_Ten_Death_Causes(models.Model):
    count_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    cause = models.ForeignKey(Death_Causes)
    percent = models.FloatField()
    total = models.IntegerField()
    year = models.IntegerField()


