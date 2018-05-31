
from django.db import models

# Create your models here.
from health.models import Counties


class Registered_Voters_By_County_And_By_Sex(models.Model):
    voters_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    sub_counties_id = models.IntegerField()
    reg_voters = models.IntegerField()
    gender = models.CharField(max_length=100)

class Offence_By_Sex_And_Command_Stations(models.Model):
    offence_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    male = models.IntegerField()
    female = models.IntegerField()
    year = models.IntegerField()

class Crimes_Reported_To_Police_By_Command_Stations(models.Model):
    crime_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    crimes = models.IntegerField()
    year = models.IntegerField()

class Cases_Handled_By_Various_Courts(models.Model):
    court_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    kadhis_court = models.IntegerField()
    magistrate_court = models.IntegerField()
    high_court = models.IntegerField()
    court_of_appeal = models.IntegerField()
    supreme_court = models.IntegerField()
    year = models.IntegerField()

class Convicted_Prisoners_By_Type_Of_Offence_And_Sex(models.Model):
    convicted_offence_type = models.AutoField(primary_key=True)
    offence = models.CharField(max_length=100)
    male = models.IntegerField()
    female = models.IntegerField()
    year = models.IntegerField()

class Environmental_Crimes_Reported_To_Nema(models.Model):
    crime_id = models.AutoField(primary_key=True)
    type_of_case = models.CharField(max_length=100)
    no_of_cases = models.IntegerField()
    year = models.IntegerField()

class Cases_Handled_By_Ethics_Commision(models.Model):
    cases_handled_id = models.AutoField(primary_key=True)
    action = models.CharField(max_length=100)
    no_cases = models.IntegerField()
    year = models.CharField(max_length=100)

class Cases_Forwarded_And_Action_Taken(models.Model):
    action_id = models.AutoField(primary_key=True)
    action_taken = models.CharField(max_length=100)
    no_of_recommendations = models.IntegerField()
    year = models.IntegerField()

class Convicted_Prison_Population_By_Age_And_Sex(models.Model):
    convict_population = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    male = models.IntegerField()
    female = models.IntegerField()
    year = models.IntegerField()

