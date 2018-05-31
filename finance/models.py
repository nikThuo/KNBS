from django.db import models

# Create your models here.
from health.models import Counties


class Cdf_Allocation(models.Model):
    cdfallocation_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    subcounty_id = models.IntegerField()
    cdfallocation = models.IntegerField()
    year = models.IntegerField()

class County_Budget_Allocation(models.Model):
    budget_allocation_id = models.AutoField(db_column='budget_allocation_ID', primary_key=True)  # Field name made lowercase.
    county = models.ForeignKey(Counties)
    recurrent = models.CharField(max_length=255)
    development = models.CharField(max_length=255)
    total_allocation = models.CharField(max_length=255)
    year = models.CharField(max_length=20)


class County_Expenditure(models.Model):
    countyexpenditure_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    compensation_employees = models.DecimalField(max_digits=15, decimal_places=2)
    goods_services = models.DecimalField(max_digits=15, decimal_places=2)
    subsidies = models.DecimalField(max_digits=15, decimal_places=2)
    grants_internationalorganisation = models.DecimalField(max_digits=15, decimal_places=2)
    grants_governmentunits = models.DecimalField(max_digits=15, decimal_places=2)
    othergrants = models.DecimalField(max_digits=15, decimal_places=2)
    capitalgrants = models.DecimalField(max_digits=15, decimal_places=2)
    socialbenefits = models.DecimalField(max_digits=15, decimal_places=2)
    otherexpense = models.DecimalField(max_digits=15, decimal_places=2)
    buildingstructures = models.DecimalField(max_digits=15, decimal_places=2)
    plantmachinery_equipment = models.DecimalField(max_digits=15, decimal_places=2)
    inventories = models.DecimalField(max_digits=15, decimal_places=2)
    otherassets = models.DecimalField(max_digits=15, decimal_places=2)
    acquisition_financialassets = models.DecimalField(max_digits=15, decimal_places=2)
    interest_debt = models.DecimalField(max_digits=15, decimal_places=2)
    total_expenditure = models.DecimalField(max_digits=15, decimal_places=2)
    year = models.CharField(max_length=50)


class County_Revenue(models.Model):
    county_revenue_id = models.AutoField(primary_key=True)
    revenue_estimates = models.CharField(max_length=200)
    conditional_grant = models.CharField(max_length=200)
    county = models.ForeignKey(Counties)
    equitable_share = models.CharField(max_length=200)
    total_revenue = models.CharField(max_length=200)
    year = models.CharField(max_length=20)

class Economic_Classification_Revenue(models.Model):
    economicrevenue_id = models.AutoField(primary_key=True)
    taxes_income_profits_capitalgains = models.CharField(max_length=250)
    taxes_property = models.CharField(max_length=250)
    taxes_vat = models.CharField(max_length=250)
    taxes_othergoodsandservices = models.CharField(max_length=250)
    taxes_internationaltrade_transactions = models.CharField(max_length=250)
    other_taxes_notelsewhereclasified = models.CharField(max_length=250)
    totaltax_revenue = models.CharField(max_length=250)
    socialsecuritycontributions = models.CharField(max_length=250)
    property_income = models.CharField(max_length=250)
    sale_goodsandservices = models.CharField(max_length=250)
    fines_penaltiesandforfeitures = models.CharField(max_length=250)
    repayments_domesticlending = models.CharField(max_length=250)
    other_receiptsnotelsewhereclassified = models.CharField(max_length=250)
    total_nontax_revenue = models.CharField(max_length=250)
    total = models.CharField(max_length=250)
    year = models.CharField(max_length=250)

class Outstanding_Debt_International_Organization(models.Model):
    outstanding_debt_id = models.AutoField(primary_key=True)
    ida = models.DecimalField(max_digits=15, decimal_places=2)
    eec_eib = models.DecimalField(max_digits=15, decimal_places=2)
    imf = models.DecimalField(max_digits=15, decimal_places=2)
    adf_adb = models.DecimalField(max_digits=15, decimal_places=2)
    commercial_banks = models.DecimalField(max_digits=15, decimal_places=2)
    others = models.DecimalField(max_digits=15, decimal_places=2)
    year = models.CharField(max_length=50)

class Outstanding_Debt_Lending_Country(models.Model):
    lending_country_id = models.AutoField(primary_key=True)
    germany = models.CharField(max_length=250)
    japan = models.CharField(max_length=250)
    france = models.CharField(max_length=250)
    usa = models.CharField(max_length=250)
    netherlands = models.CharField(max_length=250)
    denmark = models.CharField(max_length=250)
    finland = models.CharField(max_length=250)
    china = models.CharField(max_length=250)
    belgium = models.CharField(max_length=250)
    other = models.CharField(max_length=250)
    year = models.IntegerField()

class Excise_Revenue_Commodity(models.Model):
    excise_id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=100)
    beer = models.DecimalField(max_digits=65, decimal_places=2)
    cigarettes = models.DecimalField(max_digits=65, decimal_places=2)
    mineral_waters = models.DecimalField(max_digits=65, decimal_places=2)
    wines_spirits = models.DecimalField(max_digits=65, decimal_places=2)
    other_commodities = models.DecimalField(max_digits=65, decimal_places=2)
    total = models.DecimalField(max_digits=65, decimal_places=2)

# class Money_Banking_Index(models.Model):
#     institution_id = models.AutoField(primary_key=True)
#     financial_institution = models.CharField(max_length=100)
#
# class Money_Banking_Institutions(models.Model):
#     moneybanking_id = models.AutoField(primary_key=True)
#     county = models.ForeignKey(Counties)
#     subcounty_id = models.IntegerField()
#     institution = models.ForeignKey(Money_Banking_Index)
#     number = models.IntegerField()

