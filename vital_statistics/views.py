from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from health.models import Counties
from population.models import PopulationProjectionsBySelectedAgeGroup, PopulationProjectionsBySpecialAgeGroups
from vital_statistics.models import Births_And_Deaths_By_Sex, Death_Causes, ExpectedAndRegisteredBirthsAndDeaths, \
    Top_Ten_Death_Causes

def vital_statistics(request):
    return render(request, template_name='knbs_bi/vital_statistics.html')


####################################Births_And_Deaths_By_Sex####################################
#Launch Page
def sexBirthsDeathsView(request):
    births_deaths = Births_And_Deaths_By_Sex.objects.all()

    incidences = []

    if births_deaths:
        for incidence in births_deaths:
            county = Counties.objects.get(county_id=incidence.county_id)

            c = {'id': incidence.count_id, 'county': county.county_name, 'births': incidence.births, 'deaths': incidence.deaths,
                 'gender': incidence.gender, 'year': incidence.year}
            incidences.append(c)
            context = {'incidences': incidences}
    else:
        pass

    return render(request, 'knbs_bi/vital_statistics_births_and_deaths_by_sex.html', context)


@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def sexBirthsDeaths(request):
    births_deaths = Births_And_Deaths_By_Sex.objects.all()

    incidences = []

    if births_deaths:
        for incidence in births_deaths:
            county = Counties.objects.get(county_id=incidence.county_id)

            c = {'county': county.county_name, 'births': incidence.births, 'deaths': incidence.deaths,
                 'gender': incidence.gender, 'year': incidence.year}
            incidences.append(c)
    else:
        pass

    return Response(incidences)

# Add View
def addSexBirthsDeathsView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/vital_statistics_births_and_deaths_by_sex_add.html', context)

