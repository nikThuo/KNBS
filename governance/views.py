from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from governance.models import Crimes_Reported_To_Police_By_Command_Stations, Offence_By_Sex_And_Command_Stations, \
    Registered_Voters_By_County_And_By_Sex, Cases_Handled_By_Various_Courts, \
    Convicted_Prisoners_By_Type_Of_Offence_And_Sex, Environmental_Crimes_Reported_To_Nema, \
    Cases_Handled_By_Ethics_Commision, Cases_Forwarded_And_Action_Taken, Convicted_Prison_Population_By_Age_And_Sex, \
    Number_Of_Police_Prisons_And_Probation_Officers, Offences_Committed_Against_Morality, \
    Persons_Reported_To_Have_Committed_Homicide_By_Sex, Persons_Reported_To_Have_Committed_Robbery_And_Theft, \
    Daily_Average_Population_Of_Prisoners_By_Sex, Firearms_And_Ammunition_Recovered_Or_Surrendered, \
    Identity_Cards_Made_Processed_And_Collected, Magistrates_Judges_And_Practicing_Lawyers, \
    Murder_Cases_And_Convictions_Obtained_By_High_Court, Number_Of_Refugees_By_Age_And_Sex, Offenders_Serving, \
    Passports_Work_Permits_And_Foreigners_Registered, Persons_Reported_Committed_Offences_Related_To_Drugs, \
    Prison_Population_By_Sentence_Duration_And_Sex, Public_Assets_Traced_Recovered_And_Loss_Averted
from health.models import Counties, SubCounty

def governance(request):
    return render(request, template_name='knbs_bi/governance.html')

