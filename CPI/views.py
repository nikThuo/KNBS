from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from CPI.models import Annual_Avg_Retail_Prices_Of_Certain_Consumer_Goods_In_Kenya, Consumer_Price_Index, \
    Elementary_Aggregates_Weights_In_The_Cpi_Baskets, Group_Weights_For_Kenya_Cpi_Febuary_Base_2009, \
    Group_Weights_For_Kenya_Cpi_October_Base_1997
from health.models import Months


def cpi(request):
    return render(request, template_name='knbs_bi/cpi.html')


########################################## Average Retail Prices of Certain Consumer Goods ##########################################
#Launch Page
def averageRetailView(request):
    average = Annual_Avg_Retail_Prices_Of_Certain_Consumer_Goods_In_Kenya.objects.all()

    prices = []

    if average:
        for price in average:
            c = {'id':price.avg_retail_price_id, 'item': price.item, 'unit': price.unit, 'ksh': price.ksh_per_unit,
                 'year': price.year}
            prices.append(c)
            context = {'prices': prices}
    else:
        pass
    return render(request, 'knbs_bi/cpi_annual_avg_retail_prices_of_certain_consumer_goods_in_kenya.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def averageRetail(request):
    average = Annual_Avg_Retail_Prices_Of_Certain_Consumer_Goods_In_Kenya.objects.all()

    prices = []

    if average:
        for price in average:
            c = {'item': price.item, 'unit': price.unit, 'ksh': price.ksh_per_unit,
                 'year': price.year}
            prices.append(c)
    else:
        pass
    return Response(prices)

# Add View
def addAverageRetailView(request):
    return render(request, 'knbs_bi/cpi_annual_avg_retail_prices_of_certain_consumer_goods_in_kenya_add.html')

# Edit View
def editAverageRetailView(request):
    return render(request, 'knbs_bi/cpi_annual_avg_retail_prices_of_certain_consumer_goods_in_kenya_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addAverageRetail(request):
    price_add = Annual_Avg_Retail_Prices_Of_Certain_Consumer_Goods_In_Kenya(item = request.data['item'], unit = request.data['unit'],
                                                                                    ksh_per_unit = request.data['ksh'],
                                                                                    year = request.data['year'])
    if price_add:
        price_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editAverageRetail(request):
    price_edit = Annual_Avg_Retail_Prices_Of_Certain_Consumer_Goods_In_Kenya.objects.get(avg_retail_price_id = request.data['retail'])

    if 'item' in request.data:
        price_edit.item = request.data['item']

    if 'unit' in request.data:
        price_edit.unit = request.data['unit']

    if 'ksh' in request.data:
        price_edit.ksh_per_unit = request.data['ksh']

    if 'year' in request.data:
        price_edit.year = request.data['year']


    price_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

########################################## Consumer Price Index ##########################################
#Launch Page
def consumerPriceView(request):
    price = Consumer_Price_Index.objects.all()

    prices = []

    if price:
        for consumer in price:
            c = {'id':consumer.cpi_retail_price_id, 'month': consumer.month,
                 'year': consumer.year, 'group': consumer.group,
                 'food': consumer.food_and_non_alcoholic_beverages, 'alcoholic': consumer.alcoholic_beverages_tobacco_narcotics,
                 'clothing': consumer.clothing_and_footwear, 'housing': consumer.housing_water_electricity_gas_and_other_fuels,
                 'furnishings': consumer.furnishings_household_equipment_routine_household_maintenance, 'health': consumer.health,
                 'transport': consumer.transport, 'communication': consumer.communication,
                 'recreation': consumer.recreation_and_culture, 'education': consumer.education,
                 'restaurant': consumer.restaurant_and_hotels, 'miscellaneous': consumer.miscellaneous_goods_and_services,
                 'total': consumer.total}
            prices.append(c)
            context = {'prices': prices}
    else:
        pass
    return render(request, 'knbs_bi/cpi_consumer_price_index.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def consumerPrice(request):
    price = Consumer_Price_Index.objects.all()

    prices = []

    if price:
        for consumer in price:
            c = {'month': consumer.month,
                 'year': consumer.year, 'group': consumer.group,
                 'food': consumer.food_and_non_alcoholic_beverages, 'alcoholic': consumer.alcoholic_beverages_tobacco_narcotics,
                 'clothing': consumer.clothing_and_footwear, 'housing': consumer.housing_water_electricity_gas_and_other_fuels,
                 'furnishings': consumer.furnishings_household_equipment_routine_household_maintenance, 'health': consumer.health,
                 'transport': consumer.transport, 'communication': consumer.communication,
                 'recreation': consumer.recreation_and_culture, 'education': consumer.education,
                 'restaurant': consumer.restaurant_and_hotels, 'miscellaneous': consumer.miscellaneous_goods_and_services,
                 'total': consumer.total}
            prices.append(c)
    else:
        pass
    return Response(prices)

# Add View
def addConsumerPriceView(request):
    all_months = Months.objects.all()
    context = {'months': all_months}
    return render(request, 'knbs_bi/cpi_consumer_price_index_add.html', context)

# Edit View
def editConsumerPriceView(request):
    all_months = Months.objects.all()
    context = {'months': all_months}
    return render(request, 'knbs_bi/cpi_consumer_price_index_edit.html', context)

# View More
def viewConsumerPrice(request):
    return render(request, 'knbs_bi/cpi_consumer_price_index_view.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addConsumerPrice(request):
    price_add = Consumer_Price_Index(month = request.data['month'], year = request.data['year'],
                            group = request.data['group'], food_and_non_alcoholic_beverages = request.data['food'],
                            alcoholic_beverages_tobacco_narcotics = request.data['alcoholic'], clothing_and_footwear = request.data['clothing'],
                            housing_water_electricity_gas_and_other_fuels = request.data['housing'], furnishings_household_equipment_routine_household_maintenance = request.data['furnishings'],
                            health = request.data['health'], transport = request.data['transport'],
                            communication = request.data['communication'], recreation_and_culture = request.data['recreation'],
                            education = request.data['education'], restaurant_and_hotels = request.data['restaurant'],
                            miscellaneous_goods_and_services = request.data['miscellaneous'], total = request.data['total'])
    if price_add:
        price_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editConsumerPrice(request):
    price_edit = Consumer_Price_Index.objects.get(cpi_retail_price_id = request.data['retail'])

    if 'month' in request.data:
        price_edit.month = request.data['month']

    if 'year' in request.data:
        price_edit.year = request.data['year']

    if 'group' in request.data:
        price_edit.group = request.data['group']

    if 'food' in request.data:
        price_edit.food_and_non_alcoholic_beverages = request.data['food']

    if 'alcoholic' in request.data:
        price_edit.alcoholic_beverages_tobacco_narcotics = request.data['alcoholic']

    if 'clothing' in request.data:
        price_edit.clothing_and_footwear = request.data['clothing']

    if 'housing' in request.data:
        price_edit.housing_water_electricity_gas_and_other_fuels = request.data['housing']

    if 'furnishings' in request.data:
        price_edit.furnishings_household_equipment_routine_household_maintenance = request.data['furnishings']

    if 'health' in request.data:
        price_edit.health = request.data['health']

    if 'transport' in request.data:
        price_edit.transport = request.data['transport']

    if 'communication' in request.data:
        price_edit.communication = request.data['communication']

    if 'recreation' in request.data:
        price_edit.recreation_and_culture = request.data['recreation']

    if 'education' in request.data:
        price_edit.education = request.data['education']

    if 'restaurant' in request.data:
        price_edit.restaurant_and_hotels = request.data['restaurant']

    if 'miscellaneous' in request.data:
        price_edit.miscellaneous_goods_and_services = request.data['miscellaneous']

    if 'total' in request.data:
        price_edit.total = request.data['total']


    price_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

########################################## Elementary Aggregate Weights in CPI Baskets ##########################################
#Launch Page
def elementaryWeightsView(request):
    elementary = Elementary_Aggregates_Weights_In_The_Cpi_Baskets.objects.all()

    aggregates = []

    if elementary:
        for aggregate in elementary:
            c = {'id':aggregate.aggregate_weights_id, 'coicop': aggregate.coicop_code,
                 'description': aggregate.description, 'nairobi_lower': aggregate.nairobi_lower,
                 'nairobi_middle': aggregate.nairobi_middle, 'nairobi_upper': aggregate.nairobi_upper,
                 'rest': aggregate.rest_of_urban_areas, 'kenya': aggregate.kenya}
            aggregates.append(c)
            context = {'aggregates': aggregates}
    else:
        pass
    return render(request, 'knbs_bi/cpi_elementary_aggregates_weights_in_the_cpi_baskets.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def elementaryWeights(request):
    elementary = Elementary_Aggregates_Weights_In_The_Cpi_Baskets.objects.all()

    aggregates = []

    if elementary:
        for aggregate in elementary:
            c = {'coicop': aggregate.coicop_code,
                 'description': aggregate.description, 'nairobi_lower': aggregate.nairobi_lower,
                 'nairobi_middle': aggregate.nairobi_middle, 'nairobi_upper': aggregate.nairobi_upper,
                 'rest': aggregate.rest_of_urban_areas, 'kenya': aggregate.kenya}
            aggregates.append(c)
    else:
        pass
    return Response(aggregates)

# Add View
def addElementaryWeightsView(request):
    return render(request, 'knbs_bi/cpi_elementary_aggregates_weights_in_the_cpi_baskets_add.html')

# Edit View
def editElementaryWeightsView(request):
    return render(request, 'knbs_bi/cpi_elementary_aggregates_weights_in_the_cpi_baskets_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addElementaryWeights(request):
    elementary_add = Elementary_Aggregates_Weights_In_The_Cpi_Baskets(coicop_code = request.data['code'], description = request.data['description'],
                            nairobi_lower = request.data['lower'], nairobi_middle = request.data['middle'],
                            nairobi_upper = request.data['upper'], rest_of_urban_areas = request.data['rest'],
                            kenya = request.data['kenya'])
    if elementary_add:
        elementary_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editElementaryWeights(request):
    elementary_edit = Elementary_Aggregates_Weights_In_The_Cpi_Baskets.objects.get(aggregate_weights_id = request.data['weight'])

    if 'code' in request.data:
        elementary_edit.coicop_code = request.data['code']

    if 'description' in request.data:
        elementary_edit.description = request.data['description']

    if 'lower' in request.data:
        elementary_edit.nairobi_lower = request.data['lower']

    if 'middle' in request.data:
        elementary_edit.nairobi_middle = request.data['middle']

    if 'upper' in request.data:
        elementary_edit.nairobi_upper = request.data['upper']

    if 'rest' in request.data:
        elementary_edit.rest_of_urban_areas = request.data['rest']

    if 'kenya' in request.data:
        elementary_edit.kenya = request.data['kenya']

    elementary_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

########################################## Group Weights for Kenya Base 2009 ##########################################
#Launch Page
def groupWeightsView(request):
    group = Group_Weights_For_Kenya_Cpi_Febuary_Base_2009.objects.all()

    weights = []

    if group:
        for weight in group:
            c = {'id':weight.group_weights_id, 'description': weight.description,
                 'household': weight.household, 'group_weights': weight.group_weights}
            weights.append(c)
            context = {'weights': weights}
    else:
        pass
    return render(request, 'knbs_bi/cpi_group_weights_for_kenya_cpi_febuary_base_2009.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def groupWeights(request):
    group = Group_Weights_For_Kenya_Cpi_Febuary_Base_2009.objects.all()

    weights = []

    if group:
        for weight in group:
            c = {'description': weight.description,
                 'household': weight.household, 'group_weights': weight.group_weights}
            weights.append(c)
    else:
        pass
    return Response(weights)

# Add View
def addGroupWeightsView(request):
    return render(request, 'knbs_bi/cpi_group_weights_for_kenya_cpi_febuary_base_2009_add.html')

# Edit View
def editGroupWeightsView(request):
    return render(request, 'knbs_bi/cpi_group_weights_for_kenya_cpi_febuary_base_2009_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addGroupWeights(request):
    group_add = Group_Weights_For_Kenya_Cpi_Febuary_Base_2009(description = request.data['description'],
                            household = request.data['household'], group_weights = request.data['weights'])
    if group_add:
        group_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editGroupWeights(request):
    group_edit = Group_Weights_For_Kenya_Cpi_Febuary_Base_2009.objects.get(group_weights_id = request.data['group'])

    if 'description' in request.data:
        group_edit.description = request.data['description']

    if 'household' in request.data:
        group_edit.household = request.data['household']

    if 'weights' in request.data:
        group_edit.group_weights = request.data['weights']

    group_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

########################################## Group Weights for Kenya Base 1997 ##########################################
#Launch Page
def groupWeightsKenyaView(request):
    group = Group_Weights_For_Kenya_Cpi_October_Base_1997.objects.all()

    weights = []

    if group:
        for weight in group:
            c = {'id':weight.group_weight_id, 'item_group': weight.item_group,
                 'household': weight.household, 'group_weights': weight.group_weights}
            weights.append(c)
            context = {'weights': weights}
    else:
        pass
    return render(request, 'knbs_bi/cpi_group_weights_for_kenya_cpi_october_base_1997.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def groupWeightsKenya(request):
    group = Group_Weights_For_Kenya_Cpi_October_Base_1997.objects.all()

    weights = []

    if group:
        for weight in group:
            c = {'item_group': weight.item_group,
                 'household': weight.household, 'group_weights': weight.group_weights}
            weights.append(c)
    else:
        pass
    return Response(weights)

# Add View
def addGroupWeightsKenyaView(request):
    return render(request, 'knbs_bi/cpi_group_weights_for_kenya_cpi_october_base_1997_add.html')

# Edit View
def editGroupWeightsKenyaView(request):
    return render(request, 'knbs_bi/cpi_group_weights_for_kenya_cpi_october_base_1997_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addGroupWeightsKenya(request):
    group_add = Group_Weights_For_Kenya_Cpi_October_Base_1997(item_group = request.data['item'],
                            household = request.data['household'], group_weights = request.data['weights'])
    if group_add:
        group_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editGroupWeightsKenya(request):
    group_edit = Group_Weights_For_Kenya_Cpi_October_Base_1997.objects.get(group_weight_id = request.data['group'])

    if 'item' in request.data:
        group_edit.item_group = request.data['item']

    if 'household' in request.data:
        group_edit.household = request.data['household']

    if 'weights' in request.data:
        group_edit.group_weights = request.data['weights']

    group_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)