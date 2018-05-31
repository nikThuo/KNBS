from django.db import models

# Create your models here.

class Months(models.Model):
    month_id = models.AutoField(primary_key=True)
    month = models.CharField(max_length=100)

class Sectors(models.Model):
    sector_id = models.AutoField(primary_key=True)
    sector_name = models.CharField(max_length=100)
    report = models.CharField(max_length=100)
    coverage = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    table_name = models.CharField(max_length=100)
    api_url = models.CharField(max_length=100)
    embed_script = models.TextField()

class Counties(models.Model):
    county_id = models.IntegerField(primary_key=True)
    county_name = models.CharField(max_length=200)

class SubCounty(models.Model):
    count_id = models.IntegerField(primary_key=True)
    subcounty_id = models.IntegerField()
    county = models.ForeignKey(Counties)
    subcounty_name = models.CharField(max_length=100)

class DiseaseList(models.Model):
    disease_id = models.AutoField(primary_key=True)
    disease_name = models.CharField(max_length=150)

class Diseases(models.Model):
    disease_id =  models.AutoField(primary_key=True)
    year = models.IntegerField()
    accidents = models.IntegerField()
    other_diseases = models.IntegerField()
    diarrhoea = models.IntegerField()
    respiratory = models.IntegerField()
    skin = models.IntegerField()
    eye_infection = models.IntegerField()
    intestinal_worms = models.IntegerField()
    malaria = models.IntegerField()
    pneumonia = models.IntegerField()
    joint_pains = models.IntegerField()
    uti = models.IntegerField()

class Death(models.Model):
    death_id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    anaemia = models.IntegerField()
    cancer = models.IntegerField()
    heart_disease = models.IntegerField()
    hiv_aids = models.IntegerField()
    malaria = models.IntegerField()
    menengitis = models.IntegerField()
    other_accidents = models.IntegerField()
    other_causes = models.IntegerField()
    pneumonia = models.IntegerField()
    road_traffic = models.IntegerField()
    tuberclosis = models.IntegerField()

class CountyOutpatientMorbidityAboveFive(models.Model):
    morbidity_above_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    disease = models.ForeignKey(DiseaseList)
    data = models.IntegerField()
    year = models.IntegerField()

class County_Outpatient_Morbidity_Below_Five(models.Model):
    morbidity_above_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    disease = models.ForeignKey(DiseaseList)
    data = models.IntegerField()
    year = models.IntegerField()

class Facilities(models.Model):
    facility_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    facilities = models.IntegerField()
    year = models.IntegerField()

class Immunization_Rate(models.Model):
    immunization_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    rate = models.FloatField()
    year = models.IntegerField()

class Medical_Personnel(models.Model):
    medical_personnel_id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    bsc_nursing = models.IntegerField()
    clinical_officers = models.IntegerField()
    dentists = models.IntegerField()
    doctors = models.IntegerField()
    enrolled_nurses = models.IntegerField()
    pharmacists = models.IntegerField()
    pharmtech = models.IntegerField()
    health_officer = models.IntegerField()
    health_tech = models.IntegerField()
    registered_nurse = models.IntegerField()
    total = models.IntegerField()

class Nhif_Members(models.Model):
    nhif_member_id = models.AutoField(primary_key=True)
    formal_sector = models.IntegerField()
    informal_sector = models.IntegerField()
    total = models.IntegerField()
    year = models.CharField(max_length=50)

class Nhif_Resources(models.Model):
    resource_id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=50)
    benefits = models.BigIntegerField()
    contributions_net_benefits = models.BigIntegerField()
    receipts = models.BigIntegerField()

class HealthFacilitiesByOwnershipOfHealthFacilities_Ids(models.Model):
    health_facility_id = models.AutoField(primary_key=True)
    health_facility = models.CharField(max_length=100)

class HealthFacilitiesByOwnershipOfHealthFacilities(models.Model):
    facility_ownership_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    health_facility = models.ForeignKey(HealthFacilitiesByOwnershipOfHealthFacilities_Ids)
    no_of_facilities = models.IntegerField()
    year = models.IntegerField()

class RegisteredMedicalPersonnel_Ids(models.Model):
    medical_personnel_id = models.AutoField(primary_key=True)
    medical_personnel = models.CharField(max_length=100)

class RegisteredMedicalPersonnel(models.Model):
    registered_medical_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    medical_personnel = models.ForeignKey(RegisteredMedicalPersonnel_Ids)
    no_of_personnel = models.IntegerField()
    gender = models.CharField(max_length=100)
    year = models.IntegerField()

class HospitalBedsAndCots(models.Model):
    bed_cot_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    sub_county_id = models.IntegerField()
    beds = models.IntegerField()
    cots = models.IntegerField()
    year = models.IntegerField()

class Current_Use_Of_Contraception_By_County(models.Model):
    contraception_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    any_modem_method = models.DecimalField(max_digits=10, decimal_places=2)

class DistributionOfOutpatientVisitsByTypeOfHealthcareProvider(models.Model):
    health_facility_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    public = models.DecimalField(max_digits=10, decimal_places=2)
    private = models.DecimalField(max_digits=10, decimal_places=2)
    faith_based = models.DecimalField(max_digits=10,decimal_places=2)
    others = models.DecimalField(max_digits=10, decimal_places=2)

