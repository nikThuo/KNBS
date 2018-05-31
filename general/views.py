from django.db.models import Max
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from administrative.models import Unit
from agriculture.models import Land_Potential, PriceToProducersForMeatMilk, Gross_Market_Production, Cooperatives, \
    Chemical_Med_Feed_Input, Irrigation_Schemes, TotalShareCapital, ValueOfAgriculturalInputs
from building_and_construction.models import Amount
from education.models import TotalSecondarySchoolEnrollmentByYear, Csa_PrimarySchoolsByCategoryAndSubCounty, \
    Csa_SecondaryEnrolmentAndAccessIndicators, Csa_StudentEnrolmentInYouthPolytechnics, Csa_TeacherTrainingColleges, \
    Csa_EcdeCentresByCategoryAndSubCounty, Csa_PrimaryEnrolmentAndAccessIndicators, \
    Csa_AdultEducationCentresBySubCounty, Csa_AdultEducationEnrolmentBySexAndSubcounty, \
    Csa_AdultEducationProficiencyTestResults, Csa_PrimarySchoolEnrollmentByClassSexAndSubCounty, \
    Csa_YouthPolytechnicsByCategoryAndSubCounty
from finance.models import County_Revenue, County_Expenditure, County_Budget_Allocation, Cdf_Allocation, \
    Excise_Revenue_Commodity, Outstanding_Debt_Lending_Country
from general.models import Request_Dataset
from governance.models import Crimes_Reported_To_Police_By_Command_Stations, Offence_By_Sex_And_Command_Stations, \
    Registered_Voters_By_County_And_By_Sex, Cases_Handled_By_Various_Courts, \
    Convicted_Prisoners_By_Type_Of_Offence_And_Sex, Environmental_Crimes_Reported_To_Nema, \
    Cases_Handled_By_Ethics_Commision, Cases_Forwarded_And_Action_Taken, Convicted_Prison_Population_By_Age_And_Sex, \
    Number_Of_Police_Prisons_And_Probation_Officers, Offences_Committed_Against_Morality, \
    Persons_Reported_To_Have_Committed_Homicide_By_Sex, Persons_Reported_To_Have_Committed_Robbery_And_Theft
from health.models import Immunization_Rate, County_Outpatient_Morbidity_Below_Five, CountyOutpatientMorbidityAboveFive, \
    HealthFacilitiesByOwnershipOfHealthFacilities, Facilities, HospitalBedsAndCots, Nhif_Resources, Nhif_Members, \
    RegisteredMedicalPersonnel, Sectors, Registered_Active_Nhif_Members_By_County
from labour.models import Employment_Public_Sector
from land_and_climate.models import Surface_Area_By_Category, Temperature, Rainfall, Topography_Altitude
from political.models import Units
from population.models import PopulationProjectionsBySelectedAgeGroup, PopulationProjectionsBySpecialAgeGroups
from transport_and_communication.models import Road_Coverage_By_Type_And_Distance
from vital_statistics.models import Births_And_Deaths_By_Sex, ExpectedAndRegisteredBirthsAndDeaths, \
    Top_Ten_Death_Causes

@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def requestDataSet(request):
    dataset_add = Request_Dataset(name=request.data['name'], email=request.data['email'], dataset=request.data['dataset'], year=request.data['year'])

    if dataset_add:
        dataset_add.save()
        response = {"Successfully Added"}
    return Response(response)

@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def getCount(request):
    response = []

    if request.data['sector'] == 'Governance':
        sector = Sectors.objects.filter(sector_name='Governance').count()
        response = {'sector': sector}
    elif request.data['sector'] == 'Agriculture':
        sector = Sectors.objects.filter(sector_name='Agriculture').count()
        response = {'sector': sector}
    elif request.data['sector'] == 'Political and Administrative Units':
        sector = Sectors.objects.filter(sector_name='Political and Administrative Units').count()
        response = {'sector': sector}
    elif request.data['sector'] == 'Education':
        sector = Sectors.objects.filter(sector_name='Education').count()
        response = {'sector': sector}
    elif request.data['sector'] == 'Public Finance':
        sector = Sectors.objects.filter(sector_name='Public Finance').count()
        response = {'sector': sector}
    elif request.data['sector'] == 'Public Health':
        sector = Sectors.objects.filter(sector_name='Public Health').count()
        response = {'sector': sector}
    elif request.data['sector'] == 'Labour':
        sector = Sectors.objects.filter(sector_name='Labour').count()
        response = {'sector': sector}
    elif request.data['sector'] == 'Population and Vital Statistics':
        sector = Sectors.objects.filter(sector_name='Population and Vital Statistics').count()
        response = {'sector': sector}
    elif request.data['sector'] == 'Trade and Commerce':
        sector = Sectors.objects.filter(sector_name='Population and Vital Statistics').count()
        response = {'sector': sector}
    elif request.data['sector'] == 'Energy':
        sector = Sectors.objects.filter(sector_name='Population and Vital Statistics').count()
        response = {'sector': sector}

    return Response(response)

