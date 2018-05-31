
from django.db import models

# Create your models here.
from health.models import Counties


class PopulationBySexHouseholdsDensityAndCensusYears(models.Model):
    census_population_id = models.AutoField(primary_key=True)
    male = models.CharField(max_length=100)
    female = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    hhs = models.CharField(max_length=100)
    av_hh_size = models.CharField(max_length=100)
    approx_area = models.CharField(max_length=100)
    density = models.CharField(max_length=100)
    census_year = models.CharField(max_length=100)

class PopulationProjectionsBySelectedAgeGroup(models.Model):
    population_projection_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    range_0_4 = models.CharField(max_length=100)
    range_5_9 = models.CharField(max_length=100)
    range_10_14 = models.CharField(max_length=100)
    range_15_19 = models.CharField(max_length=100)
    range_20_24 = models.CharField(max_length=100)
    range_25_29 = models.CharField(max_length=100)
    range_30_34 = models.CharField(max_length=100)
    range_35_39 = models.CharField(max_length=100)
    range_40_44 = models.CharField(max_length=100)
    range_45_49 = models.CharField(max_length=100)
    range_50_54 = models.CharField(max_length=100)
    range_55_59 = models.CharField(max_length=100)
    range_60_64 = models.CharField(max_length=100)
    range_65_69 = models.CharField(max_length=100)
    range_70_74 = models.CharField(max_length=100)
    range_75_79 = models.CharField(max_length=100)
    range_80_plus = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    year = models.CharField(max_length=100)

class PopulationProjectionsBySpecialAgeGroups(models.Model):
    selected_age_group_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    under_1 = models.CharField(max_length=100)
    range_1_2 = models.CharField(max_length=100)
    range_3_5 = models.CharField(max_length=100)
    range_6_13 = models.CharField(max_length=100)
    range_14_17 = models.CharField(max_length=100)
    range_18_24 = models.CharField(max_length=100)
    range_18_34 = models.CharField(max_length=100)
    range_less_18 = models.CharField(max_length=100)
    range_18_plus = models.CharField(max_length=100)
    range_15_49 = models.CharField(max_length=100)
    range_15_64 = models.CharField(max_length=100)
    range_65_plus = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    year = models.CharField(max_length=100)

class Households_Type_Floor_Material_Main_Dwelling_Unit(models.Model):
    floor_material_id = models.AutoField(primary_key=True)
    material = models.CharField(max_length=100)
    households = models.IntegerField()

class Households_By_Main_Source_of_Water(models.Model):
    source_of_water_id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=100)
    total = models.IntegerField()

class By_Type_of_Disability(models.Model):
    disability_id = models.AutoField(primary_key=True)
    disability = models.IntegerField()
    females = models.IntegerField()
    males = models.IntegerField()
    total_population = models.IntegerField()

class Percentage_Households_Ownership_Household_Assets(models.Model):
    ownership_id = models.AutoField(primary_key=True)
    asset = models.CharField(max_length=100)
    percentage = models.DecimalField(max_digits=30, decimal_places=5)

class Distribution_Sex_Number_Households_Area_Density(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    area_in_square_km = models.DecimalField(max_digits=30, decimal_places=2)
    county_name = models.CharField(max_length=100)
    density = models.DecimalField(max_digits=30, decimal_places=7)
    female = models.IntegerField()
    male = models.IntegerField()
    no_of_houseHolds = models.IntegerField()
    total_population = models.IntegerField()

class By_Sex_And_School_Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    education_level = models.CharField(max_length=100)
    female = models.IntegerField()
    male = models.IntegerField()
    total_population = models.IntegerField()

class By_Sex_And_Age_Groups(models.Model):
    group_id = models.AutoField(primary_key=True)
    female = models.IntegerField()
    male = models.IntegerField()
    total_population = models.IntegerField()
    age_group = models.CharField(max_length=100)

