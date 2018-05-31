from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from energy.models import AverageMonthlyPumpPricesForFuelByCategory, \
    Average_Retail_Prices_Of_Selected_Petroleum_Products, Net_Domestic_Sale_Of_Petroleum_Fuels_By_Consumer_Category, \
    Value_And_Quantity_Of_Imports_Exports, Petroleum_Supply_And_Demand, Installed_And_Effective_Capacity_Of_Electricity, \
    Generation_And_Imports_Of_Electricity, Electricity_Demand_And_Supply
from health.models import Counties

def energy(request):
    return render(request, template_name='knbs_bi/energy.html')


############################################AverageMonthlyPumpPricesForFuelByCategory############################################
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def pumpPricesFuel(request):
    pump_price = AverageMonthlyPumpPricesForFuelByCategory.objects.all()

    prices = []

    if pump_price:
        for price in pump_price:
            county = Counties.objects.get(county_id=price.county_id)

            c = {'county': county.county_name, 'month': price.month_id, 'super_petrol': price.super_petrol,
                 'diesel': price.diesel, 'kerosene': price.kerosene, 'year': price.year}

            prices.append(c)
    else:
        pass

    return Response(prices)

# Launch Page
def pumpPricesFuelView(request):
    pump_price = AverageMonthlyPumpPricesForFuelByCategory.objects.all()

    prices = []

    if pump_price:
        for price in pump_price:
            county = Counties.objects.get(county_id=price.county_id)

            c = {'id': price.county_id, 'county': county.county_name, 'month': price.month_id, 'super_petrol': price.super_petrol,
                 'diesel': price.diesel, 'kerosene': price.kerosene, 'year': price.year}

            prices.append(c)
            context = {'prices': prices}
    else:
        pass

    return render(request, 'knbs_bi/energy_average_monthly_pump_prices_for_fuel_by_category.html', prices)

# Add View
def addPumpPricesFuelView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/energy_average_monthly_pump_prices_for_fuel_by_category_add.html')


# Edit View
def editPumpPricesFuelView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/energy_average_monthly_pump_prices_for_fuel_by_category_edit.html')


# # Add Record
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def addPumpPricesFuel(request):
#     counties = Counties.objects.get(county_name=request.data['county'])
#
#     if counties:
#         kaunti = counties.county_id
#
#         price_add = AverageMonthlyPumpPricesForFuelByCategory(county_id=kaunti, request.data['commodity'],
#                                                                      quantum_indice=request.data['indice'],
#                                                                      year=request.data['year'])
#         if indice_add:
#             indice_add.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#
# # Edit Record
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def editPumpPricesFuel(request):
#     indice_edit = AverageMonthlyPumpPricesForFuelByCategory.objects.get(quantum_indice_id=request.data['quantum_id'])
#
#     if 'commodity' in request.data:
#         indice_edit.commodity = request.data['commodity']
#     if 'indice' in request.data:
#         indice_edit.quantum_indice = request.data['indice']
#     if 'year' in request.data:
#         indice_edit.year = request.data['year']
#
#     indice_edit.save()
#     return Response(status=status.HTTP_201_CREATED)

############################################Average Retail Prices of Selected Petroleum Products############################################
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def averagePrices(request):
    average_price = Average_Retail_Prices_Of_Selected_Petroleum_Products.objects.all()

    prices = []

    if average_price:
        for price in average_price:

            c = {'petroleum_product': price.petroleum_product, 'retail_price': price.retail_price_ksh, 'month': price.month,
                 'year': price.year}

            prices.append(c)
    else:
        pass

    return Response(prices)

# Launch Page
def averagePricesView(request):
    average_price = Average_Retail_Prices_Of_Selected_Petroleum_Products.objects.all()

    prices = []

    if average_price:
        for price in average_price:

            c = {'id':price.retail_price_id, 'petroleum_product': price.petroleum_product, 'retail_price': price.retail_price_ksh, 'month': price.month,
                 'year': price.year}

            prices.append(c)
            context = {'prices': prices}
    else:
        pass

    return render(request, 'knbs_bi/energy_average_retail_prices_of_selected_petroleum_products.html', context)

# Add View
def addAveragePricesView(request):
    return render(request, 'knbs_bi/energy_average_retail_prices_of_selected_petroleum_products_add.html')