# Edit View
def editSexBirthsDeathsView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/vital_statistics_births_and_deaths_by_sex_edit.html', context)

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addSexBirthsDeaths(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id

    births_deaths_add = Births_And_Deaths_By_Sex(county_id=kaunti, births=request.data['births'], deaths=request.data['deaths'], gender=request.data['gender'],
                                                           year=request.data['year'])
    if births_deaths_add:
        births_deaths_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editSexBirthsDeaths(request):
    births_deaths_edit = Births_And_Deaths_By_Sex.objects.get(count_id=request.data['count'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            births_deaths_edit.county_id = counties.county_id

    if 'births' in request.data:
        births_deaths_edit.births = request.data['births']

    if 'deaths' in request.data:
        births_deaths_edit.deaths = request.data['deaths']

    if 'gender' in request.data:
        births_deaths_edit.gender = request.data['gender']

    if 'year' in request.data:
        births_deaths_edit.year = request.data['year']

    births_deaths_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)


####################################ExpectedAndRegisteredBirthsAndDeaths####################################
#Launch Page
def expectedBirthsDeathsView(request):
    births_deaths = ExpectedAndRegisteredBirthsAndDeaths.objects.all()

    expectations = []

    if births_deaths:
        for expectation in births_deaths:
            county = Counties.objects.get(county_id=expectation.county_id)

            c = {'id': expectation.count_id, 'county': county.county_name, 'coverage': expectation.coverage, 'births': expectation.births,
                 'deaths': expectation.deaths, 'year': expectation.year}
            expectations.append(c)
            context = {'expectations': expectations}
    else:
        pass

    return render(request, 'knbs_bi/vital_statistics_expected_and_registered_births_and_deaths.html', context)

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def expectedBirthsDeaths(request):
    births_deaths = ExpectedAndRegisteredBirthsAndDeaths.objects.all()

    expectations = []

    if births_deaths:
        for expectation in births_deaths:
            county = Counties.objects.get(county_id=expectation.county_id)

            c = {'county': county.county_name, 'coverage': expectation.coverage, 'births': expectation.births,
                 'deaths': expectation.deaths, 'year': expectation.year}
            expectations.append(c)
    else:
        pass

    return Response(expectations)

# Add View
def addExpectedBirthsDeathsView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/vital_statistics_expected_and_registered_births_and_deaths_add.html', context)

# Edit View
def editExpectedBirthsDeathsView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/vital_statistics_expected_and_registered_births_and_deaths_edit.html', context)

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addExpectedBirthsDeaths(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id

    births_deaths_add = ExpectedAndRegisteredBirthsAndDeaths(county_id=kaunti, coverage=request.data['coverage'], births=request.data['births'],
                                                             deaths=request.data['deaths'], year=request.data['year'])
    if births_deaths_add:
        births_deaths_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editExpectedBirthsDeaths(request):
    births_deaths_edit = ExpectedAndRegisteredBirthsAndDeaths.objects.get(count_id=request.data['count'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            births_deaths_edit.county_id = counties.county_id

    if 'coverage' in request.data:
        births_deaths_edit.coverage = request.data['coverage']

    if 'births' in request.data:
        births_deaths_edit.births = request.data['births']

    if 'deaths' in request.data:
        births_deaths_edit.deaths = request.data['deaths']

    if 'year' in request.data:
        births_deaths_edit.year = request.data['year']

    births_deaths_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

####################################Death Causes####################################
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def deathCauses(request):
    death_causes = Death_Causes.objects.all()

    causes = []

    if death_causes:
        for cause in death_causes:
            c = {'causes': cause.cause}
            causes.append(c)
    else:
        pass

    return Response(causes)

####################################Top_Ten_Death_Causes_2014####################################
#Launch Page
def topTenDeathCausesView(request):
    top_ten = Top_Ten_Death_Causes.objects.all()

    causes = []

    if top_ten:
        for cause in top_ten:
            county = Counties.objects.get(county_id=cause.county_id)
            cause_name = Death_Causes.objects.get(cause_id=cause.cause_id)

            c = {'id': cause.count_id, 'county': county.county_name, 'cause': cause_name.cause, 'percent': cause.percent,
                 'total': cause.total, 'year': cause.year}
            causes.append(c)
            context = {'causes': causes}
    else:
        pass

    return render(request, 'knbs_bi/vital_statistics_top_ten_death_causes_2014.html', context)


@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def topTenDeathCauses(request):
    top_ten = Top_Ten_Death_Causes.objects.all()

    causes = []

    if top_ten:
        for cause in top_ten:
            county = Counties.objects.get(county_id=cause.county_id)
            cause_name = Death_Causes.objects.get(cause_id=cause.cause_id)

            c = {'county': county.county_name, 'cause': cause_name.cause, 'percent': cause.percent,
                 'total': cause.total, 'year': cause.year}
            causes.append(c)
    else:
        pass

    return Response(causes)


# Add View
def addTopTenDeathCausesView(request):
    all_counties = Counties.objects.all()
    cause_name = Death_Causes.objects.all()
    context = {'counties': all_counties, 'causes': cause_name}
    return render(request, 'knbs_bi/vital_statistics_top_ten_death_causes_2014_add.html', context)


# Edit View
def editTopTenDeathCausesView(request):
    all_counties = Counties.objects.all()
    cause_name = Death_Causes.objects.all()
    context = {'counties': all_counties, 'causes': cause_name}
    return render(request, 'knbs_bi/vital_statistics_top_ten_death_causes_2014_edit.html', context)


# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addTopTenDeathCauses(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    cause_name = Death_Causes.objects.get(cause=request.data['cause'])

    if counties and cause_name:
        kaunti = counties.county_id
        reason = cause_name.cause_id

        top_ten_add = Top_Ten_Death_Causes(county_id=kaunti, cause_id=reason,
                                                             percent=request.data['percent'],
                                                             total=request.data['total'], year=request.data['year'])
    if top_ten_add:
        top_ten_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editTopTenDeathCauses(request):
    top_ten_edit = Top_Ten_Death_Causes.objects.get(count_id=request.data['count'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            top_ten_edit.county_id = counties.county_id

    if 'cause' in request.data:
        cause_name = Death_Causes.objects.get(cause=request.data['cause'])
        if cause_name:
            top_ten_edit.cause_id = cause_name.cause_id

    if 'percent' in request.data:
        top_ten_edit.percent = request.data['percent']

    if 'total' in request.data:
        top_ten_edit.total = request.data['total']

    if 'year' in request.data:
        top_ten_edit.year = request.data['year']

    top_ten_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

####################################PopulationProjectionsBySelectedAgeGroup####################################
#Launch Page
def populationSelectedAgeGroupView(request):
    selected_age_group = PopulationProjectionsBySelectedAgeGroup.objects.all()

    projections = []

    if selected_age_group:
        for projection in selected_age_group:
            county = Counties.objects.get(county_id=projection.county_id)

            c = {'id': projection.population_projection_id, 'county': county.county_name, 'range_0_4': projection.range_0_4, 'range_5_9': projection.range_5_9,
                 'range_10_14': projection.range_10_14, 'range_15_19': projection.range_15_19, 'range_20_24': projection.range_20_24, 'range_25_29': projection.range_25_29,
                 'range_30_34': projection.range_30_34, 'range_35_39': projection.range_35_39, 'range_40_44': projection.range_40_44, 'range_45_49': projection.range_45_49,
                 'range_50_54': projection.range_50_54, 'range_55_59': projection.range_55_59, 'range_60_64': projection.range_60_64, 'range_65_69': projection.range_65_69,
                 'range_70_74': projection.range_70_74, 'range_75_79': projection.range_75_79, 'range_80_plus': projection.range_80_plus,
                 'gender': projection.gender, 'year': projection.year}
            projections.append(c)
            context = {'projections': projections}
    else:
        pass

    return render(request, 'knbs_bi/population_projections_by_selected_age_group.html', context)


@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def populationSelectedAgeGroup(request):
    selected_age_group = PopulationProjectionsBySelectedAgeGroup.objects.all()

    projections = []

    if selected_age_group:
        for projection in selected_age_group:
            county = Counties.objects.get(county_id=projection.county_id)

            c = {'county': county.county_name, 'range_0_4': projection.range_0_4, 'range_5_9': projection.range_5_9,
                 'range_10_14': projection.range_10_14, 'range_15_19': projection.range_15_19, 'range_20_24': projection.range_20_24, 'range_25_29': projection.range_25_29,
                 'range_30_34': projection.range_30_34, 'range_35_39': projection.range_35_39, 'range_40_44': projection.range_40_44, 'range_45_49': projection.range_45_49,
                 'range_50_54': projection.range_50_54, 'range_55_59': projection.range_55_59, 'range_60_64': projection.range_60_64, 'range_65_69': projection.range_65_69,
                 'range_70_74': projection.range_70_74, 'range_75_79': projection.range_75_79, 'range_80_plus': projection.range_80_plus,
                 'gender': projection.gender, 'year': projection.year}
            projections.append(c)
    else:
        pass

    return Response(projections)


# Add View
def addPopulationSelectedAgeGroupView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/population_projections_by_selected_age_group_add.html', context)


# Edit View
def editPopulationSelectedAgeGroupView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/population_projections_by_selected_age_group_edit.html', context)

# View More
def viewPopulationSelectedAgeGroup(request):
    return render(request, 'knbs_bi/population_projections_by_selected_age_group_view.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addPopulationSelectedAgeGroup(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id

        selected_agegroup_add = PopulationProjectionsBySelectedAgeGroup(county_id=kaunti, range_0_4=request.data['range_0_4'], range_5_9 = request.data['range_5_9'],
                                                                        range_10_14=request.data['range_10_14'], range_15_19 = request.data['range_15_19'], range_20_24 = request.data['range_20_24'],
                                                                        range_25_29=request.data['range_25_29'], range_30_34=request.data['range_30_34'], range_35_39=request.data['range_35_39'],
                                                                        range_40_44=request.data['range_40_44'], range_45_49=request.data['range_45_49'], range_50_54=request.data['range_50_54'],
                                                                        range_55_59=request.data['range_55_59'], range_60_64=request.data['range_60_64'], range_65_69=request.data['range_65_69'],
                                                                        range_70_74=request.data['range_70_74'], range_75_79=request.data['range_75_79'],  range_80_plus=request.data['range_80_plus'],
                                                              gender=request.data['gender'], year=request.data['year'])
    if selected_agegroup_add:
        selected_agegroup_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editPopulationSelectedAgeGroup(request):
    selected_agegroup_edit = PopulationProjectionsBySelectedAgeGroup.objects.get(population_projection_id=request.data['projection_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            selected_agegroup_edit.county_id = counties.county_id

    if 'range_0_4' in request.data:
        selected_agegroup_edit.range_0_4 = request.data['range_0_4']

    if 'range_5_9' in request.data:
        selected_agegroup_edit.range_5_9 = request.data['range_5_9']

    if 'range_10_14' in request.data:
        selected_agegroup_edit.range_10_14 = request.data['range_10_14']

    if 'range_15_19' in request.data:
        selected_agegroup_edit.range_15_19 = request.data['range_15_19']

    if 'range_20_24' in request.data:
        selected_agegroup_edit.range_20_24 = request.data['range_20_24']

    if 'range_25_29' in request.data:
        selected_agegroup_edit.range_25_29 = request.data['range_25_29']

    if 'range_30_34' in request.data:
        selected_agegroup_edit.range_30_34 = request.data['range_30_34']

    if 'range_35_39' in request.data:
        selected_agegroup_edit.range_35_39 = request.data['range_35_39']

    if 'range_40_44' in request.data:
        selected_agegroup_edit.range_40_44 = request.data['range_40_44']

    if 'range_45_49' in request.data:
        selected_agegroup_edit.range_45_49 = request.data['range_45_49']

    if 'range_50_54' in request.data:
        selected_agegroup_edit.range_50_54 = request.data['range_50_54']

    if 'range_55_59' in request.data:
        selected_agegroup_edit.range_55_59 = request.data['range_55_59']

    if 'range_60_64' in request.data:
        selected_agegroup_edit.range_60_64 = request.data['range_60_64']

    if 'range_65_69' in request.data:
        selected_agegroup_edit.range_65_69 = request.data['range_65_69']

    if 'range_70_74' in request.data:
        selected_agegroup_edit.range_70_74 = request.data['range_70_74']

    if 'range_75_79' in request.data:
        selected_agegroup_edit.range_75_79 = request.data['range_75_79']

    if 'range_80_plus' in request.data:
        selected_agegroup_edit.range_80_plus = request.data['range_80_plus']

    if 'gender' in request.data:
        selected_agegroup_edit.gender = request.data['gender']

    if 'year' in request.data:
        selected_agegroup_edit.year = request.data['year']

    selected_agegroup_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

####################################PopulationProjectionsBySpecialAgeGroups####################################
#Launch Page
#Launch Page
def populationSpecialAgeGroupView(request):
    special_age_group = PopulationProjectionsBySpecialAgeGroups.objects.all()

    projections = []

    if special_age_group:
        for projection in special_age_group:
            county = Counties.objects.get(county_id=projection.county_id)

            c = {'id': projection.selected_age_group_id, 'county': county.county_name, 'under_1': projection.under_1, 'range_1_2': projection.range_1_2,
                 'range_3_5': projection.range_3_5, 'range_6_13': projection.range_6_13, 'range_14_17': projection.range_14_17, 'range_18_24': projection.range_18_24,
                 'range_18_34': projection.range_18_34, 'range_less_18': projection.range_less_18, 'range_18_plus': projection.range_18_plus, 'range_15_49': projection.range_15_49,
                 'range_15_64': projection.range_15_64, 'range_65_plus': projection.range_65_plus, 'gender': projection.gender, 'year': projection.year}
            projections.append(c)
            context = {'projections': projections}
    else:
        pass

    return render(request, 'knbs_bi/population_projections_by_special_age_groups.html', context)


@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def populationSpecialAgeGroup(request):
    special_age_group = PopulationProjectionsBySpecialAgeGroups.objects.all()

    projections = []

    if special_age_group:
        for projection in special_age_group:
            county = Counties.objects.get(county_id=projection.county_id)

            c = {'county': county.county_name, 'under_1': projection.under_1, 'range_1_2': projection.range_1_2,
                 'range_3_5': projection.range_3_5, 'range_6_13': projection.range_6_13, 'range_14_17': projection.range_14_17, 'range_18_24': projection.range_18_24,
                 'range_18_34': projection.range_18_34, 'range_less_18': projection.range_less_18, 'range_18_plus': projection.range_18_plus, 'range_15_49': projection.range_15_49,
                 'range_15_64': projection.range_15_64, 'range_65_plus': projection.range_65_plus, 'gender': projection.gender, 'year': projection.year}
            projections.append(c)
    else:
        pass

    return Response(projections)

# Add View
def addPopulationSpecialAgeGroupView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/population_projections_by_special_age_groups_add.html', context)


# Edit View
def editPopulationSpecialAgeGroupView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/population_projections_by_special_age_groups_edit.html', context)

# View More
def viewPopulationSpecialAgeGroup(request):
    return render(request, 'knbs_bi/population_projections_by_special_age_groups_view.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addPopulationSpecialAgeGroup(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id

        special_agegroup_add = PopulationProjectionsBySpecialAgeGroups(county_id=kaunti, under_1=request.data['under_1'], range_1_2 = request.data['range_1_2'],
                                                                       range_3_5=request.data['range_3_5'], range_6_13 = request.data['range_6_13'], range_14_17 = request.data['range_14_17'],
                                                                       range_18_24=request.data['range_18_24'], range_18_34=request.data['range_18_34'], range_less_18=request.data['range_less_18'],
                                                                       range_18_plus=request.data['range_18_plus'], range_15_49=request.data['range_15_49'], range_15_64=request.data['range_15_64'],
                                                                       range_65_plus=request.data['range_65_plus'], gender=request.data['gender'], year=request.data['year'])
    if special_agegroup_add:
        special_agegroup_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editPopulationSpecialAgeGroup(request):
    special_agegroup_edit = PopulationProjectionsBySpecialAgeGroups.objects.get(selected_age_group_id=request.data['age_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            special_agegroup_edit.county_id = counties.county_id

    if 'under_1' in request.data:
        special_agegroup_edit.under_1 = request.data['under_1']

    if 'range_1_2' in request.data:
        special_agegroup_edit.range_1_2 = request.data['range_1_2']

    if 'range_3_5' in request.data:
        special_agegroup_edit.range_3_5 = request.data['range_3_5']

    if 'range_6_13' in request.data:
        special_agegroup_edit.range_6_13 = request.data['range_6_13']

    if 'range_14_17' in request.data:
        special_agegroup_edit.range_14_17 = request.data['range_14_17']

    if 'range_18_24' in request.data:
        special_agegroup_edit.range_18_24 = request.data['range_18_24']

    if 'range_18_34' in request.data:
        special_agegroup_edit.range_18_34 = request.data['range_18_34']

    if 'range_less_18' in request.data:
        special_agegroup_edit.range_less_18 = request.data['range_less_18']

    if 'range_18_plus' in request.data:
        special_agegroup_edit.range_18_plus = request.data['range_18_plus']

    if 'range_15_49' in request.data:
        special_agegroup_edit.range_15_49 = request.data['range_15_49']

    if 'range_15_64' in request.data:
        special_agegroup_edit.range_15_64 = request.data['range_15_64']

    if 'range_65_plus' in request.data:
        special_agegroup_edit.range_65_plus = request.data['range_65_plus']

    if 'gender' in request.data:
        special_agegroup_edit.gender = request.data['gender']

    if 'year' in request.data:
        special_agegroup_edit.year = request.data['year']


    special_agegroup_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)