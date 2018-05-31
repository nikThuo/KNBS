# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from __future__ import unicode_literals
#
# from django.db import models
#
#
# class Counties(models.Model):
#     county_id = models.IntegerField(primary_key=True)
#     county_name = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.county_name
#
#     class Meta:
#         db_table = 'counties'
#
#
# # class CountyBudgetAllocation(models.Model):
# #     budget_allocation_id = models.AutoField(db_column='budget_allocation_ID', primary_key=True)  # Field name made lowercase.
# #     county_id = models.IntegerField()
# #     recurrent = models.CharField(max_length=255)
# #     development = models.CharField(max_length=255)
# #     total = models.CharField(max_length=255)
# #     year = models.CharField(max_length=20)
# #
# #     class Meta:
# #         db_table = 'county_budget_allocation'
#
#
# class CountyExpenditure(models.Model):
#     countyexpenditure_id = models.AutoField(primary_key=True)
#     county_id = models.IntegerField()
#     compensation_employees = models.CharField(max_length=250)
#     goods_services = models.CharField(max_length=250)
#     subsidies = models.CharField(max_length=250)
#     grants_internationalorganisation = models.CharField(max_length=250)
#     grants_governmentunits = models.CharField(max_length=250)
#     othergrants = models.CharField(max_length=250)
#     capitalgrants = models.CharField(max_length=250)
#     socialbenefits = models.CharField(max_length=250)
#     otherexpense = models.CharField(max_length=250)
#     buildingstructures = models.CharField(max_length=250)
#     plantmachinery_equipment = models.CharField(max_length=250)
#     inventories = models.CharField(max_length=250)
#     otherassets = models.CharField(max_length=250)
#     acquisition_financialassets = models.CharField(max_length=250)
#     interest_debt = models.CharField(max_length=250)
#     total = models.CharField(max_length=250)
#     year = models.CharField(max_length=250)
#
#     class Meta:
#         db_table = 'county_expenditure'
#
#
# # class CountyRevenue(models.Model):
# #     county_revenue_id = models.AutoField(primary_key=True)
# #     revenue_estimates = models.CharField(max_length=200)
# #     conditional_grant = models.CharField(max_length=200)
# #     county_id = models.CharField(max_length=200)
# #     equitable_share = models.CharField(max_length=200)
# #     total_revenue = models.CharField(max_length=200)
# #     year = models.CharField(max_length=20)
# #
# #     class Meta:
# #         db_table = 'county_revenue'
#
#
# class CoverageRatesOfBirthsDeaths(models.Model):
#     rates_id = models.AutoField(primary_key=True)
#     county = models.CharField(max_length=50)
#     year = models.CharField(max_length=50)
#     births = models.CharField(max_length=50)
#     deaths = models.CharField(max_length=50)
#
#     class Meta:
#         db_table = 'coverage_rates_of_births_deaths'
#
#
# class Death(models.Model):
#     death_id = models.AutoField(primary_key=True)
#     year = models.IntegerField()
#     anaemia = models.IntegerField()
#     cancer = models.IntegerField()
#     heart_disease = models.IntegerField()
#     hiv_aids = models.IntegerField()
#     malaria = models.IntegerField()
#     menengitis = models.IntegerField()
#     other_accidents = models.IntegerField()
#     other_causes = models.IntegerField()
#     pneumonia = models.IntegerField()
#     road_traffic = models.IntegerField()
#     tuberclosis = models.IntegerField()
#
#     class Meta:
#         db_table = 'death'
#
#
# class Diseases(models.Model):
#     disease_id = models.AutoField(primary_key=True)
#     year = models.IntegerField()
#     accidents = models.IntegerField()
#     other_diseases = models.IntegerField()
#     diarrhoea = models.IntegerField()
#     respiratory = models.IntegerField()
#     skin = models.IntegerField()
#     eye_infection = models.IntegerField()
#     intestinal_worms = models.IntegerField()
#     malaria = models.IntegerField()
#     pneumonia = models.IntegerField()
#     joint_pains = models.IntegerField()
#     uti = models.IntegerField()
#
#     class Meta:
#         db_table = 'diseases'
#
#
# # class EconomicClassificationRevenue(models.Model):
# #     economicrevenue_id = models.AutoField(primary_key=True)
# #     taxes_income_profits_capitalgains = models.CharField(max_length=250)
# #     taxes_property = models.CharField(max_length=250)
# #     taxes_vat = models.CharField(max_length=250)
# #     taxes_othergoodsandservices = models.CharField(max_length=250)
# #     taxes_internationaltrade_transactions = models.CharField(max_length=250)
# #     other_taxes_notelsewhereclasified = models.CharField(max_length=250)
# #     totaltax_revenue = models.CharField(max_length=250)
# #     socialsecuritycontributions = models.CharField(max_length=250)
# #     property_income = models.CharField(max_length=250)
# #     sale_goodsandservices = models.CharField(max_length=250)
# #     fines_penaltiesandforfeitures = models.CharField(max_length=250)
# #     repayments_domesticlending = models.CharField(max_length=250)
# #     other_receiptsnotelsewhereclassified = models.CharField(max_length=250)
# #     total_nontax_revenue = models.CharField(max_length=250)
# #     total = models.CharField(max_length=250)
# #     year = models.CharField(max_length=250)
# #
# #     class Meta:
# #         db_table = 'economic_classification_revenue'
#
#
# class Enrolment(models.Model):
#     enrolment_id = models.AutoField(primary_key=True)
#     year = models.CharField(max_length=100)
#     male = models.IntegerField()
#     female = models.IntegerField()
#     total_enrolment = models.IntegerField()
#
#     class Meta:
#         db_table = 'enrolment'
#
#
# class EstimatedHivPrevalenceRate(models.Model):
#     prevalence_rate_id = models.AutoField(primary_key=True)
#     year = models.CharField(max_length=50)
#     hiv_rate = models.CharField(max_length=50)
#
#     class Meta:
#         db_table = 'estimated_hiv_prevalence_rate'
#
#
# # class ExciseRevenueCommodity(models.Model):
# #     excise_id = models.AutoField(primary_key=True)
# #     year = models.CharField(max_length=250)
# #     beer = models.CharField(max_length=250)
# #     cigarettes = models.CharField(max_length=250)
# #     mineral_waters = models.CharField(max_length=250)
# #     wines_spirits = models.CharField(max_length=250)
# #     other_commodities = models.CharField(max_length=250)
# #     total = models.CharField(max_length=250)
# #
# #     class Meta:
# #         db_table = 'excise_revenue_commodity'
#
#
# # class HealthFacilities(models.Model):
# #     facility_id = models.AutoField(primary_key=True)
# #     county_id = models.IntegerField()
# #     facilities = models.IntegerField()
# #     year = models.IntegerField()
# #
# #     class Meta:
# #         db_table = 'health_facilities'
#
#
# class KnbsAdmin(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=200)
#     email = models.CharField(max_length=150)
#     pin = models.CharField(max_length=100)
#     user_image = models.CharField(max_length=150)
#     isactive = models.IntegerField(db_column='isActive')  # Field name made lowercase.
#
#     class Meta:
#         db_table = 'knbs_admin'
#
#
# # class MedicalPersonnel(models.Model):
# #     medical_personnel_id = models.AutoField(primary_key=True)
# #     year = models.IntegerField()
# #     bsc_nursing = models.IntegerField()
# #     clinical_officers = models.IntegerField()
# #     dentists = models.IntegerField()
# #     doctors = models.IntegerField()
# #     enrolled_nurses = models.IntegerField()
# #     pharmacists = models.IntegerField()
# #     pharmtech = models.IntegerField()
# #     health_officer = models.IntegerField()
# #     health_tech = models.IntegerField()
# #     registered_nurse = models.IntegerField()
# #     total = models.IntegerField()
# #
# #     class Meta:
# #         db_table = 'medical_personnel'
#
#
# # class NationalGovernmentExpenditure(models.Model):
# #     government_expenditure_id = models.AutoField(primary_key=True)
# #     acquisition_nonfinancial_assets = models.CharField(max_length=250)
# #     acquisition_financial_assets = models.CharField(max_length=250)
# #     loans_repayments = models.CharField(max_length=250)
# #     compensation_employees = models.CharField(max_length=250)
# #     goods_services = models.CharField(max_length=250)
# #     subsidies = models.CharField(max_length=250)
# #     interest = models.CharField(max_length=250)
# #     grants = models.CharField(max_length=250)
# #     other_expense = models.CharField(max_length=250)
# #     social_benefits = models.CharField(max_length=250)
# #     capital_grants = models.CharField(max_length=250)
# #     total = models.CharField(max_length=250)
# #     year = models.CharField(max_length=250)
# #
# #     class Meta:
# #         db_table = 'national_government_expenditure'
# #
# #
# # class NationalGovernmentExpenditurePurpose(models.Model):
# #     purpose_id = models.AutoField(primary_key=True)
# #     year = models.CharField(max_length=20)
# #     general_publicservices = models.CharField(max_length=250)
# #     public_debttransactions = models.CharField(max_length=250)
# #     transfers = models.CharField(max_length=250)
# #     defense = models.CharField(max_length=250)
# #     order_safety = models.CharField(max_length=250)
# #     economic_commercial_labor = models.CharField(max_length=250)
# #     agriculture = models.CharField(max_length=250)
# #     fuel_energy = models.CharField(max_length=250)
# #     mining_manufacturing_construction = models.CharField(max_length=250)
# #     transport = models.CharField(max_length=250)
# #     communication = models.CharField(max_length=250)
# #     other_industries = models.CharField(max_length=250)
# #     environmental_protection = models.CharField(max_length=250)
# #     housing_communityamenities = models.CharField(max_length=250)
# #     health = models.CharField(max_length=250)
# #     recreation_culture_religion = models.CharField(max_length=250)
# #     education = models.CharField(max_length=250)
# #     socialprotection = models.CharField(max_length=250)
# #
# #     class Meta:
# #         db_table = 'national_government_expenditure_purpose'
#
#
# # class NhifMembers(models.Model):
# #     nhif_member_id = models.AutoField(primary_key=True)
# #     formal_sector = models.IntegerField()
# #     informal_sector = models.IntegerField()
# #     total = models.IntegerField()
# #     year = models.CharField(max_length=50)
# #
# #     class Meta:
# #         db_table = 'nhif_members'
# #
# #
# # class NhifResources(models.Model):
# #     resource_id = models.AutoField(primary_key=True)
# #     year = models.CharField(max_length=50)
# #     benefits = models.BigIntegerField()
# #     contributions_net_benefits = models.BigIntegerField()
# #     receipts = models.BigIntegerField()
# #
# #     class Meta:
# #         db_table = 'nhif_resources'
#
#
# # class OutstandingDebtInternationalOrganization(models.Model):
# #     outstanding_debt = models.AutoField(primary_key=True)
# #     ida = models.CharField(max_length=250)
# #     eec_eib = models.CharField(max_length=250)
# #     imf = models.CharField(max_length=250)
# #     adf_adb = models.CharField(max_length=250)
# #     commercial_banks = models.CharField(max_length=250)
# #     others = models.CharField(max_length=250)
# #     year = models.CharField(max_length=50)
# #
# #     class Meta:
# #         db_table = 'outstanding_debt_international_organization'
# #
# #
# # class OutstandingDebtLendingCountry(models.Model):
# #     lending_country_id = models.AutoField(primary_key=True)
# #     germany = models.CharField(max_length=250)
# #     japan = models.CharField(max_length=250)
# #     france = models.CharField(max_length=250)
# #     usa = models.CharField(max_length=250)
# #     netherlands = models.CharField(max_length=250)
# #     denmark = models.CharField(max_length=250)
# #     finland = models.CharField(max_length=250)
# #     china = models.CharField(max_length=250)
# #     belgium = models.CharField(max_length=250)
# #     other = models.CharField(max_length=250)
# #     year = models.IntegerField()
# #
# #     class Meta:
# #         db_table = 'outstanding_debt_lending_country'
#
#
# class PopulationAndHousingCensus(models.Model):
#     census_id = models.AutoField(primary_key=True)
#     name_of_centre = models.CharField(max_length=50)
#     district = models.CharField(max_length=50)
#     status = models.CharField(max_length=50)
#     male = models.CharField(max_length=50)
#     female = models.CharField(max_length=50)
#     total = models.CharField(max_length=50)
#     sex_ratio = models.CharField(max_length=50)
#
#     class Meta:
#         db_table = 'population_and_housing_census'
#
#
# class ProjectedLifeExpectancy(models.Model):
#     life_expectancy_id = models.AutoField(primary_key=True)
#     hiv_status = models.CharField(max_length=50)
#     gender = models.CharField(max_length=50)
#     year_range = models.CharField(max_length=50)
#     expectancy_index = models.CharField(max_length=50)
#
#     class Meta:
#         db_table = 'projected_life_expectancy'
#
#
# class RegisteredBirthsOccurrence(models.Model):
#     birth_id = models.AutoField(primary_key=True)
#     county = models.CharField(max_length=50)
#     year = models.CharField(max_length=50)
#     health_facility = models.CharField(max_length=50)
#     home = models.CharField(max_length=50)
#
#     class Meta:
#         db_table = 'registered_births_&_occurrence'
#
#
# class RegisteredDeathsOccurrence(models.Model):
#     death_id = models.AutoField(primary_key=True)
#     county = models.CharField(max_length=50)
#     year = models.CharField(max_length=50)
#     health_facility = models.CharField(max_length=50)
#     home = models.CharField(max_length=50)
#
#     class Meta:
#         db_table = 'registered_deaths_&_occurrence'
#
#
# class Sectors(models.Model):
#     sector_id = models.AutoField(primary_key=True)
#     sector_name = models.CharField(max_length=255)
#     dataset_title = models.CharField(max_length=500)
#
#     class Meta:
#         db_table = 'sectors'
#
#
# class Students(models.Model):
#     id = models.IntegerField(primary_key=True)
#     lastname = models.CharField(db_column='Lastname', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     course = models.CharField(db_column='Course', max_length=70, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         db_table = 'students'
#
#
# class VitalStatistics(models.Model):
#     vital_id = models.AutoField(primary_key=True)
#     county = models.CharField(max_length=50)
#     year = models.CharField(max_length=50)
#     births = models.CharField(max_length=50)
#     deaths = models.CharField(max_length=50)
#
#     class Meta:
#         db_table = 'vital_statistics'
