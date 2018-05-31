from django.db import models

# Create your models here.
from health.models import Counties


class Coverage_Of_Postal_Services_Ids(models.Model):
    postal_service_id = models.AutoField(primary_key=True)
    postal_service = models.CharField(max_length=100)

class Coverage_Of_Postal_Services(models.Model):
    postal_coverage_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    postal_service = models.ForeignKey(Coverage_Of_Postal_Services_Ids)
    number = models.IntegerField()
    year = models.IntegerField()

class Coverage_Of_Telephone_Services_Ids(models.Model):
    telephone_service_id = models.AutoField(primary_key=True)
    telephone_service = models.CharField(max_length=100)

class Coverage_Of_Telephone_Services(models.Model):
    telephone_coverage_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    telephone_service = models.ForeignKey(Coverage_Of_Telephone_Services_Ids)
    number = models.IntegerField()
    year = models.IntegerField()

class Road_Coverage_Type_Distance_Ids(models.Model):
    road_type_id = models.AutoField(primary_key=True)
    road_type = models.CharField(max_length=100)

class Road_Coverage_By_Type_And_Distance(models.Model):
    road_coverage_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    road_type = models.ForeignKey(Road_Coverage_Type_Distance_Ids)
    distance = models.FloatField()
    year = models.IntegerField()

    # def save(self, *args, **kwargs):
    #     self.distance = round(self.value, 2)
    #     super(Road_Coverage_By_Type_And_Distance, self).save(*args, **kwargs)

class Expenditure_On_Roads(models.Model):
    expenditure_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    expenditure = models.BigIntegerField()
    year = models.IntegerField()

class Status_Of_Ongoing_Roads_Programme(models.Model):
    road_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    length = models.DecimalField(max_digits=10, decimal_places=2)
    percentage_completion = models.DecimalField(max_digits=10, decimal_places=2)
    estimated_project_cost = models.DecimalField(max_digits=10, decimal_places=2)