class National_Government_Expenditure(models.Model):
    government_expenditure_id = models.AutoField(primary_key=True)
    acquisition_nonfinancial_assets = models.CharField(max_length=250)
    acquisition_financial_assets = models.CharField(max_length=250)
    loans_repayments = models.CharField(max_length=250)
    compensation_employees = models.CharField(max_length=250)
    goods_services = models.CharField(max_length=250)
    subsidies = models.CharField(max_length=250)
    interest = models.CharField(max_length=250)
    grants = models.CharField(max_length=250)
    other_expense = models.CharField(max_length=250)
    social_benefits = models.CharField(max_length=250)
    capital_grants = models.CharField(max_length=250)
    total = models.CharField(max_length=250)
    year = models.CharField(max_length=250)

class National_Government_Expenditure_Purpose(models.Model):
    purpose_id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=20)
    general_publicservices = models.CharField(max_length=250)
    public_debttransactions = models.CharField(max_length=250)
    transfers = models.CharField(max_length=250)
    defense = models.CharField(max_length=250)
    order_safety = models.CharField(max_length=250)
    economic_commercial_labor = models.CharField(max_length=250)
    agriculture = models.CharField(max_length=250)
    fuel_energy = models.CharField(max_length=250)
    mining_manufacturing_construction = models.CharField(max_length=250)
    transport = models.CharField(max_length=250)
    communication = models.CharField(max_length=250)
    other_industries = models.CharField(max_length=250)
    environmental_protection = models.CharField(max_length=250)
    housing_communityamenities = models.CharField(max_length=250)
    health = models.CharField(max_length=250)
    recreation_culture_religion = models.CharField(max_length=250)
    education = models.CharField(max_length=250)
    socialprotection = models.CharField(max_length=250)

class Cdf_Allocation_By_Constituency(models.Model):
    cdf_allocation_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    subcounty_id = models.IntegerField()
    cdf_amount = models.IntegerField()
    year = models.IntegerField()

class Expenditures_And_Revenues(models.Model):
    exp_rev_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    expenditure = models.BigIntegerField()
    revenue = models.BigIntegerField()
    year = models.IntegerField()

class National_Government_Allocation(models.Model):
    nat_govt_fund_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    allocated_funds = models.BigIntegerField()
    year = models.IntegerField()

class Allocation_And_Disbursement_Of_Funds_Social_Protection(models.Model):
    social_fund_id = models.AutoField(primary_key=True)
    no_of_beneficiaries = models.IntegerField()
    allocation = models.BigIntegerField()
    direct_cash_disbursement = models.BigIntegerField()
    social_fund_category = models.CharField(max_length=100)
    year = models.CharField(max_length=10)

class Economic_Analysis_Of_National_Government_Expenditure(models.Model):
    expenditure_id = models.AutoField(primary_key=True)
    expenditure = models.CharField(max_length=100)
    amount_in_millions = models.DecimalField(max_digits=65, decimal_places=10)
    year = models.CharField(max_length=100)

class Economic_Classification_Of_County_Government_Expenditure(models.Model):
    expenditure_id = models.AutoField(primary_key=True)
    county_government_expenditure = models.CharField(max_length=100)
    amount_in_millions = models.DecimalField(max_digits=65, decimal_places=10)
    year = models.CharField(max_length=100)

class Classification_National_Government_Expenditure_Function(models.Model):
    classification_id = models.AutoField(primary_key=True)
    government_function = models.CharField(max_length=100)
    recurrent_account_in_millions = models.DecimalField(max_digits=65, decimal_places=10)
    development_account_in_millions = models.DecimalField(max_digits=65, decimal_places=10)
    total_in_millions = models.DecimalField(max_digits=65, decimal_places=10)
    year = models.CharField(max_length=100)

class Statement_Of_National_Government_Operations(models.Model):
    operation_id = models.AutoField(primary_key=True)
    national_government_operation = models.CharField(max_length=100)
    amount_in_millions = models.DecimalField(max_digits=65, decimal_places=10)
    year = models.CharField(max_length=100)


class Expenditure_Functions_County_Governments (models.Model):
    cofog_id = models.AutoField(primary_key=True)
    general_public_services = models.DecimalField(max_digits=65, decimal_places=10)
    general_economic_affairs = models.DecimalField(max_digits=65, decimal_places=10)
    economic_affairs_agriculture = models.DecimalField(max_digits=65, decimal_places=10)
    economic_affairs_transport = models.DecimalField(max_digits=65, decimal_places=10)
    other_economic_affairs = models.DecimalField(max_digits=65, decimal_places=10)
    environmental_protection = models.DecimalField(max_digits=65, decimal_places=10)
    housing_community_ammenities = models.DecimalField(max_digits=65, decimal_places=10)
    health = models.DecimalField(max_digits=65, decimal_places=10)
    recreation_culture_religion = models.DecimalField(max_digits=65, decimal_places=10)
    education = models.DecimalField(max_digits=65, decimal_places=10)
    social_protection = models.DecimalField(max_digits=65, decimal_places=10)
    total = models.DecimalField(max_digits=65, decimal_places=10)
    year = models.CharField(max_length=20)

# class NationalGovtDevelopmentAndRecurrentExpenditureOnSocialServices(models.Model):
#     expenditure_id = models.AutoField(primary_key=True)
#     expenditure = models.CharField(max_length=100)
#     expenditure_type = models.CharField(max_length=100)
#     amount = models.DecimalField(max_digits=20, decimal_places=2)
#     year = models.IntegerField()
#






