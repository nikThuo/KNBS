from django.db import models

# Create your models here.
class Quantity_Value_Fish_Landed(models.Model):
    quantity_id = models.AutoField(primary_key=True)
    year = models.DateField()
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=65, decimal_places=2)

class Record_Sale_Goverment_Products(models.Model):
    record_id = models.AutoField(primary_key=True)
    year = models.DateField()
    soft_wood = models.DecimalField(max_digits=65, decimal_places=2)
    fuelwood_charcoal = models.DecimalField(max_digits=65, decimal_places=2)
    power_and_telegraph = models.DecimalField(max_digits=65, decimal_places=2)

class Trends_Envi_Natural_Resources(models.Model):
    trend_id = models.AutoField(primary_key=True)
    year = models.DateField()
    forestry_and_logging = models.DecimalField(max_digits=65, decimal_places=2)
    fishing_and_aquaculture = models.DecimalField(max_digits=65, decimal_places=2)
    mining_and_quarrying = models.DecimalField(max_digits=65, decimal_places=2)
    water_supply = models.DecimalField(max_digits=65, decimal_places=2)
    GDP_at_current_prices = models.DecimalField(max_digits=65, decimal_places=2)
    resource_as_percent_of_GDP = models.DecimalField(max_digits=65, decimal_places=2)

class Water_Purification_Points(models.Model):
    water_id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=100)
    water_purification_points = models.DecimalField(max_digits=65, decimal_places=2)
    boreholes_total = models.DecimalField(max_digits=65, decimal_places=2)
    public = models.DecimalField(max_digits=65, decimal_places=2)

class Average_Export_Prices_Ash(models.Model):
    average_id = models.AutoField(primary_key=True)
    soda_ash = models.DecimalField(max_digits=65, decimal_places=2)
    fluorspar = models.DecimalField(max_digits=65, decimal_places=2)
    year = models.DateField()

class Development_Expenditure_Water(models.Model):
    development_id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=100)
    water_development = models.DecimalField(max_digits=65, decimal_places=2)
    training_of_water_development_staff = models.DecimalField(max_digits=65, decimal_places=2)
    rural_water_supplies = models.DecimalField(max_digits=65, decimal_places=2)
    miscellaneous_and_special_water_programmes = models.DecimalField(max_digits=65, decimal_places=2)
    national_water_conservation_and_pipeline_corporation = models.DecimalField(max_digits=65, decimal_places=2)
    irrigation_development = models.DecimalField(max_digits=65, decimal_places=2)
    national_irrigation_board = models.DecimalField(max_digits=65, decimal_places=2)

class Expenditure_Cleaning_Refuse(models.Model):
    development_id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=100)
    refuse_removal = models.DecimalField(max_digits=65, decimal_places=2)

class Government_Forest(models.Model):
    govt_id = models.AutoField(primary_key=True)
    year = models.DateField()
    previous_plantation_area = models.DecimalField(max_digits=65, decimal_places=2)
    area_planted = models.DecimalField(max_digits=65, decimal_places=2)
    area_clear_felled = models.DecimalField(max_digits=65, decimal_places=2)

class Num_High_Risk_Environ_Impact(models.Model):
    risk_id = models.AutoField(primary_key=True)
    year = models.DateField()
    transport_and_communication = models.DecimalField(max_digits=65, decimal_places=2)
    energy = models.DecimalField(max_digits=65, decimal_places=2)
    tourism = models.DecimalField(max_digits=65, decimal_places=2)
    mining_and_quarrying = models.DecimalField(max_digits=65, decimal_places=2)
    human_settlements_and_Infrastructure = models.DecimalField(max_digits=65, decimal_places=2)
    agriculture_and_forestry = models.DecimalField(max_digits=65, decimal_places=2)
    commerce_and_industry = models.DecimalField(max_digits=65, decimal_places=2)
    water_resources = models.DecimalField(max_digits=65, decimal_places=2)

class Population_Wildlife(models.Model):
    population_id = models.AutoField(primary_key=True)
    year = models.DateField()
    buffalo = models.DecimalField(max_digits=65, decimal_places=2)
    burchell_zebra = models.DecimalField(max_digits=65, decimal_places=2)
    eland = models.DecimalField(max_digits=65, decimal_places=2)
    elephant = models.DecimalField(max_digits=65, decimal_places=2)
    gerenuk = models.DecimalField(max_digits=65, decimal_places=2)
    giraffe = models.DecimalField(max_digits=65, decimal_places=2)
    grant_gazelle = models.DecimalField(max_digits=65, decimal_places=2)
    grevy_zebra = models.DecimalField(max_digits=65, decimal_places=2)
    hunters_hartebeest = models.DecimalField(max_digits=65, decimal_places=2)
    impala = models.DecimalField(max_digits=65, decimal_places=2)
    kongoni = models.DecimalField(max_digits=65, decimal_places=2)
    kudu = models.DecimalField(max_digits=65, decimal_places=2)
    oryx = models.DecimalField(max_digits=65, decimal_places=2)
    ostrich = models.DecimalField(max_digits=65, decimal_places=2)
    thomson_gazelle = models.DecimalField(max_digits=65, decimal_places=2)
    topi = models.DecimalField(max_digits=65, decimal_places=2)
    warthog = models.DecimalField(max_digits=65, decimal_places=2)
    waterbuck = models.DecimalField(max_digits=65, decimal_places=2)
    wildebeest = models.DecimalField(max_digits=65, decimal_places=2)

class Quantity_Of_Total_Mineral(models.Model):
    quantity_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=65, decimal_places=2)
    year = models.DateField()

class Value_Of_Total_Mineral(models.Model):
    value_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=65, decimal_places=2)
    year = models.DateField()



