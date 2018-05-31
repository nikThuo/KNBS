from django.db import models

# Create your models here.
class Annual_Avg_Retail_Prices_Of_Certain_Consumer_Goods_In_Kenya(models.Model):
    avg_retail_price_id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    ksh_per_unit = models.DecimalField(max_digits=20, decimal_places=10)
    year = models.IntegerField()

class Consumer_Price_Index(models.Model):
    cpi_retail_price_id = models.AutoField(primary_key=True)
    month = models.CharField(max_length=100)
    year = models.IntegerField()
    group = models.CharField(max_length=100)
    food_and_non_alcoholic_beverages = models.DecimalField(max_digits=20, decimal_places=10)
    alcoholic_beverages_tobacco_narcotics = models.DecimalField(max_digits=20, decimal_places=10)
    clothing_and_footwear = models.DecimalField(max_digits=20, decimal_places=10)
    housing_water_electricity_gas_and_other_fuels = models.DecimalField(max_digits=20, decimal_places=10)
    furnishings_household_equipment_routine_household_maintenance = models.DecimalField(max_digits=20, decimal_places=10)
    health = models.DecimalField(max_digits=20, decimal_places=10)
    transport = models.DecimalField(max_digits=20, decimal_places=10)
    communication = models.DecimalField(max_digits=20, decimal_places=10)
    recreation_and_culture = models.DecimalField(max_digits=20, decimal_places=10)
    education = models.DecimalField(max_digits=20, decimal_places=10)
    restaurant_and_hotels = models.DecimalField(max_digits=20, decimal_places=10)
    miscellaneous_goods_and_services = models.DecimalField(max_digits=20, decimal_places=10)
    total = models.DecimalField(max_digits=20, decimal_places=10)

class Elementary_Aggregates_Weights_In_The_Cpi_Baskets(models.Model):
    aggregate_weights_id = models.AutoField(primary_key=True)
    coicop_code = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    nairobi_lower = models.DecimalField(max_digits=20, decimal_places=10)
    nairobi_middle = models.DecimalField(max_digits=20, decimal_places=10)
    nairobi_upper = models.DecimalField(max_digits=20, decimal_places=10)
    rest_of_urban_areas = models.DecimalField(max_digits=20, decimal_places=10)
    kenya = models.DecimalField(max_digits=20, decimal_places=10)

class Group_Weights_For_Kenya_Cpi_Febuary_Base_2009(models.Model):
    group_weights_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    household = models.CharField(max_length=100)
    group_weights = models.DecimalField(max_digits=20, decimal_places=10)

class Group_Weights_For_Kenya_Cpi_October_Base_1997(models.Model):
    group_weight_id = models.AutoField(primary_key=True)
    item_group = models.CharField(max_length=100)
    household = models.CharField(max_length=100)
    group_weights = models.DecimalField(max_digits=20, decimal_places=10)