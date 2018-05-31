from django.shortcuts import render

# Create your views here.
#===============================POLITICAL==============================

#All Units
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

# from political.models import Units
from health.models import Counties, SubCounty
from political.models import Units


def political(request):
    return render(request, template_name='knbs_bi/political.html')
#===============================Units===============================
#Launch Page
def allUnitsView(request):
    all_units = Units.objects.all()

    units = []

    if all_units:
        for unit in all_units:
            county = Counties.objects.get(county_id=unit.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=unit.subcounty_id)

            if subcounty:
                for sc in subcounty:
                    c = {'id':unit.political_unit_id, 'county': county.county_name, 'subcounty': sc.subcounty_name,
                         'county_ward': unit.county_ward}

                    units.append(c)
                    context = {'units': units}
    else:
        pass

    return render(request, 'knbs_bi/political_units.html', context)

#Political Add View
def addUnitsView(request):
    all_counties = Counties.objects.all()
    sub_county = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': sub_county}
    # translation.activate('en')
    return render(request, 'knbs_bi/political_units_add.html', context)

#Political Edit View
def editUnitsView(request):
    all_counties = Counties.objects.all()
    sub_county = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': sub_county}
    return render(request, 'knbs_bi/political_units_edit.html', context)


@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def allUnits(request):
    all_units = Units.objects.all()

    units = []

    if all_units:
        for unit in all_units:
            counties = Counties.objects.get(county_id=unit.county_id)
            sub_county = SubCounty.objects.get(subcounty_id= unit.subcounty_id)
            c = {'county': counties.county_name, 'subcounty':sub_county.subcounty_name, 'no_of_wards':unit.county_ward}
            units.append(c)
    else:
        pass
    return Response(units)

# Add Political
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addPolitical(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])

    if counties and sub:
        kaunti = counties.county_id
        sub_kaunti = sub.subcounty_id

        unit_add = Units(county_id=kaunti, subcounty_id=sub_kaunti, county_ward=request.data['ward'])

        if unit_add:
            unit_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Political
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editPolitical(request):
    unit_edit = Units.objects.get(political_unit_id=request.data['political_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            unit_edit.county_id = counties.county_id

    if 'sub_county' in request.data:
        sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])
        if sub:
            unit_edit.subcounty_id = sub.subcounty_id

    if 'ward' in request.data:
        unit_edit.county_ward = request.data['ward']

    unit_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)