# Edit View
def editAveragePricesView(request):
    return render(request, 'knbs_bi/energy_average_retail_prices_of_selected_petroleum_products_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addAveragePrices(request):
    price_add = Average_Retail_Prices_Of_Selected_Petroleum_Products(petroleum_product=request.data['petroleum'],
                                                                     retail_price_ksh=request.data['price'],
                                                                     month=request.data['month'], year=request.data['year'])
    if price_add:
        price_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editAveragePrices(request):
    price_edit = Average_Retail_Prices_Of_Selected_Petroleum_Products.objects.get(retail_price_id=request.data['price_id'])

    if 'petroleum' in request.data:
        price_edit.petroleum_product = request.data['petroleum']
    if 'price' in request.data:
        price_edit.retail_price_ksh = request.data['price']
    if 'month' in request.data:
        price_edit.month = request.data['month']
    if 'year' in request.data:
        price_edit.year = request.data['year']

    price_edit.save()
    return Response(status=status.HTTP_201_CREATED)

############################################Net_Domestic_Sale_Of_Petroleum_Fuels_By_Consumer_Category############################################
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def domesticSale(request):
    domestic_sale = Net_Domestic_Sale_Of_Petroleum_Fuels_By_Consumer_Category.objects.all()

    fuels = []

    if domestic_sale:
        for fuel in domestic_sale:

            c = {'consumer': fuel.user, 'quantity_tonnes': fuel.quantity_tonnes, 'year': fuel.year}

            fuels.append(c)
    else:
        pass

    return Response(fuels)

# Launch Page
def domesticSaleView(request):
    domestic_sale = Net_Domestic_Sale_Of_Petroleum_Fuels_By_Consumer_Category.objects.all()

    fuels = []

    if domestic_sale:
        for fuel in domestic_sale:

            c = {'id':fuel.domestic_sale_id, 'consumer': fuel.user, 'quantity_tonnes': fuel.quantity_tonnes, 'year': fuel.year}

            fuels.append(c)
            context = {'fuels': fuels}
    else:
        pass

    return render(request, 'knbs_bi/energy_net_domestic_sale_of_petroleum_fuels_by_consumer_category.html', context)

# Add View
def addDomesticSaleView(request):
    return render(request, 'knbs_bi/energy_net_domestic_sale_of_petroleum_fuels_by_consumer_category_add.html')

# Edit View
def editDomesticSaleView(request):
    return render(request, 'knbs_bi/energy_net_domestic_sale_of_petroleum_fuels_by_consumer_category_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addDomesticSale(request):
    sale_add = Net_Domestic_Sale_Of_Petroleum_Fuels_By_Consumer_Category(user=request.data['user'], quantity_tonnes=request.data['quantity'],
                                                    year=request.data['year'])
    if sale_add:
        sale_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editDomesticSale(request):
    sale_edit = Net_Domestic_Sale_Of_Petroleum_Fuels_By_Consumer_Category.objects.get(domestic_sale_id=request.data['sale_id'])

    if 'user' in request.data:
        sale_edit.user = request.data['user']
    if 'quantity' in request.data:
        sale_edit.quantity_tonnes = request.data['quantity']
    if 'year' in request.data:
        sale_edit.year = request.data['year']

    sale_edit.save()
    return Response(status=status.HTTP_201_CREATED)

############################################Value_And_Quantity_Of_Imports_Exports############################################
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def valueQuantity(request):
    value_quantity = Value_And_Quantity_Of_Imports_Exports.objects.all()

    quantities = []

    if value_quantity:
        for quantity in value_quantity:

            c = {'type': quantity.type, 'petroleum_product': quantity.petroleum_product, 'quantity_tonnes': quantity.quantity_tonnes,
                 'value_millions': quantity.value_millions, 'year': quantity.year}

            quantities.append(c)
    else:
        pass

    return Response(quantities)

# Launch Page
def valueQuantityView(request):
    value_quantity = Value_And_Quantity_Of_Imports_Exports.objects.all()

    quantities = []

    if value_quantity:
        for quantity in value_quantity:
            c = {'id': quantity.petroleum_id,'type': quantity.type, 'petroleum_product': quantity.petroleum_product,'quantity_tonnes': quantity.quantity_tonnes,
                 'value_millions': quantity.value_millions, 'year': quantity.year}

            quantities.append(c)
            context = {'quantities': quantities}
    else:
        pass

    return render(request, 'knbs_bi/energy_value_and_quantity_of_imports_exports.html', context)

# Add View
def addValueQuantityView(request):
    return render(request, 'knbs_bi/energy_value_and_quantity_of_imports_exports_add.html')

# Edit View
def editValueQuantityView(request):
    return render(request, 'knbs_bi/energy_value_and_quantity_of_imports_exports_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addValueQuantity(request):
    value_add = Value_And_Quantity_Of_Imports_Exports(type=request.data['type'], petroleum_product=request.data['petroleum'],
                                                      quantity_tonnes=request.data['quantity'], value_millions=request.data['value'],
                                                    year=request.data['year'])
    if value_add:
        value_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editValueQuantity(request):
    value_edit = Value_And_Quantity_Of_Imports_Exports.objects.get(petroleum_id=request.data['petroleum_id'])

    if 'type' in request.data:
        value_edit.type = request.data['type']
    if 'petroleum' in request.data:
        value_edit.petroleum_product = request.data['petroleum']
    if 'quantity' in request.data:
        value_edit.quantity_tonnes = request.data['quantity']
    if 'value' in request.data:
        value_edit.value_millions = request.data['value']
    if 'year' in request.data:
        value_edit.year = request.data['year']

    value_edit.save()
    return Response(status=status.HTTP_201_CREATED)

############################################Petroleum_Supply_And_Demand############################################
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def petroleumSupply(request):
    pet_supply = Petroleum_Supply_And_Demand.objects.all()

    supplies = []

    if pet_supply:
        for supply in pet_supply:

            c = {'type': supply.type, 'petroleum_product': supply.petroleum_product, 'quantity_tonnes': supply.quantity_tonnes,
                 'year': supply.year}

            supplies.append(c)
    else:
        pass

    return Response(supplies)

# Launch Page
def petroleumSupplyView(request):
    pet_supply = Petroleum_Supply_And_Demand.objects.all()

    supplies = []

    if pet_supply:
        for supply in pet_supply:

            c = {'id':supply.petroleum_id, 'type': supply.type, 'petroleum_product': supply.petroleum_product, 'quantity_tonnes': supply.quantity_tonnes,
                 'year': supply.year}

            supplies.append(c)
            context = {'supplies': supplies}
    else:
        pass

    return render(request, 'knbs_bi/energy_petroleum_supply_and_demand.html', context)

# Add View
def addPetroleumSupplyView(request):
    return render(request, 'knbs_bi/energy_petroleum_supply_and_demand_add.html')

# Edit View
def editPetroleumSupplyView(request):
    return render(request, 'knbs_bi/energy_petroleum_supply_and_demand_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addPetroleumSupply(request):
    pet_add = Petroleum_Supply_And_Demand(type=request.data['type'], petroleum_product=request.data['petroleum'],
                                                      quantity_tonnes=request.data['quantity'], year=request.data['year'])
    if pet_add:
        pet_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editPetroleumSupply(request):
    pet_edit = Petroleum_Supply_And_Demand.objects.get(petroleum_id=request.data['petroleum_id'])

    if 'type' in request.data:
        pet_edit.type = request.data['type']
    if 'petroleum' in request.data:
        pet_edit.petroleum_product = request.data['petroleum']
    if 'quantity' in request.data:
        pet_edit.quantity_tonnes = request.data['quantity']
    if 'year' in request.data:
        pet_edit.year = request.data['year']

    pet_edit.save()
    return Response(status=status.HTTP_201_CREATED)

############################################Installed_And_Effective_Capacity_Of_Electricity############################################
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def installedCapacity(request):
    installed_capacity = Installed_And_Effective_Capacity_Of_Electricity.objects.all()

    capacities = []

    if installed_capacity:
        for capacity in installed_capacity:

            c = {'type': capacity.type, 'electricity_source': capacity.electricity_source, 'capacity_megawatts': capacity.capacity_megawatts,
                 'year': capacity.year}

            capacities.append(c)
    else:
        pass

    return Response(capacities)

# Launch Page
def installedCapacityView(request):
    installed_capacity = Installed_And_Effective_Capacity_Of_Electricity.objects.all()

    capacities = []

    if installed_capacity:
        for capacity in installed_capacity:

            c = {'id': capacity.capacity_id, 'type': capacity.type, 'electricity_source': capacity.electricity_source, 'capacity_megawatts': capacity.capacity_megawatts,
                 'year': capacity.year}

            capacities.append(c)
            context = {'capacities': capacities}
    else:
        pass

    return render(request, 'knbs_bi/energy_installed_and_effective_capacity_of_electricity.html', context)

# Add View
def addInstalledCapacityView(request):
    return render(request, 'knbs_bi/energy_installed_and_effective_capacity_of_electricity_add.html')

# Edit View
def editInstalledCapacityView(request):
    return render(request, 'knbs_bi/energy_installed_and_effective_capacity_of_electricity_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addInstalledCapacity(request):
    capacity_add = Installed_And_Effective_Capacity_Of_Electricity(type=request.data['type'], electricity_source=request.data['source'],
                                                      capacity_megawatts=request.data['capacity'], year=request.data['year'])
    if capacity_add:
        capacity_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editInstalledCapacity(request):
    capacity_edit = Installed_And_Effective_Capacity_Of_Electricity.objects.get(capacity_id=request.data['capacity_id'])

    if 'type' in request.data:
        capacity_edit.type = request.data['type']
    if 'source' in request.data:
        capacity_edit.electricity_source = request.data['source']
    if 'capacity' in request.data:
        capacity_edit.capacity_megawatts = request.data['capacity']
    if 'year' in request.data:
        capacity_edit.year = request.data['year']

    capacity_edit.save()
    return Response(status=status.HTTP_201_CREATED)

############################################Generation_And_Imports_Of_Electricity############################################
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def generalImports(request):
    general_imports = Generation_And_Imports_Of_Electricity.objects.all()

    generations = []

    if general_imports:
        for generation in general_imports:

            c = {'type': generation.type, 'electricity_source': generation.electricity_source, 'capacity_megawatts': generation.capacity_megawatts,
                 'year': generation.year}

            generations.append(c)
    else:
        pass

    return Response(generations)

# Launch Page
def generalImportsView(request):
    general_imports = Generation_And_Imports_Of_Electricity.objects.all()

    generations = []

    if general_imports:
        for generation in general_imports:

            c = {'id':generation.electricity_id, 'type': generation.type, 'electricity_source': generation.electricity_source,
                 'capacity_megawatts': generation.capacity_megawatts, 'year': generation.year}

            generations.append(c)
            context = {'generations': generations}
    else:
        pass

    return render(request, 'knbs_bi/energy_generation_and_imports_of_electricity.html', context)

# Add View
def addGeneralImportsView(request):
    return render(request, 'knbs_bi/energy_generation_and_imports_of_electricity_add.html')

# Edit View
def editGeneralImportsView(request):
    return render(request, 'knbs_bi/energy_generation_and_imports_of_electricity_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addGeneralImports(request):
    import_add = Generation_And_Imports_Of_Electricity(type=request.data['type'], electricity_source=request.data['source'],
                                                      capacity_megawatts=request.data['capacity'], year=request.data['year'])
    if import_add:
        import_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editGeneralImports(request):
    import_edit = Generation_And_Imports_Of_Electricity.objects.get(electricity_id=request.data['electricity_id'])

    if 'type' in request.data:
        import_edit.type = request.data['type']
    if 'source' in request.data:
        import_edit.electricity_source = request.data['source']
    if 'capacity' in request.data:
        import_edit.capacity_megawatts = request.data['capacity']
    if 'year' in request.data:
        import_edit.year = request.data['year']

    import_edit.save()
    return Response(status=status.HTTP_201_CREATED)

############################################Electricity_Demand_And_Supply############################################
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def electricityDemand(request):
    elec_demand = Electricity_Demand_And_Supply.objects.all()

    supplies = []

    if elec_demand:
        for supply in elec_demand:

            c = {'demand_supply': supply.demand_supply, 'capacity_megawatts': supply.capacity_megawatts,
                 'year': supply.ye}

            supplies.append(c)
    else:
        pass

    return Response(supplies)

# Launch Page
def electricityDemandView(request):
    elec_demand = Electricity_Demand_And_Supply.objects.all()

    supplies = []

    if elec_demand:
        for supply in elec_demand:

            c = {'id':supply.electricity_id, 'demand_supply': supply.demand_supply, 'capacity_megawatts': supply.capacity_megawatts,
                 'year': supply.year}

            supplies.append(c)
            context = {'supplies': supplies}
    else:
        pass

    return render(request, 'knbs_bi/energy_electricity_demand_and_supply.html', context)

# Add View
def addElectricityDemandView(request):
    return render(request, 'knbs_bi/energy_electricity_demand_and_supply_add.html')

# Edit View
def editElectricityDemandView(request):
    return render(request, 'knbs_bi/energy_electricity_demand_and_supply_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addElectricityDemand(request):
    elec_add = Electricity_Demand_And_Supply(demand_supply=request.data['demand'], capacity_megawatts=request.data['capacity'],
                                                      year=request.data['year'])
    if elec_add:
        elec_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editElectricityDemand(request):
    elec_edit = Electricity_Demand_And_Supply.objects.get(electricity_id=request.data['electricity_id'])

    if 'demand' in request.data:
        elec_edit.demand_supply = request.data['demand']
    if 'capacity' in request.data:
        elec_edit.capacity_megawatts = request.data['capacity']
    if 'year' in request.data:
        elec_edit.year = request.data['year']

    elec_edit.save()
    return Response(status=status.HTTP_201_CREATED)
