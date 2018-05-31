from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from administrative.models import Unit
from health.models import Counties, SubCounty, Sectors


def administrative(request):
    return render(request, template_name='knbs_bi/administrative.html')

def no_records(request):
    datasets = Sectors.objects.filter(sector_name='Political and Administrative Units')
    context = {'admin_count': datasets.count()}
    return render(request, 'knbs_bi/index.html', context)


#===============================Administrative Unit===============================
#Launch Page
def allUnitView(request):
    all_units = Unit.objects.all()

    units = []

    if all_units:
        for unit in all_units:
            county = Counties.objects.get(county_id=unit.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=unit.subcounty_id)

            if subcounty:
                for sc in subcounty:
                    c = {'id':unit.administrative_unit_id, 'county': county.county_name, 'subcounty': sc.subcounty_name,
                         'divisions': unit.divisions, 'locations': unit.locations, 'sub_locations': unit.sub_locations}

                    units.append(c)
                    context = {'units': units}
    else:
        pass

    return render(request, 'knbs_bi/administrative_unit.html', context)

#Administrative Add View
def addUnitView(request):
    all_counties = Counties.objects.all()
    sub_county = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': sub_county}
    # translation.activate('en')
    return render(request, 'knbs_bi/administrative_unit_add.html', context)

#Administrative Edit View
def editUniView(request):
    all_counties = Counties.objects.all()
    sub_county = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': sub_county}
    return render(request, 'knbs_bi/administrative_unit_edit.html', context)

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def allUnit(request):
    all_units = Unit.objects.all()

    units = []

    if all_units:
        for unit in all_units:
            counties = Counties.objects.get(county_id=unit.county_id)
            # sub_county = SubCounty.objects.filter(subcounty_id=unit.subcounty_id)
            # d = sub_county
            c = {'county': counties.county_name,
                 'no_of_divisions': unit.divisions, 'no_of_locations':unit.locations, 'no_of_sublocations':unit.sub_locations}
            units.append(c)
    else:
        pass
    return Response(units)

# Add Administrative
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addAdministrative(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])

    if counties and sub:
        kaunti = counties.county_id
        sub_kaunti = sub.subcounty_id

        unit_add = Unit(county_id=kaunti, subcounty_id=sub_kaunti, divisions=request.data['divisions'],
                                              locations=request.data['locations'], sub_locations=request.data['sub_locations'])

        if unit_add:
            unit_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Administrative
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editAdministrative(request):
    unit_edit = Unit.objects.get(administrative_unit_id=request.data['admin_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            unit_edit.county_id = counties.county_id

    if 'sub_county' in request.data:
        sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])
        if sub:
            unit_edit.subcounty_id = sub.subcounty_id

    if 'divisions' in request.data:
        unit_edit.divisions = request.data['divisions']
    if 'locations' in request.data:
        unit_edit.locations = request.data['locations']
    if 'sub_locations' in request.data:
        unit_edit.sub_locations = request.data['sub_locations']

    unit_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)
