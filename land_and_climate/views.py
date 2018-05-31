from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from health.models import Counties
from land_and_climate.models import Surface_Area_By_Category, Surface_Area_By_Category_Ids, Temperature_Ids, \
    Temperature, Rainfall, Rainfall_Ids, Topography_Altitude


def land_and_climate(request):
    return render(request, template_name="knbs_bi/land_and_climate.html")

#===============================Surface Area by Category===============================
#Launch Page
def viewSurfaceArea(request):
    all_surface = Surface_Area_By_Category.objects.all()

    categories = []

    if all_surface:
        for category in all_surface:
            counties = Counties.objects.get(county_id=category.county_id)
            surface = Surface_Area_By_Category_Ids.objects.get(category_id=category.category_id)
            c = {'id': category.surface_area_id, 'county': counties.county_name, 'category': surface.categories, 'area': category.area_sq_km}
            categories.append(c)
            context = {'categories': categories}
    return render(request, 'knbs_bi/land_and_climate_surface_area_by_category.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def surfaceArea(request):
    all_surface = Surface_Area_By_Category.objects.all()

    categories = []

    if all_surface:
        for category in all_surface:
            counties = Counties.objects.get(county_id=category.county_id)
            surface = Surface_Area_By_Category_Ids.objects.get(category_id=category.category_id)
            c = {'county': counties.county_name, 'category': surface.categories, 'area': category.area_sq_km}
            categories.append(c)
    else:
        pass
    return Response(categories)

#Add County Revenue
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addSurfaceArea(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    surface = Surface_Area_By_Category_Ids.objects.get(categories=request.data['category'])

    if counties and surface:
        kaunti = counties.county_id


        surface_area_add = Surface_Area_By_Category(county_id = kaunti, category_id=surface.category_id, area_sq_km = request.data['area'])

        if surface_area_add:
            surface_area_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit County Revenue
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editSurfaceArea(request):

    surface_area_update = Surface_Area_By_Category.objects.get(surface_area_id= request.data['surface_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            surface_area_update.county_id = counties.county_id
    if 'category' in request.data:
        surface = Surface_Area_By_Category_Ids.objects.get(categories=request.data['category'])
        if surface:
            surface_area_update.category_id = surface.category_id

    if 'area' in request.data:
        surface_area_update.area_sq_km = request.data['area']

    surface_area_update.save()
    response = {'Update Successful'}
    return Response(response)

#County Revenue Add View
def addSurfaceAreaView(request):
    all_counties = Counties.objects.all()
    surface = Surface_Area_By_Category_Ids.objects.all()
    context = {'counties': all_counties, 'surface': surface}
    # translation.activate('en')
    return render(request, 'knbs_bi/land_and_climate_surface_area_by_category_add.html', context)

#County Revenue Edit View
def editSurfaceAreaView(request):
    all_counties = Counties.objects.all()
    surface = Surface_Area_By_Category_Ids.objects.all()
    context = {'counties': all_counties, 'surface': surface}
    return render(request, 'knbs_bi/land_and_climate_surface_area_by_category_edit.html', context)

#===============================Temperature===============================
#Launch Page
def viewTemperature(request):
    all_temperature = Temperature.objects.all()

    temperatures = []

    if all_temperature:
        for temperature in all_temperature:
            counties = Counties.objects.get(county_id=temperature.county_id)
            temp = Temperature_Ids.objects.get(temperature_id=temperature.temperature_id)
            c = {'id': temperature.climate_temperature_id, 'county': counties.county_name, 'temperature': temp.temperatures, 'degrees': temperature.temp_celsius_degrees,
                 'year': temperature.year}
            temperatures.append(c)
            context = {'temperatures': temperatures}
    return render(request, 'knbs_bi/land_and_climate_temperature.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def Temperatures(request):
    all_temperature = Temperature.objects.all()

    temperatures = []

    if all_temperature:
        for temperature in all_temperature:
            counties = Counties.objects.get(county_id=temperature.county_id)
            temp = Temperature_Ids.objects.get(temperature_id=temperature.temperature_id)
            c = {'county': counties.county_name, 'temperature': temp.temperatures, 'degrees': temperature.temp_celsius_degrees,
                 'year': temperature.year}
            temperatures.append(c)
    return Response(temperatures)

#Add County Revenue
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addTemperature(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    temp = Temperature_Ids.objects.get(temperatures=request.data['temperatures'])

    if counties and temp:
        kaunti = counties.county_id
        temperature = temp.temperature_id

        temperature_add = Temperature(county_id = kaunti, temperature_id=temperature, temp_celsius_degrees = request.data['degrees'],
                                                   year=request.data['year'])

        if temperature_add:
            temperature_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit County Revenue
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editTemperature(request):

    temperature_update = Temperature.objects.get(climate_temperature_id= request.data['temperature_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            temperature_update.county_id = counties.county_id

    if 'temperature' in request.data:
        temp = Temperature_Ids.objects.get(temperatures=request.data['temperature'])
        if temp:
            temperature_update.temperature_id = temp.temperature_id

    if 'degrees' in request.data:
        temperature_update.temp_celsius_degrees = request.data['degrees']

    if 'year' in request.data:
        temperature_update.year = request.data['year']

    temperature_update.save()
    response = {'Update Successful'}
    return Response(response)

#County Revenue Add View
def addTemperatureView(request):
    all_counties = Counties.objects.all()
    temperatures = Temperature_Ids.objects.all()
    context = {'counties': all_counties, 'temperatures': temperatures}
    # translation.activate('en')
    return render(request, 'knbs_bi/land_and_climate_temperature_add.html', context)

#County Revenue Edit View
def editTemperatureView(request):
    all_counties = Counties.objects.all()
    temperatures = Temperature_Ids.objects.all()
    context = {'counties': all_counties, 'temperatures': temperatures}
    return render(request, 'knbs_bi/land_and_climate_temperature_edit.html', context)

#===============================Rainfall===============================
#Launch Page
def viewRainfall(request):
    all_rainfall = Rainfall.objects.all()

    rainfall = []

    if all_rainfall:
        for rain in all_rainfall:
            counties = Counties.objects.get(county_id=rain.county_id)
            fall = Rainfall_Ids.objects.get(rainfall_id=rain.rainfall_id)
            c = {'id': rain.climate_rainfall_id, 'county': counties.county_name, 'rainfall': fall.rainFall, 'rain_mm': rain.rainfall_in_mm,
                 'year': rain.year}
            rainfall.append(c)
            context = {'rainfall': rainfall}
    return render(request, 'knbs_bi/land_and_climate_rainfall.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def rain_fall(request):
    all_rainfall = Rainfall.objects.all()

    rainfall = []

    if all_rainfall:
        for rain in all_rainfall:
            counties = Counties.objects.get(county_id=rain.county_id)
            fall = Rainfall_Ids.objects.get(rainfall_id=rain.rainfall_id)
            c = {'county': counties.county_name, 'rainfall': fall.rainFall, 'rain_mm': rain.rainfall_in_mm,
                 'year': rain.year}
            rainfall.append(c)
    return Response(rainfall)

#Add County Revenue
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addRainfall(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    fall = Rainfall_Ids.objects.get(rainFall=request.data['rainfall'])

    if counties and fall:
        kaunti = counties.county_id
        rain = fall.rainfall_id

        rainfall_add = Rainfall(county_id = kaunti, rainfall_id=rain, rainfall_in_mm= request.data['rain_mm'],
                                                   year=request.data['year'])

        if rainfall_add:
            rainfall_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit County Revenue
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editRainfall(request):

    rainfall_update = Rainfall.objects.get(climate_rainfall_id=request.data['rainfall_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            rainfall_update.county_id = counties.county_id

    if 'rainfall' in request.data:
        rain = Rainfall_Ids.objects.get(rainFall=request.data['rainfall'])
        if rain:
            rainfall_update.rainfall_id = rain.rainfall_id

    if 'rain_mm' in request.data:
        rainfall_update.rainfall_in_mm = request.data['rain_mm']

    if 'year' in request.data:
        rainfall_update.year = request.data['year']

    rainfall_update.save()
    response = {'Update Successful'}
    return Response(response)

#County Revenue Add View
def addRainfallView(request):
    all_counties = Counties.objects.all()
    rainfall = Rainfall_Ids.objects.all()
    context = {'counties': all_counties, 'rainfall': rainfall}
    # translation.activate('en')
    return render(request, 'knbs_bi/land_and_climate_rainfall_add.html', context)

#County Revenue Edit View
def editRainfallView(request):
    all_counties = Counties.objects.all()
    rainfall = Rainfall_Ids.objects.all()
    context = {'counties': all_counties, 'rainfall': rainfall}
    return render(request, 'knbs_bi/land_and_climate_rainfall_edit.html', context)

#===============================Topography and Altitude===============================
#Launch Page
def viewTopograhyAltitude(request):
    all_topography = Topography_Altitude.objects.all()

    topograhies = []

    if all_topography:
        for topograhy in all_topography:
            counties = Counties.objects.get(county_id=topograhy.county_id)
            c = {'id': topograhy.altitude_topography_id, 'county': counties.county_name, 'geography': topograhy.geography_type, 'altitude': topograhy.altitude_in_metres,
                 'year': topograhy.year}
            topograhies.append(c)
            context = {'topograhies': topograhies}
    return render(request, 'knbs_bi/land_and_climate_topography_altitude.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def topograhyAltitude(request):
    all_topography = Topography_Altitude.objects.all()

    topograhies = []

    if all_topography:
        for topograhy in all_topography:
            counties = Counties.objects.get(county_id=topograhy.county_id)
            c = {'county': counties.county_name, 'geography': topograhy.geography_type, 'altitude': topograhy.altitude_in_metres,
                 'year': topograhy.year}
            topograhies.append(c)
    return Response(topograhies)

#Add County Revenue
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addTopograhyAltitude(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id

        topography_add = Topography_Altitude(county_id = kaunti, geography_type = request.data['geography'], altitude_in_metres= request.data['altitude'],
                                                   year=request.data['year'])

        if topography_add:
            topography_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit County Revenue
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editTopograhyAltitude(request):
    topography_update = Topography_Altitude.objects.get(altitude_topography_id=request.data['topograhy_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            topography_update.county_id = counties.county_id

    if 'geography' in request.data:
        topography_update.geography_type = request.data['geography']

    if 'altitude' in request.data:
        topography_update.altitude_in_metres = request.data['altitude']

    if 'year' in request.data:
        topography_update.year = request.data['year']

    topography_update.save()
    response = {'Update Successful'}
    return Response(response)

#County Revenue Add View
def addTopograhyAltitudeView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    # translation.activate('en')
    return render(request, 'knbs_bi/land_and_climate_topography_altitude_add.html', context)

#County Revenue Edit View
def editTopograhyAltitudeView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/land_and_climate_topography_altitude_edit.html', context)