from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from health.models import Counties
from population.models import PopulationBySexHouseholdsDensityAndCensusYears, PopulationProjectionsBySelectedAgeGroup, \
    PopulationProjectionsBySpecialAgeGroups


@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def populationSex(request):
    pop_sex = PopulationBySexHouseholdsDensityAndCensusYears.objects.all()

    pops = []

    if pop_sex:
        for population in pop_sex:
            c = {'no_of_male': population.male, 'no_of_female': population.female, 'total': population.total,
                 'hhs': population.hhs, 'av_hh_size': population.av_hh_size, 'approx_area': population.approx_area,
                 'density': population.density, 'census_year': population.census_year}
            pops.append(c)
    else:
        pass
    return Response(pops)

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def populationSelectedAge(request):
    pop_select = PopulationProjectionsBySelectedAgeGroup.objects.all()

    pops = []

    if pop_select:
        for population in pop_select:
            county = Counties.objects.get(county_id=population.county_id)
            c = {'county': county.county_name, 'range_0_4': population.range_0_4, 'range_5_9': population.range_5_9,
                 'range_10_14': population.range_10_14, 'range_15_19': population.range_15_19,
                 'range_20_24': population.range_20_24, 'range_25_29': population.range_25_29,
                 'range_30_34': population.range_30_34, 'range_35_39': population.range_35_39,
                 'range_40_44': population.range_40_44, 'range_45_49': population.range_45_49,
                 'range_50_54': population.range_50_54, 'range_55_59': population.range_55_59,
                 'range_60_64': population.range_60_64, 'range_65_69': population.range_65_69,
                 'range_70_74':population.range_70_74, 'range_75_79': population.range_75_79,
                 'range_80_plus': population.range_80_plus, 'total': population.total, 'gender': population.gender,
                 'year': population.year}
            pops.append(c)
    else:
        pass
    return Response(pops)

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def populationSpecialGroup(request):
    pop_special = PopulationProjectionsBySpecialAgeGroups.objects.all()

    pops = []

    if pop_special:
        for population in pop_special:
            county = Counties.objects.get(county_id=population.county_id)
            c = {'county': county.county_name, 'under_1': population.under_1, 'range_1_2': population.range_1_2,
                 'range_3_5': population.range_3_5, 'range_6_13': population.range_6_13,
                 'range_14_17': population.range_14_17, 'range_18_24': population.range_18_24,
                 'range_18_34': population.range_18_34, 'range_less_18': population.range_less_18,
                 'range_18_plus': population.range_18_plus, 'range_15_49': population.range_15_49,
                 'range_15_64': population.range_15_64, 'range_65_plus': population.range_65_plus,
                 'gender': population.gender, 'year': population.year}
            pops.append(c)
    else:
        pass
    return Response(pops)