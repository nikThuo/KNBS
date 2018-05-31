from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from health.models import Counties
from transport_and_communication.models import Road_Coverage_By_Type_And_Distance, Road_Coverage_Type_Distance_Ids, \
    Coverage_Of_Telephone_Services, Coverage_Of_Telephone_Services_Ids, Coverage_Of_Postal_Services, \
    Coverage_Of_Postal_Services_Ids


def transport_and_communication(request):
    return render(request, template_name="knbs_bi/transport_and_communication.html")

#===============================Surface Area by Category===============================
#Launch Page
def viewTransportCommunication(request):
    all_transport = Road_Coverage_By_Type_And_Distance.objects.all()

    coverages = []

    if all_transport:
        for coverage in all_transport:
            counties = Counties.objects.get(county_id=coverage.county_id)
            road = Road_Coverage_Type_Distance_Ids.objects.get(road_type_id=coverage.road_type_id)
            c = {'id': coverage.road_coverage_id, 'county': counties.county_name, 'road_type': road.road_type, 'distance': coverage.distance,
                 'year': coverage.year}
            coverages.append(c)
            context = {'coverages': coverages}
    return render(request, 'knbs_bi/transport_and_communication_road_coverage_by_type_and_distance.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def TransportCommunication(request):
    all_transport = Road_Coverage_By_Type_And_Distance.objects.all()

    coverages = []

    if all_transport:
        for coverage in all_transport:
            counties = Counties.objects.get(county_id=coverage.county_id)
            road = Road_Coverage_Type_Distance_Ids.objects.get(road_type_id=coverage.road_type_id)
            c = {'county': counties.county_name, 'road_type': road.road_type, 'distance': coverage.distance,
                 'year': coverage.year}
            coverages.append(c)
    return Response(coverages)

#Add County Revenue
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addTransportCommunication(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    road = Road_Coverage_Type_Distance_Ids.objects.get(road_type=request.data['road_type'])

    if counties and road:
        kaunti = counties.county_id


        coverage_add = Road_Coverage_By_Type_And_Distance(county_id = kaunti, road_type_id = road.road_type_id, distance = request.data['distance'],
                                                          year = request.data['year'])

        if coverage_add:
            coverage_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit County Revenue
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editTransportCommunication(request):

    coverage_update = Road_Coverage_By_Type_And_Distance.objects.get(road_coverage_id=request.data['coverage_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            coverage_update.county_id = counties.county_id
    if 'road_type' in request.data:
        road = Road_Coverage_Type_Distance_Ids.objects.get(road_type=request.data['road_type'])
        if road:
            coverage_update.category_id = road.road_type_id

    if 'distance' in request.data:
        coverage_update.distance = request.data['distance']

    if 'year' in request.data:
        coverage_update.year = request.data['year']

    coverage_update.save()
    response = {'Update Successful'}
    return Response(response)

#County Revenue Add View
def addTransportCommunicationView(request):
    all_counties = Counties.objects.all()
    roads = Road_Coverage_Type_Distance_Ids.objects.all()
    context = {'counties': all_counties, 'roads': roads}
    # translation.activate('en')
    return render(request, 'knbs_bi/transport_and_communication_road_coverage_by_type_and_distance_add.html', context)

#County Revenue Edit View
def editTransportCommunicationView(request):
    all_counties = Counties.objects.all()
    roads = Road_Coverage_Type_Distance_Ids.objects.all()
    context = {'counties': all_counties, 'roads': roads}
    return render(request, 'knbs_bi/transport_and_communication_road_coverage_by_type_and_distance_edit.html', context)

#===============================Coverage_Of_Telephone_Services===============================
#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def telephoneCoverage(request):
    telephone_coverage = Coverage_Of_Telephone_Services.objects.all()

    coverages = []

    if telephone_coverage:
        for coverage in telephone_coverage:
            counties = Counties.objects.get(county_id=coverage.county_id)
            telephone = Coverage_Of_Telephone_Services_Ids.objects.get(telephone_service_id=coverage.telephone_service_id)
            c = {'county': counties.county_name, 'telephone_service': telephone.telephone_service, 'number': coverage.number,
                 'year': coverage.year}
            coverages.append(c)
    return Response(coverages)

#===============================Coverage_Of_Postal_Services===============================
#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def postalCoverage(request):
    postal_coverage = Coverage_Of_Postal_Services.objects.all()

    coverages = []

    if postal_coverage:
        for coverage in postal_coverage:
            counties = Counties.objects.get(county_id=coverage.county_id)
            postal = Coverage_Of_Postal_Services_Ids.objects.get(postal_service_id=coverage.postal_service_id)
            c = {'county': counties.county_name, 'postal_service': postal.postal_service, 'number': coverage.number,
                 'year': coverage.year}
            coverages.append(c)
    return Response(coverages)