####################################Crimes_Reported_To_Police_By_Command_Stations####################################
#launch Page
def crimesReportedView(request):
    reported_crimes = Crimes_Reported_To_Police_By_Command_Stations.objects.all()

    crimes = []

    if reported_crimes:
        for crime in reported_crimes:
            county = Counties.objects.get(county_id=crime.county_id)
            c = {'id': crime.crime_id, 'county': county.county_name, 'crime':crime.crimes, 'year': crime.year}
            crimes.append(c)
            context = {'crimes': crimes}
    else:
        pass

    return render(request, 'knbs_bi/governance_crimes_reported_to_police_by_command_stations.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def crimesReported(request):
    reported_crimes = Crimes_Reported_To_Police_By_Command_Stations.objects.all()

    crimes = []

    if reported_crimes:
        for crime in reported_crimes:
            county = Counties.objects.get(county_id=crime.county_id)
            c = {'county': county.county_name, 'crime':crime.crimes, 'year': crime.year}
            crimes.append(c)
    else:
        pass

    return Response(crimes)


# Add View
def addCrimesReportedView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/governance_crimes_reported_to_police_by_command_stations_add.html', context)

# Edit View
def editCrimesReportedView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/governance_crimes_reported_to_police_by_command_stations_edit.html', context)

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addCrimesReported(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id

    crimes_add = Crimes_Reported_To_Police_By_Command_Stations(county_id=kaunti, crimes=request.data['crimes'],
                                                           year=request.data['year'])
    if crimes_add:
        crimes_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editCrimesReported(request):
    crimes_edit = Crimes_Reported_To_Police_By_Command_Stations.objects.get(crime_id=request.data['crime'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            crimes_edit.county_id = counties.county_id

    if 'crimes' in request.data:
        crimes_edit.crimes = request.data['crimes']

    if 'year' in request.data:
        crimes_edit.year = request.data['year']

    crimes_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

####################################Offence_By_Sex_And_Command_Stations####################################
#launch Page
def offenceSexView(request):
    offence_sex = Offence_By_Sex_And_Command_Stations.objects.all()

    offences = []

    if offence_sex:
        for offence in offence_sex:
            county = Counties.objects.get(county_id=offence.county_id)
            c = {'id': offence.offence_id, 'county': county.county_name, 'male': offence.male,
                 'female': offence.female, 'year': offence.year}
            offences.append(c)
            context = {'offences': offences}
    else:
        pass

    return render(request, 'knbs_bi/governance_offence_by_sex_and_command_stations.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def offenceSex(request):
    offence_sex = Offence_By_Sex_And_Command_Stations.objects.all()

    offences = []

    if offence_sex:
        for offence in offence_sex:
            county = Counties.objects.get(county_id=offence.county_id)
            c = {'county': county.county_name, 'male': offence.male,
                 'female': offence.female, 'year': offence.year}
            offences.append(c)
    else:
        pass

    return Response(offences)

# Add View
def addOffenceSexView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/governance_offence_by_sex_and_command_stations_add.html', context)

# Edit View
def editOffenceSexView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/governance_offence_by_sex_and_command_stations_edit.html', context)

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addOffenceSex(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id

    offence_add = Offence_By_Sex_And_Command_Stations(county_id=kaunti, male=request.data['male'], female=request.data['female'],
                                                           year=request.data['year'])
    if offence_add:
        offence_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editOffenceSex(request):
    offence_edit = Offence_By_Sex_And_Command_Stations.objects.get(offence_id=request.data['offence'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            offence_edit.county_id = counties.county_id

    if 'male' in request.data:
        offence_edit.male = request.data['male']

    if 'female' in request.data:
        offence_edit.female = request.data['female']

    if 'year' in request.data:
        offence_edit.year = request.data['year']

    offence_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)


####################################Registered_Voters_By_County_And_By_Sex####################################
#launch Page
def registeredVotersCountyView(request):
    registered_voters = Registered_Voters_By_County_And_By_Sex.objects.all()

    voters = []

    if registered_voters:
        for voter in registered_voters:
            county = Counties.objects.get(county_id=voter.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=voter.sub_counties_id)

            if subcounty:
                for sc in subcounty:
                    c = {'id': voter.voters_id, 'county': county.county_name, 'subcounty': sc.subcounty_name,
                        'reg_voter': voter.reg_voters, 'gender': voter.gender}
                    voters.append(c)
                    context = {'voters': voters}
    else:
        pass

    return render(request, 'knbs_bi/governance_registered_voters_by_county_and_by_sex.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def registeredVotersCounty(request):
    registered_voters = Registered_Voters_By_County_And_By_Sex.objects.all()

    voters = []

    if registered_voters:
        for voter in registered_voters:
            county = Counties.objects.get(county_id=voter.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=voter.sub_counties_id)

            if subcounty:
                for sc in subcounty:
                    c = {'county': county.county_name, 'subcounty': sc.subcounty_name,
                        'reg_voter': voter.reg_voters, 'gender': voter.gender}
                    voters.append(c)
    else:
        pass

    return Response(voters)

# Add View
def addRegisteredVotersCountyView(request):
    all_counties = Counties.objects.all()
    sub_county = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': sub_county}
    return render(request, 'knbs_bi/governance_registered_voters_by_county_and_by_sex_add.html', context)

# Edit View
def editRegisteredVotersCountyView(request):
    all_counties = Counties.objects.all()
    sub_county = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': sub_county}
    return render(request, 'knbs_bi/governance_registered_voters_by_county_and_by_sex_edit.html', context)

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addRegisteredVotersCounty(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])

    if counties and sub:
        kaunti = counties.county_id
        sub_kaunti = sub.subcounty_id

        offence_add = Registered_Voters_By_County_And_By_Sex(county_id=kaunti, sub_counties_id=sub_kaunti, reg_voters=request.data['voters'], gender=request.data['gender'])
        if offence_add:
            offence_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editRegisteredVotersCounty(request):
    offence_edit = Registered_Voters_By_County_And_By_Sex.objects.get(voters_id=request.data['voter_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            offence_edit.county_id = counties.county_id

    if 'sub_county' in request.data:
        sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])
        if sub:
            offence_edit.sub_counties_id = sub.subcounty_id

    if 'voters' in request.data:
        offence_edit.reg_voters = request.data['voters']

    if 'gender' in request.data:
        offence_edit.gender = request.data['gender']


    offence_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

####################################Cases_Handled_By_Various_Courts####################################
#launch Page
def casesVariousCourtsView(request):
    cases_courts = Cases_Handled_By_Various_Courts.objects.all()

    cases = []

    if cases_courts:
        for case in cases_courts:
            c = {'id': case.court_id, 'category': case.category, 'kadhis_court': case.kadhis_court, 'magistrate_court': case.magistrate_court,
                 'high_court': case.high_court, 'court_of_appeal': case.court_of_appeal, 'supreme_court': case.supreme_court, 'year':case.year}
            cases.append(c)
            context = {'cases': cases}
    else:
        pass

    return render(request, 'knbs_bi/governance_cases_handled_by_various_courts.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def casesVariousCourts(request):
    cases_courts = Cases_Handled_By_Various_Courts.objects.all()

    cases = []

    if cases_courts:
        for case in cases_courts:
            c = {'category': case.category, 'kadhis_court': case.kadhis_court, 'magistrate_court': case.magistrate_court,
                 'high_court': case.high_court, 'court_of_appeal': case.court_of_appeal, 'supreme_court': case.supreme_court, 'year':case.year}
            cases.append(c)
    else:
        pass

    return Response(cases)

####################################Convicted_Prisoners_By_Type_Of_Offence_And_Sex####################################
#launch Page
def prisonersOffencesexView(request):
    offence_sex = Convicted_Prisoners_By_Type_Of_Offence_And_Sex.objects.all()

    offences = []

    if offence_sex:
        for offence in offence_sex:
            c = {'id': offence.convicted_offence_type, 'offence': offence.offence, 'male': offence.male,
                 'female': offence.female, 'year':offence.year}
            offences.append(c)
            context = {'offences': offences}
    else:
        pass

    return render(request, 'knbs_bi/governance_convicted_prisoners_by_type_of_offence_and_sex.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def prisonersOffencesex(request):
    offence_sex = Convicted_Prisoners_By_Type_Of_Offence_And_Sex.objects.all()

    offences = []

    if offence_sex:
        for offence in offence_sex:
            c = {'offence': offence.offence, 'male': offence.male,
                 'female': offence.female, 'year':offence.year}
            offences.append(c)
    else:
        pass

    return Response(offences)

####################################Environmental_Crimes_Reported_To_Nema####################################
#launch Page
def environmentalCrimesView(request):
    env_crime = Environmental_Crimes_Reported_To_Nema.objects.all()

    crimes = []

    if env_crime:
        for crime in env_crime:
            c = {'id': crime.crime_id, 'type_of_case': crime.type_of_case, 'no_of_cases': crime.no_of_cases,
                 'year':crime.year}
            crimes.append(c)
            context = {'crimes': crimes}
    else:
        pass

    return render(request, 'knbs_bi/governance_environmental_crimes_reported_to_nema.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def environmentalCrimes(request):
    env_crime = Environmental_Crimes_Reported_To_Nema.objects.all()

    crimes = []

    if env_crime:
        for crime in env_crime:
            c = {'type_of_case': crime.type_of_case, 'no_of_cases': crime.no_of_cases,
                 'year':crime.year}
            crimes.append(c)
    else:
        pass

    return Response(crimes)

####################################Cases_Handled_By_Ethics_Commision####################################
#launch Page
def casesEACCView(request):
    cases_eacc = Cases_Handled_By_Ethics_Commision.objects.all()

    cases = []

    if cases_eacc:
        for case in cases_eacc:
            c = {'action': case.action, 'no_of_cases': case.no_cases,
                 'year':case.year}
            cases.append(c)
            context = {'cases': cases}
    else:
        pass

    return render(request, 'knbs_bi/governance_cases_handled_by_ethics_commision.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def casesEACC(request):
    cases_eacc = Cases_Handled_By_Ethics_Commision.objects.all()

    cases = []

    if cases_eacc:
        for case in cases_eacc:
            c = {'id': case.cases_handled_id, 'action': case.action, 'no_of_cases': case.no_cases,
                 'year':case.year}
            cases.append(c)
    else:
        pass

    return Response(cases)

####################################Cases_Forwarded_And_Action_Taken####################################
#launch Page
def casesForwardedActediew(request):
    cases_acted = Cases_Forwarded_And_Action_Taken.objects.all()

    cases = []

    if cases_acted:
        for case in cases_acted:
            c = {'id': case.action_id, 'action': case.action_taken, 'no_of_recommendations': case.no_of_recommendations,
                 'year':case.year}
            cases.append(c)
            context = {'cases': cases}
    else:
        pass

    return render(request, 'knbs_bi/governance_cases forwarded and action taken.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def casesForwardedActed(request):
    cases_acted = Cases_Forwarded_And_Action_Taken.objects.all()

    cases = []

    if cases_acted:
        for case in cases_acted:
            c = {'action': case.action_taken, 'no_of_recommendations': case.no_of_recommendations,
                 'year':case.year}
            cases.append(c)
    else:
        pass

    return Response(cases)

####################################Convicted_Prison_Population_By_Age_And_Sex####################################
#launch Page
def convictedPrisonAgeSexView(request):
    convited = Convicted_Prison_Population_By_Age_And_Sex.objects.all()

    convicts = []

    if convited:
        for convict in convited:
            c = {'id': convict.convict_population, 'category': convict.category, 'male': convict.male, 'female': convict.female,
                 'year':convict.year}
            convicts.append(c)
            context = {'convicts': convicts}
    else:
        pass

    return render(request, 'knbs_bi/governance_convicted_prison_population_by_age_and_sex.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def convictedPrisonAgeSex(request):
    convited = Convicted_Prison_Population_By_Age_And_Sex.objects.all()

    convicts = []

    if convited:
        for convict in convited:
            c = {'category': convict.category, 'male': convict.male, 'female': convict.female,
                 'year':convict.year}
            convicts.append(c)
    else:
        pass

    return Response(convicts)

####################################Number_Of_Police_Prisons_And_Probation_Officers####################################
#launch Page
def policePrisonsProbationView(request):
    ppp = Number_Of_Police_Prisons_And_Probation_Officers.objects.all()

    records = []

    if ppp:
        for record in ppp:
            c = {'id': record.category_id, 'category': record.category, 'male': record.male, 'female': record.female,
                 'year':record.year}
            records.append(c)
            context = {'records': records}
    else:
        pass

    return render(request, 'knbs_bi/governance_number_of_police_prisons_and_probation_officers.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def policePrisonsProbation(request):
    ppp = Number_Of_Police_Prisons_And_Probation_Officers.objects.all()

    records = []

    if ppp:
        for record in ppp:
            c = {'category': record.category, 'male': record.male, 'female': record.female,
                 'year':record.year}
            records.append(c)
    else:
        pass

    return Response(records)

####################################Offences Committed Against Morality####################################
#launch Page
def offenceMoralityView(request):
    morality = Offences_Committed_Against_Morality.objects.all()

    offences = []

    if morality:
        for offence in morality:
            c = {'id': offence.offences_commiited_against_morality_id, 'category': offence.category, 'male': offence.male, 'female': offence.female,
                 'year':offence.year}
            offences.append(c)
            context = {'offences': offences}
    else:
        pass

    return render(request, 'knbs_bi/governance_offences_committed_against_morality.html', context)

#launch Page
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def offenceMorality(request):
    morality = Offences_Committed_Against_Morality.objects.all()

    offences = []

    if morality:
        for offence in morality:
            c = {'category': offence.category, 'male': offence.male, 'female': offence.female,
                 'year':offence.year}
            offences.append(c)
    else:
        pass

    return Response(offences)

####################################Persons_Reported_To_Have_Committed_Homicide_By_Sex####################################
#launch Page
def homicideSexView(request):
    homicide_sex = Persons_Reported_To_Have_Committed_Homicide_By_Sex.objects.all()

    offences = []

    if homicide_sex:
        for offence in homicide_sex:
            c = {'id': offence.offence_id, 'offence': offence.offence, 'male': offence.male, 'female': offence.female,
                 'year':offence.year}
            offences.append(c)
            context = {'offences': offences}
    else:
        pass

    return render(request, 'knbs_bi/governance_persons_reported_to_have_committed_homicide_by_sex.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def homicideSex(request):
    homicide_sex = Persons_Reported_To_Have_Committed_Homicide_By_Sex.objects.all()

    offences = []

    if homicide_sex:
        for offence in homicide_sex:
            c = {'offence': offence.offence, 'male': offence.male, 'female': offence.female,
                 'year':offence.year}
            offences.append(c)
    else:
        pass

    return Response(offences)

####################################Persons_Reported_To_Have_Committed_Robbery_And_Theft####################################
#launch Page
def robberyTheftView(request):
    robebery_theft = Persons_Reported_To_Have_Committed_Robbery_And_Theft.objects.all()

    offences = []

    if robebery_theft:
        for offence in robebery_theft:
            c = {'id': offence.offence_id, 'offence': offence.offence, 'male': offence.male, 'female': offence.female,
                 'year':offence.year}
            offences.append(c)
            context = {'offences': offences}
    else:
        pass

    return render(request, 'knbs_bi/governance_persons_reported_to_have_committed_robbery_and_theft.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def robberyTheft(request):
    robebery_theft = Persons_Reported_To_Have_Committed_Robbery_And_Theft.objects.all()

    offences = []

    if robebery_theft:
        for offence in robebery_theft:
            c = {'offence': offence.offence, 'male': offence.male, 'female': offence.female,
                 'year':offence.year}
            offences.append(c)
    else:
        pass

    return Response(offences)

####################################Daily_Average_Population_Of_Prisoners_By_Sex####################################
#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def dailyAvearge(request):
    daily_avearge = Daily_Average_Population_Of_Prisoners_By_Sex.objects.all()

    averages = []

    if daily_avearge:
        for average in daily_avearge:
            c = {'category': average.category, 'male': average.male, 'female': average.female,
                 'year':average.year}
            averages.append(c)
    else:
        pass

    return Response(averages)

####################################Firearms_And_Ammunition_Recovered_Or_Surrendered####################################
#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def fireArms(request):
    ammunition = Firearms_And_Ammunition_Recovered_Or_Surrendered.objects.all()

    fireams = []

    if ammunition:
        for firearm in ammunition:
            c = {'category': firearm.category, 'rifles': firearm.rifles, 'pistols': firearm.pistols, 'toy_pistols': firearm.toy_pistols,
                 'ammunition': firearm.ammunition, 'year':firearm.year}
            fireams.append(c)
    else:
        pass

    return Response(fireams)

####################################Identity_Cards_Made_Processed_And_Collected####################################
#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def idCards(request):
    id_cards = Identity_Cards_Made_Processed_And_Collected.objects.all()

    cards = []

    if id_cards:
        for card in id_cards:
            county = Counties.objects.get(county_id=card.county_id)
            c = {'county': county.county_name, 'npr_apps_made': card.npr_apps_made, 'npr_ids_prod': card.npr_ids_prod, 'npr_ids_collected': card.npr_ids_collected,
                 'year':card.year}
            cards.append(c)
    else:
        pass

    return Response(cards)

####################################Magistrates_Judges_And_Practicing_Lawyers####################################
#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def courtStaff(request):
    court_staff = Magistrates_Judges_And_Practicing_Lawyers.objects.all()

    employees = []

    if court_staff:
        for employee in court_staff:
            c = {'category': employee.category, 'male': employee.male, 'female': employee.female, 'year': employee.year}
            employees.append(c)
    else:
        pass

    return Response(employees)

####################################Murder_Cases_And_Convictions_Obtained_By_High_Court####################################
#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def murderCases(request):
    murder_cases = Murder_Cases_And_Convictions_Obtained_By_High_Court.objects.all()

    cases = []

    if murder_cases:
        for case in murder_cases:
            c = {'court_station': case.court_station, 'registered_murder_cases': case.reg_murder_convictions_obtained_id, 'murder_convictions_obtained': case.murder_convictions_obtained,
                 'year': case.year}
            cases.append(c)
    else:
        pass

    return Response(cases)

####################################Number_Of_Refugees_By_Age_And_Sex####################################
#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def refugeeAgeSex(request):
    refugee_age_sex = Number_Of_Refugees_By_Age_And_Sex.objects.all()

    refugees = []

    if refugee_age_sex:
        for refugee in refugee_age_sex:
            c = {'children': refugee.children, 'adult': refugee.adult, 'gender': refugee.gender,
                 'year': refugee.year}
            refugees.append(c)
    else:
        pass

    return Response(refugees)

####################################Offenders_Serving####################################
#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def offendersServing(request):
    offenders_serving = Offenders_Serving.objects.all()

    offenders = []

    if offenders_serving:
        for offender in offenders_serving:
            c = {'offence': offender.offence, 'male': offender.male, 'female': offender.female, 'category': offender.category,
                 'year': offender.year}
            offenders.append(c)
    else:
        pass

    return Response(offenders)

####################################Passports_Work_Permits_And_Foreigners_Registered####################################
#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def passportPermits(request):
    passport_permits = Passports_Work_Permits_And_Foreigners_Registered.objects.all()

    passports = []

    if passport_permits:
        for passport in passport_permits:
            c = {'passport_issued': passport.passport_issued, 'foreign_nat_reg': passport.foreign_nat_reg, 'work_permit_issued': passport.work_permit_issued,
                 'work_permit_ren': passport.work_permit_ren, 'year': passport.year}
            passports.append(c)
    else:
        pass

    return Response(passports)

####################################Persons_Reported_Committed_Offences_Related_To_Drugs####################################
#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def personsReported(request):
    persons_reported = Persons_Reported_Committed_Offences_Related_To_Drugs.objects.all()

    persons = []

    if persons_reported:
        for person in persons_reported:
            c = {'offence': person.offence, 'male': person.male, 'female': person.female, 'year': person.year}
            persons.append(c)
    else:
        pass

    return Response(persons)

####################################Prison_Population_By_Sentence_Duration_And_Sex####################################
#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def prisonPopulation(request):
    prison_population = Prison_Population_By_Sentence_Duration_And_Sex.objects.all()

    population = []

    if prison_population:
        for pop in prison_population:
            c = {'category': pop.category, 'male': pop.male, 'female': pop.female, 'year': pop.year}
            population.append(c)
    else:
        pass

    return Response(population)

####################################Public_Assets_Traced_Recovered_And_Loss_Averted####################################
#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def publicAssets(request):
    public_assets = Public_Assets_Traced_Recovered_And_Loss_Averted.objects.all()

    assets = []

    if public_assets:
        for asset in public_assets:
            c = {'public_assets_traced': asset.public_assets_traced, 'public_assets_recovered': asset.public_assets_recovered, 'loss_averted': asset.loss_averted,
                 'year': asset.year}
            assets.append(c)
    else:
        pass

    return Response(assets)