@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def getYear(request):
    response = []

    if request.data['year'] == 'county_revenue':
        res = County_Revenue.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'county_expenditure':
        res = County_Expenditure.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'county_budget':
        res = County_Budget_Allocation.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'cdf_allocation':
        res = Cdf_Allocation.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'excise_revenue':
        res = Excise_Revenue_Commodity.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'lending_country':
        res = Outstanding_Debt_Lending_Country.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'births_deaths':
        res = Births_And_Deaths_By_Sex.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'exp_births_deaths':
        res = ExpectedAndRegisteredBirthsAndDeaths.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'death_causes':
        res = Top_Ten_Death_Causes.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'selected_agegroup':
        res = PopulationProjectionsBySelectedAgeGroup.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'special_agegroup':
        res = PopulationProjectionsBySpecialAgeGroups.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}

    elif request.data['year'] == 'county_sse':
        res = TotalSecondarySchoolEnrollmentByYear.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'county_pscs':
        res = Csa_PrimarySchoolsByCategoryAndSubCounty.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'county_seai':
        res = Csa_SecondaryEnrolmentAndAccessIndicators.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'county_pecss':
        res = Csa_PrimarySchoolEnrollmentByClassSexAndSubCounty.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'county_seyp':
        res = Csa_StudentEnrolmentInYouthPolytechnics.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'county_ttc':
        res = Csa_TeacherTrainingColleges.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'county_eccs':
        res = Csa_EcdeCentresByCategoryAndSubCounty.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'county_ypcs':
        res = Csa_YouthPolytechnicsByCategoryAndSubCounty.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'county_peai':
        res = Csa_PrimaryEnrolmentAndAccessIndicators.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'county_aecs':
        res = Csa_AdultEducationCentresBySubCounty.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'county_aeess':
        res = Csa_AdultEducationEnrolmentBySexAndSubcounty.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'county_aeptr':
        res = Csa_AdultEducationProficiencyTestResults.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'county_ficrcuoy':
        res = Immunization_Rate.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'county_ompb5ya':
        res = County_Outpatient_Morbidity_Below_Five.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'county_ompa5ya':
        res = CountyOutpatientMorbidityAboveFive.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'county_rmp':
        res = RegisteredMedicalPersonnel.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'county_hfo':
        res = HealthFacilitiesByOwnershipOfHealthFacilities.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'county_hf':
        res = Facilities.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'county_hbc':
        res = HospitalBedsAndCots.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'active_nhif_members':
        res = Registered_Active_Nhif_Members_By_County.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'nhif_resources':
        res = Nhif_Resources.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'nhif_members':
        res = Nhif_Members.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}

    elif request.data['year'] == 'county_cppcs':
        res = Crimes_Reported_To_Police_By_Command_Stations.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'county_oscs':
        res = Offence_By_Sex_And_Command_Stations.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'county_rvcs':
        res = Registered_Voters_By_County_And_By_Sex.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'cases_handled':
        res = Cases_Handled_By_Various_Courts.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'convicted_pyos':
        res = Convicted_Prisoners_By_Type_Of_Offence_And_Sex.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'environmental_crimes':
        res = Environmental_Crimes_Reported_To_Nema.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'cases_hadled_eacc':
        res = Cases_Handled_By_Ethics_Commision.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'cases_action_taken':
        res = Cases_Forwarded_And_Action_Taken.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'convicted_ppas':
        res = Convicted_Prison_Population_By_Age_And_Sex.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'number_pppo':
        res = Number_Of_Police_Prisons_And_Probation_Officers.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'offences_cam':
        res = Offences_Committed_Against_Morality.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'persons_rhchs':
        res = Persons_Reported_To_Have_Committed_Homicide_By_Sex.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'persons_rhcrt':
        res = Persons_Reported_To_Have_Committed_Robbery_And_Theft.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}

    elif request.data['year'] == 'employment_ps':
        res = Employment_Public_Sector.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}

    elif request.data['year'] == 'county_au':
        res = Unit.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}

    elif request.data['year'] == 'county_pu':
        res = Units.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}

    elif request.data['year'] == 'trade_cu':
        res = Units.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}

    elif request.data['year'] == 'county_lp':
        res = Land_Potential.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'price_producers':
        res = PriceToProducersForMeatMilk.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'chem_feed':
        res = Chemical_Med_Feed_Input.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'coop':
        res = Cooperatives.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'gross_market':
        res = Gross_Market_Production.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'irrigation_scheme':
        res = Irrigation_Schemes.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'total_share':
        res = TotalShareCapital.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'agricultural_inputs':
        res = ValueOfAgriculturalInputs.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}

    elif request.data['year'] == 'surface_area':
        res = Surface_Area_By_Category.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'temperature':
        res = Temperature.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'rainfall':
        res = Rainfall.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}
    elif request.data['year'] == 'altitude':
        res = Topography_Altitude.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}

    elif request.data['year'] == 'coverage':
        res = Road_Coverage_By_Type_And_Distance.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}

    elif request.data['year'] == 'build_amount':
        res = Amount.objects.all()
        year = res.aggregate(Max('year'))
        response = {'year': year}

    return Response(response)