class Number_Of_Police_Prisons_And_Probation_Officers(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    male = models.IntegerField()
    female = models.IntegerField()
    year = models.IntegerField()

class Offences_Committed_Against_Morality(models.Model):
    offences_commiited_against_morality_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    male = models.IntegerField()
    female = models.IntegerField()
    year = models.IntegerField()

class Persons_Reported_To_Have_Committed_Homicide_By_Sex(models.Model):
    offence_id = models.AutoField(primary_key=True)
    offence = models.CharField(max_length=100)
    male = models.IntegerField()
    female = models.IntegerField()
    year = models.IntegerField()

class Persons_Reported_To_Have_Committed_Robbery_And_Theft(models.Model):
    offence_id = models.AutoField(primary_key=True)
    offence = models.CharField(max_length=100)
    male = models.IntegerField()
    female = models.IntegerField()
    year = models.IntegerField()

class Daily_Average_Population_Of_Prisoners_By_Sex(models.Model):
    daily_population_prisoners_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    male = models.IntegerField()
    female = models.IntegerField()
    year = models.IntegerField()

class Firearms_And_Ammunition_Recovered_Or_Surrendered(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    rifles = models.IntegerField()
    pistols = models.IntegerField()
    toy_pistols = models.IntegerField()
    ammunition = models.IntegerField()
    year = models.IntegerField()

class Identity_Cards_Made_Processed_And_Collected(models.Model):
    nprs_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    npr_apps_made = models.IntegerField()
    npr_ids_prod = models.IntegerField()
    npr_ids_collected = models.IntegerField()
    year = models.IntegerField()

class Magistrates_Judges_And_Practicing_Lawyers(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    male = models.IntegerField()
    female = models.IntegerField()
    year = models.IntegerField()

class Murder_Cases_And_Convictions_Obtained_By_High_Court(models.Model):
    reg_murder_convictions_obtained_id = models.AutoField(primary_key=True)
    court_station = models.CharField(max_length=100)
    registered_murder_cases = models.IntegerField()
    murder_convictions_obtained = models.IntegerField()
    year = models.IntegerField()

class Number_Of_Refugees_By_Age_And_Sex(models.Model):
    category_id = models.AutoField(primary_key=True)
    children = models.IntegerField()
    adult = models.IntegerField()
    gender = models.CharField(max_length=100)
    year = models.IntegerField()

class Offenders_Serving(models.Model):
    offence_id = models.AutoField(primary_key=True)
    offence = models.CharField(max_length=100)
    male = models.IntegerField()
    female = models.IntegerField()
    category = models.CharField(max_length=100)
    year = models.IntegerField()

class Passports_Work_Permits_And_Foreigners_Registered(models.Model):
    passports_permits_registered_foreigners_id = models.AutoField(primary_key=True)
    passport_issued = models.IntegerField()
    foreign_nat_reg = models.IntegerField()
    work_permit_issued = models.IntegerField()
    work_permit_ren = models.IntegerField()
    year = models.IntegerField()

class Persons_Reported_Committed_Offences_Related_To_Drugs(models.Model):
    offence_id = models.AutoField(primary_key=True)
    offence = models.CharField(max_length=100)
    male = models.IntegerField()
    female = models.IntegerField()
    year = models.IntegerField()

class Prison_Population_By_Sentence_Duration_And_Sex(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    male = models.IntegerField()
    female = models.IntegerField()
    year = models.IntegerField()

class Public_Assets_Traced_Recovered_And_Loss_Averted(models.Model):
    category_id = models.AutoField(primary_key=True)
    public_assets_traced = models.DecimalField(max_digits=10, decimal_places=2)
    public_assets_recovered = models.DecimalField(max_digits=10, decimal_places=2)
    loss_averted = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()

class Participation_In_Key_Decision_Making_Positions_By_Sex(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    female = models.IntegerField()
    male = models.IntegerField()
    percentage = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()

class Women_Groups_Registration_Contributions_Uwezo_Funds(models.Model):
    group_id = models.AutoField(primary_key=True)
    no_of_beneficiaries = models.IntegerField()
    uwezo_fund_disbursed = models.IntegerField()
    year = models.CharField(max_length=10)

class Women_Groups_Registration_Cont_Women_Enterprise_Fund(models.Model):
    group_id = models.AutoField(primary_key=True)
    no_of_beneficiaries = models.IntegerField()
    women_enterprise_fund = models.IntegerField()
    year = models.CharField(max_length=10)

class Women_Groups_Registration_Contributions_Women_Groups(models.Model):
    group_id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    membership = models.IntegerField()
    group_contributions = models.BigIntegerField()
    year = models.CharField(max_length=10)

############################################Governance Gender Fact Sheet############################################

class Experienceof_Domestic_Violence_By_Age(models.Model):
    woman_id = models.AutoField(primary_key=True)
    age = models.CharField(max_length=10)
    percentage_experienced_physical_violence = models.DecimalField(max_digits=10, decimal_places=1)
    percentage_experienced_sexual_violence = models.DecimalField(max_digits=10, decimal_places=1)
    percentage_experienced_physical_and_sexual_violence = models.DecimalField(max_digits=10, decimal_places=1)
    gender = models.CharField(max_length=10)

class Experienceof_Domestic_Violence_By_Marital_Success(models.Model):
    woman_id = models.AutoField(primary_key=True)
    marital_status = models.CharField(max_length=30)
    percentage_experienced_physical_violence = models.DecimalField(max_digits=10, decimal_places=1)
    percentage_experienced_sexual_violence = models.DecimalField(max_digits=10, decimal_places=1)
    percentage_experienced_physical_and_sexual_violence = models.DecimalField(max_digits=10, decimal_places=1)
    gender = models.CharField(max_length=10)

class Experienceof_Domestic_Violence_By_Residence(models.Model):
    woman_id = models.AutoField(primary_key=True)
    residence = models.CharField(max_length=10)
    percentage_experienced_physical_violence = models.DecimalField(max_digits=10, decimal_places=1)
    percentage_experienced_sexual_violence = models.DecimalField(max_digits=10, decimal_places=1)
    percentage_experienced_physical_and_sexual_violence = models.DecimalField(max_digits=10, decimal_places=1)
    gender = models.CharField(max_length=10)

class Knowledge_And_Prevalence_Of_Female_Circumcision (models.Model):
    woman_id = models.AutoField(primary_key=True)
    age = models.CharField(max_length=10)
    percentage_women_heard_of_FC = models.DecimalField(max_digits=10, decimal_places=1)
    percentage_women_not_heard_of_FC = models.DecimalField(max_digits=10, decimal_places=1)
    year = models.CharField(max_length=10)

class Members_Of_NationalAssembly_and_Senators(models.Model):
    woman_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=20)
    women = models.IntegerField()
    men = models.IntegerField()
    total = models.IntegerField()
    women_percentage = models.DecimalField(max_digits=10, decimal_places=1)

class Persons_Reported_ToHave_Committed_Defilement(models.Model):
    persons_id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    proportion = models.DecimalField(max_digits=10, decimal_places=1)
    gender = models.CharField(max_length=20)
    year = models.IntegerField()

class Persons_Reported_ToHave_Committed_Rape(models.Model):
    persons_id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    proportion = models.DecimalField(max_digits=10, decimal_places=1)
    gender = models.CharField(max_length=20)
    year = models.IntegerField()

class Total_Prisoners_Committed_For_Debt_BySex(models.Model):
    persons_id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    proportion = models.DecimalField(max_digits=10, decimal_places=1)
    gender = models.CharField(max_length=20)
    year = models.IntegerField()

class Prevalence_Female_Circumcision_And_Type(models.Model):
    persons_id = models.AutoField(primary_key=True)
    age = models.CharField(max_length=20)
    cut_no_flesh_removed = models.DecimalField(max_digits=10, decimal_places=1)
    cut_flesh_removed = models.DecimalField(max_digits=10, decimal_places=1)
    sewn_closed = models.DecimalField(max_digits=10, decimal_places=1)
    others = models.DecimalField(max_digits=10, decimal_places=1)
    percentage_women_circumcised = models.DecimalField(max_digits=10, decimal_places=1)