class Insurance_Coverage_By_Counties_And_Types(models.Model):
    insurance_coverage_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    insured = models.DecimalField(max_digits=10, decimal_places=2)
    nhif = models.DecimalField(max_digits=10, decimal_places=2)
    cbhi = models.DecimalField(max_digits=10, decimal_places=2)
    private = models.DecimalField(max_digits=10, decimal_places=2)
    others = models.DecimalField(max_digits=10, decimal_places=2)

class Maternal_Care(models.Model):
    maternal_care_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    percent_receiving_antenatal_care_from_a_skilled_provider = models.DecimalField(max_digits=10, decimal_places=2)
    percent_delivered_in_a_health_facility = models.DecimalField(max_digits=10, decimal_places=2)
    percent_delivered_by_a_skilled_provider = models.DecimalField(max_digits=10, decimal_places=2)

class Nutritional_Status_Of_Children(models.Model):
    nutrition_child_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    stunted = models.DecimalField(max_digits=10, decimal_places=2)
    wasted = models.DecimalField(max_digits=10, decimal_places=2)
    under_weight = models.DecimalField(max_digits=10, decimal_places=2)

class Nutritional_Status_Of_Women(models.Model):
    nutrition_adult_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    undernutrition = models.DecimalField(max_digits=10, decimal_places=2)
    normal = models.DecimalField(max_digits=10, decimal_places=2)
    overweight = models.DecimalField(max_digits=10, decimal_places=2)
    obese = models.DecimalField(max_digits=10, decimal_places=2)

class Registered_Medical_Laboratories_By_Counties(models.Model):
    reg_med_lab_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    class_a = models.IntegerField()
    class_b = models.IntegerField()
    class_c = models.IntegerField()
    class_d = models.IntegerField()
    class_e = models.IntegerField()
    class_f = models.IntegerField()
    unknown = models.IntegerField()

class Use_Of_Mosquito_Nets_By_Children(models.Model):
    use_mosquito_net_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    children_under_five_years_who_slept_under_nets_last_night = models.DecimalField(max_digits=10, decimal_places=2)

class Hiv_Aids_Awareness_And_Testing(models.Model):
    awareness_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    male = models.DecimalField(max_digits=10, decimal_places=2)
    female = models.DecimalField(max_digits=10, decimal_places=2)
    hiv_awareness = models.CharField(max_length=100)

class Registered_Active_Nhif_Members_By_County(models.Model):
    member_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    formal = models.IntegerField()
    informal = models.IntegerField()
    year = models.CharField(max_length=10)

class Registered_Active_Nhif_Members_Nationally(models.Model):
    member_id = models.AutoField(primary_key=True)
    formal = models.IntegerField()
    informal = models.IntegerField()
    year = models.CharField(max_length=10)


############################################Gender Fact Sheet############################################

class Early_Childhood_Mortality_Rates_By_Sex (models.Model):
    rate_id = models.AutoField(primary_key=True)
    mortality_rate = models.DecimalField(max_digits=10, decimal_places=1)
    status = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    year = models.CharField(max_length=10)

class Fertility_By_Education_Status (models.Model):
    fertility_id = models.AutoField(primary_key=True)
    fertility = models.DecimalField(max_digits=10, decimal_places=1)
    education_status = models.CharField(max_length=20)
    year = models.CharField(max_length=10)

class Fertility_Rate_By_Age_And_Residence (models.Model):
    fertility_id = models.AutoField(primary_key=True)
    fertility_rate = models.DecimalField(max_digits=10, decimal_places=1)
    age_group = models.CharField(max_length=10)
    residence = models.CharField(max_length=10)
    year = models.CharField(max_length=10)

class Percentage_Adults_Who_Are_Current_Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    age_group = models.CharField(max_length=10)
    women = models.DecimalField(max_digits=10, decimal_places=1)
    men = models.DecimalField(max_digits=10, decimal_places=1)
    category = models.CharField(max_length=10)

class Percentage_Incidence_Of_Diseases_In_Kenya (models.Model):
    incidence_id  = models.AutoField(primary_key=True)
    percentage_incidence = models.DecimalField(max_digits=10, decimal_places=1)
    disease  = models.CharField(max_length=20)
    year = models.IntegerField()

class Percentage_Who_Drink_Alcohol_By_Age (models.Model):
    percentage_id  = models.AutoField(primary_key=True)
    age = models.CharField(max_length=10)
    women = models.DecimalField(max_digits=10, decimal_places=1)
    men = models.DecimalField(max_digits=10, decimal_places=1)

class Place_Of_Delivery (models.Model):
    place_id  = models.AutoField(primary_key=True)
    number = models.DecimalField(max_digits=10, decimal_places=1)
    place = models.CharField(max_length=20)
    year = models.CharField(max_length=10)

class Prevalence_Of_Overweight_And_Obesity(models.Model):
    prevalence_id = models.AutoField(primary_key=True)
    age_group = models.CharField(max_length=10)
    women = models.IntegerField()
    men = models.IntegerField()
    total = models.IntegerField()
    category = models.CharField(max_length=20)


