from django.shortcuts import render

# Create your views here.

# def agriculture(request):
#     return render(request, template_name="knbs_bi/agriculture.html")
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from agriculture.models import Chemical_Med_Feed_Input, Cooperatives, Gross_Market_Production, Irrigation_Schemes, \
    PriceToProducersForMeatMilk, TotalShareCapital, ValueOfAgriculturalInputs, Land_Potential, Land_Potential_Ids, \
    Area_Under_Sugarcane_Harvested_Production_Avg_Yield, Categories_Of_Agricultural_Land, \
    Production_Area_Average_Yield_Coffee_Type_Of_Grower, Production_Area_Average_Yield_Tea_Type_Grower, \
    Production_Of_Livestock_And_Dairy_Products
from health.models import Counties, SubCounty


def agriculture(request):
    return render(request, template_name='knbs_bi/agriculture.html')

# def validate_decimals(value):
#     try:
#         return round(float(value), 2)
#     except:
#         raise ValidationError(
#             _('%(value)s is not an integer or a float  number'),
#             params={'value': value},
#         )

########################################## Chemical Feeds ##########################################
#Launch Page
def chemicalFeedView(request):
    chemical_feed = Chemical_Med_Feed_Input.objects.all()

    feeds = []

    if chemical_feed:
        for feed in chemical_feed:
            c = {'id':feed.chemical_med_feed_inputs_id, 'year': feed.year, 'cattle_feed': feed.cattle_feed, 'dips_spray_fluids': feed.dips_spray_fluids,
                 'fungicides': feed.fungicides, 'herbicides': feed.herbicides, 'insecticides': feed.insecticides,
                 'other_feeds': feed.other_feeds, 'other_livestock_drugs': feed.other_livestock_drugs,
                 'pig_feed': feed.pig_feed, 'plant_hormones': feed.plant_hormones, 'poultry_feed': feed.poultry_feed,
                 'vaccines': feed.vaccines}
            feeds.append(c)
            context = {'feeds': feeds}
    else:
        pass
    return render(request, 'knbs_bi/agriculture_chemical_med_feed_input.html', context)

#view More
def viewChemFeed(request):
    return render(request, template_name='knbs_bi/agriculture_chemical_med_feed_input_view.html')
#all
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def chemicalFeed(request):
    chemical_feed = Chemical_Med_Feed_Input.objects.all()

    feeds = []

    if chemical_feed:
        for feed in chemical_feed:
            c = {'year': feed.year, 'cattle_feed': feed.cattle_feed, 'dips_spray_fluids': feed.dips_spray_fluids,
                 'fungicides': feed.fungicides, 'herbicides': feed.herbicides, 'insecticides': feed.insecticides,
                 'other_feeds': feed.other_feeds, 'other_livestock_drugs': feed.other_livestock_drugs,
                 'pig_feed': feed.pig_feed, 'plant_hormones': feed.plant_hormones, 'poultry_feed': feed.poultry_feed,
                 'vaccines': feed.vaccines}
            feeds.append(c)
    else:
        pass
    return Response(feeds)

# Add View
def addChemicalFeedView(request):
    return render(request, 'knbs_bi/agriculture_chemical_med_feed_input_add.html')

# Edit View
def editChemicalFeedView(request):
    return render(request, 'knbs_bi/agriculture_chemical_med_feed_input_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addChemicalFeed(request):
    chemical_feed_add = Chemical_Med_Feed_Input(year=request.data['year'], cattle_feed=request.data['cattle'], dips_spray_fluids=request.data['dips'],
                                                           fungicides=request.data['fungicides'], herbicides=request.data['herbicides'], insecticides=request.data['insecticides'],
                                                other_feeds=request.data['feeds'], other_livestock_drugs=request.data['drugs'], pig_feed=request.data['pig_feed'],
                                                plant_hormones=request.data['plant'], poultry_feed=request.data['poultry'], vaccines=request.data['vaccines'])
    if chemical_feed_add:
        chemical_feed_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editChemicalFeed(request):
    chemical_feed_edit = Chemical_Med_Feed_Input.objects.get(chemical_med_feed_inputs_id=request.data['chemical'])

    if 'year' in request.data:
        chemical_feed_edit.year = request.data['year']

    if 'cattle' in request.data:
        chemical_feed_edit.cattle_feed = request.data['cattle']

    if 'dips' in request.data:
        chemical_feed_edit.dips_spray_fluids = request.data['dips']

    if 'fungicides' in request.data:
        chemical_feed_edit.fungicides = request.data['fungicides']
    if 'herbicides' in request.data:
        chemical_feed_edit.herbicides = request.data['herbicides']
    if 'insecticides' in request.data:
        chemical_feed_edit.insecticides = request.data['insecticides']

    if 'feeds' in request.data:
        chemical_feed_edit.other_feeds = request.data['feeds']
    if 'drugs' in request.data:
        chemical_feed_edit.other_livestock_drugs = request.data['drugs']
    if 'pig_feed' in request.data:
        chemical_feed_edit.pig_feed = request.data['pig_feed']
    if 'plant' in request.data:
        chemical_feed_edit.plant_hormones = request.data['plant']
    if 'poultry' in request.data:
        chemical_feed_edit.poultry_feed = request.data['poultry']
    if 'vaccines' in request.data:
        chemical_feed_edit.vaccines = request.data['vaccines']

    chemical_feed_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)
########################################## Cooperatives ##########################################
#Launch Page
def cooperativesView(request):
    coop = Cooperatives.objects.all()

    records = []

    if coop:
        for record in coop:
            c = {'id': record.cooperatives_id, 'year': record.year, 'coffee': record.coffee, 'cotton': record.cotton, 'pyrethrum': record.pyrethrum,
                 'sugar': record.sugar, 'dairy': record.dairy, 'multi_purpose': record.multi_purpose,
                 'farm_purchase': record.farm_purchase, 'fisheries': record.fisheries, 'other_agricultural': record.other_agricultural,
                 'saccos': record.saccos, 'consumer':record.consumer, 'housing': record.housing, 'craftsmen': record.craftsmen,
                 'transport': record.transport, 'other_non_agriculture': record.other_non_agricultur, 'unions': record.unions}
            records.append(c)
            context = {'records': records}
    else:
        pass
    return render(request, 'knbs_bi/agriculture_cooperatives.html', context)

#Add View
def addCooperativesView(request):
    return render(request, template_name='knbs_bi/agriculture_cooperatives_add.html')

#Edit View
def editCooperativesView(request):
    return render(request, template_name='knbs_bi/agriculture_cooperatives_edit.html')

#View More
def viewCooperatives(request):
    return render(request, template_name='knbs_bi/agriculture_cooperatives_view.html')

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def cooperatives(request):
    coop = Cooperatives.objects.all()

    records = []

    if coop:
        for record in coop:
            c = {'year': record.year, 'coffee': record.coffee, 'cotton': record.cotton, 'pyrethrum': record.pyrethrum,
                 'sugar': record.sugar, 'dairy': record.dairy, 'multi_purpose': record.multi_purpose,
                 'farm_purchase': record.farm_purchase, 'fisheries': record.fisheries, 'other_agricultural': record.other_agricultural,
                 'saccos': record.saccos, 'consumer':record.consumer, 'housing': record.housing, 'craftsmen': record.craftsmen,
                 'transport': record.transport, 'other_non_agriculture': record.other_non_agricultur, 'unions': record.unions}
            records.append(c)
    else:
        pass
    return Response(records)

#Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addCooperatives(request):
    coop_add = Cooperatives(year=request.data['year'], coffee=request.data['coffee'], cotton=request.data['cotton'],
                            pyrethrum=request.data['pyrethrum'], sugar=request.data['sugar'], dairy=request.data['dairy'],
                            multi_purpose=request.data['purpose'], farm_purchase=request.data['farm'], fisheries=request.data['fisheries'],
                            other_agricultural=request.data['agricultural'], saccos=request.data['saccos'], consumer=request.data['consumer'],
                            housing=request.data['housing'], craftsmen=request.data['craftsmen'], transport=request.data['transport'],
                            other_non_agricultur=request.data['non_agric'], unions=request.data['unions'])
    if coop_add:
        coop_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editCooperatives(request):
    coop_edit = Cooperatives.objects.get(cooperatives_id=request.data['cooperative'])

    if 'year' in request.data:
        coop_edit.year = request.data['year']

    if 'coffee' in request.data:
        coop_edit.coffee = request.data['coffee']

    if 'cotton' in request.data:
        coop_edit.cotton = request.data['cotton']

    if 'pyrethrum' in request.data:
        coop_edit.pyrethrum = request.data['pyrethrum']
    if 'sugar' in request.data:
        coop_edit.sugar = request.data['sugar']
    if 'dairy' in request.data:
        coop_edit.dairy = request.data['dairy']
    if 'purpose' in request.data:
        coop_edit.multi_purpose = request.data['purpose']
    if 'farm' in request.data:
        coop_edit.farm_purchase = request.data['farm']
    if 'fisheries' in request.data:
        coop_edit.fisheries = request.data['fisheries']

    if 'agricultural' in request.data:
        coop_edit.other_agricultural = request.data['agricultural']
    if 'saccos' in request.data:
        coop_edit.saccos = request.data['saccos']
    if 'consumer' in request.data:
        coop_edit.consumer = request.data['consumer']
    if 'housing' in request.data:
        coop_edit.housing = request.data['housing']
    if 'craftsmen' in request.data:
        coop_edit.craftsmen = request.data['craftsmen']
    if 'transport' in request.data:
        coop_edit.transport = request.data['transport']
    if 'non_agric' in request.data:
        coop_edit.other_non_agricultur = request.data['non_agric']
    if 'unions' in request.data:
        coop_edit.unions = request.data['unions']

    coop_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

########################################## Gross Market Production ##########################################
#Launch Page
def marketProductionView(request):
    mar_prod = Gross_Market_Production.objects.all()

    productions = []

    if mar_prod:
        for production in mar_prod:
            c = {'id': production.gross_market_production_at_constant_id, 'year': production.year, 'cattle_and_calves_for_slaughter': production.cattle_and_calves_for_slaughter,
                 'sugarcane': production.sugarcane, 'vegetables': production.vegetables, 'cutflowers': production.cutflowers,
                 'tea': production.tea, 'fruits': production.fruits, 'poultry_and_eggs': production.poultry_and_eggs,
                 'wheat': production.wheat, 'sheep_goats_and_lambs_for_slaughter': production.sheep_goats_and_lambs_for_slaughter,
                 'maize': production.maize, 'coffee': production.coffee, 'barley': production.barley,
                 'dairy_products':production.dairy_products, 'cotton': production.cotton, 'hides_and_skins': production.hides_and_skins,
                 'other_cereals': production.other_cereals, 'other_temporary_crops': production.other_temporary_crops,
                 'pigs_for_slaughter': production.pigs_for_slaughter, 'wool': production.wool, 'potatoes': production.potatoes,
                 'pulses': production.pulses, 'pyrethrum': production.pyrethrum, 'rice_paddy': production.rice_paddy,
                 'tobacco': production.tobacco, 'total_crops': production.total_crops, 'grand_total': production.grand_total}
            productions.append(c)
            context = {'productions':productions}
    else:
        pass
    return render(request, 'knbs_bi/agriculture_gross_market_production.html', context)

#Add View
def addMarketProductionView(request):
    return render(request, template_name='knbs_bi/agriculture_gross_market_production_add.html')

#Edit View
def editMarketProductionView(request):
    return render(request, template_name='knbs_bi/agriculture_gross_market_production_edit.html')

#View More
def viewMarketProduction(request):
    return render(request, template_name='knbs_bi/agriculture_gross_market_production_view.html')

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def marketProduction(request):
    mar_prod = Gross_Market_Production.objects.all()

    productions = []

    if mar_prod:
        for production in mar_prod:
            c = {'year': production.year, 'cattle_and_calves_for_slaughter': production.cattle_and_calves_for_slaughter,
                 'sugarcane': production.sugarcane, 'vegetables': production.vegetables, 'cutflowers': production.cutflowers,
                 'tea': production.tea, 'fruits': production.fruits, 'poultry_and_eggs': production.poultry_and_eggs,
                 'wheat': production.wheat, 'sheep_goats_and_lambs_for_slaughter': production.sheep_goats_and_lambs_for_slaughter,
                 'maize': production.maize, 'coffee': production.coffee, 'barley': production.barley,
                 'dairy_products':production.dairy_products, 'cotton': production.cotton, 'hides_and_skins': production.hides_and_skins,
                 'other_cereals': production.other_cereals, 'other_temporary_crops': production.other_temporary_crops,
                 'pigs_for_slaughter': production.pigs_for_slaughter, 'wool': production.wool, 'potatoes': production.potatoes,
                 'pulses': production.pulses, 'pyrethrum': production.pyrethrum, 'rice_paddy': production.rice_paddy,
                 'tobacco': production.tobacco, 'total_crops': production.total_crops, 'grand_total': production.grand_total}
            productions.append(c)
    else:
        pass
    return Response(productions)

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addMarketProduction(request):
    prod_add = Gross_Market_Production(year=request.data['year'], cattle_and_calves_for_slaughter=request.data['cattle'],
                                       sugarcane=request.data['sugarcane'], vegetables=request.data['vegetables'],
                                       cutflowers=request.data['cutflowers'], tea=request.data['tea'],
                                       fruits=request.data['fruits'], poultry_and_eggs=request.data['poultry'],
                                       wheat=request.data['wheat'], sheep_goats_and_lambs_for_slaughter=request.data['sheep'],
                                       maize=request.data['maize'], coffee=request.data['coffee'],
                                       barley=request.data['barley'], dairy_products=request.data['dairy'],
                                       cotton=request.data['cotton'], hides_and_skins=request.data['hides'],
                                       other_cereals=request.data['cereals'], other_temporary_crops=request.data['crops'],
                                       pigs_for_slaughter=request.data['pigs'], wool=request.data['wool'],
                                       potatoes=request.data['potatoes'], pulses=request.data['pulses'],
                                       pyrethrum=request.data['pyrethrum'], rice_paddy=request.data['rice'],
                                       tobacco=request.data['tobacco'], total_crops=request.data['total_crops'],
                                       grand_total=request.data['grand_total'])
    if prod_add:
        prod_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editMarketProduction(request):
    prod_edit = Gross_Market_Production.objects.get(gross_market_production_at_constant_id=request.data['gross'])

    if 'year' in request.data:
        prod_edit.year = request.data['year']

    if 'cattle' in request.data:
        prod_edit.cattle_and_calves_for_slaughter = request.data['cattle']

    if 'sugarcane' in request.data:
        prod_edit.sugarcane = request.data['sugarcane']

    if 'vegetables' in request.data:
        prod_edit.vegetables = request.data['vegetables']
    if 'cutflowers' in request.data:
        prod_edit.cutflowers = request.data['cutflowers']
    if 'tea' in request.data:
        prod_edit.tea = request.data['tea']

    if 'fruits' in request.data:
        prod_edit.fruits = request.data['fruits']
    if 'poultry' in request.data:
        prod_edit.poultry_and_eggs = request.data['poultry']
    if 'wheat' in request.data:
        prod_edit.wheat = request.data['wheat']
    if 'sheep' in request.data:
        prod_edit.sheep_goats_and_lambs_for_slaughter = request.data['sheep']
    if 'maize' in request.data:
        prod_edit.maize = request.data['maize']
    if 'coffee' in request.data:
        prod_edit.coffee = request.data['coffee']
    if 'barley' in request.data:
        prod_edit.barley = request.data['barley']
    if 'dairy' in request.data:
        prod_edit.dairy_products = request.data['dairy']
    if 'cotton' in request.data:
        prod_edit.cotton = request.data['cotton']
    if 'hides' in request.data:
        prod_edit.hides_and_skins = request.data['hides']
    if 'cereals' in request.data:
        prod_edit.other_cereals = request.data['cereals']
    if 'crops' in request.data:
        prod_edit.other_temporary_crops = request.data['crops']
    if 'pigs' in request.data:
        prod_edit.pigs_for_slaughter = request.data['pigs']
    if 'wool' in request.data:
        prod_edit.wool = request.data['wool']
    if 'potatoes' in request.data:
        prod_edit.potatoes = request.data['potatoes']
    if 'pulses' in request.data:
        prod_edit.pulses = request.data['pulses']
    if 'pyrethrum' in request.data:
        prod_edit.pyrethrum = request.data['pyrethrum']
    if 'rice' in request.data:
        prod_edit.rice_paddy = request.data['rice']
    if 'tobacco' in request.data:
        prod_edit.tobacco = request.data['tobacco']
    if 'total_crops' in request.data:
        prod_edit.total_crops = request.data['total_crops']
    if 'grand_total' in request.data:
        prod_edit.grand_total = request.data['grand_total']

    prod_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

########################################## Irrigation Schemes##########################################
#Launch Page
def irrigationSchemesView(request):
    irrigation = Irrigation_Schemes.objects.all()

    schemes = []

    if irrigation:
        for scheme in irrigation:
            c = {'id': scheme.irrigation_schemes_id, 'ahero_gross_value_of_crop_millions': scheme.ahero_gross_value_of_crop_millions,
                 'ahero_hectares_cropped': scheme.ahero_hectares_cropped,
                 'ahero_number_of_plots_holders': scheme.ahero_number_of_plots_holders, 'ahero_paddy_yields_tonnes': scheme.ahero_paddy_yields_tonnes,
                 'ahero_payments_to_plot_holders_millions': scheme.ahero_payments_to_plot_holders_millions, 'all_schemes_gross_value_of_crop_millions': scheme.all_schemes_gross_value_of_crop_millions,
                 'all_schemes_hectares_cropped': scheme.all_schemes_hectares_cropped, 'all_schemes_number_of_plots_holders': scheme.all_schemes_number_of_plots_holders,
                 'all_schemes_paddy_yields_tonnes': scheme.all_schemes_paddy_yields_tonnes, 'all_schemes_payments_to_plot_holders_millions':scheme.all_schemes_payments_to_plot_holders_millions,
                 'bunyala_gross_value_of_crop_millions': scheme.bunyala_gross_value_of_crop_millions, 'bunyala_hectares_cropped': scheme.bunyala_hectares_cropped,
                 'bunyala_number_of_plots_holders': scheme.bunyala_number_of_plots_holders, 'bunyala_paddy_yields_tonnes': scheme.bunyala_paddy_yields_tonnes,
                 'bunyala_payments_to_plot_holders_millions': scheme.bunyala_payments_to_plot_holders_millions, 'mwea_gross_value_of_crop_millions':scheme.mwea_gross_value_of_crop_millions,
                 'mwea_hectares_cropped': scheme.mwea_hectares_cropped, 'mwea_number_of_plots_holders': scheme.mwea_number_of_plots_holders,
                 'mwea_paddy_yields_tonnes': scheme.mwea_paddy_yields_tonnes, 'mwea_payments_to_plot_holders_million': scheme.mwea_payments_to_plot_holders_million,
                 'perkerra_gross_value_of_crop_millions': scheme.perkerra_gross_value_of_crop_millions, 'perkerra_hectares_cropped': scheme.perkerra_hectares_cropped,
                 'perkerra_number_of_plots_holders': scheme.perkerra_number_of_plots_holders, 'perkerra_payments_to_plot_holders_millions': scheme.perkerra_payments_to_plot_holders_millions,
                 'perkerra_seed_maize_tonnes': scheme.perkerra_seed_maize_tonnes, 'west_kano_gross_value_of_crop_millions': scheme.west_kano_gross_value_of_crop_millions,
                 'west_kano_hectares_cropped': scheme.west_kano_hectares_cropped, 'west_kano_number_of_plots_holders': scheme.west_kano_number_of_plots_holders,
                 'west_kano_paddy_yields_tonnes': scheme.west_kano_paddy_yields_tonnes, 'west_kano_payments_to_plot_holders_millions': scheme.west_kano_payments_to_plot_holders_millions,
                 'year': scheme.year}
            schemes.append(c)
            context = {'schemes': schemes}
    else:
        pass
    return render(request, 'knbs_bi/agriculture_irrigation_schemes.html', context)

#Add View
def addIrrigationSchemesView(request):
    return render(request, template_name='knbs_bi/agriculture_irrigation_schemes_add.html')

#Edit View
def editIrrigationSchemesView(request):
    return render(request, template_name='knbs_bi/agriculture_irrigation_schemes_edit.html')

#View More
def viewIrrigationSchemes(request):
    return render(request, template_name='knbs_bi/agriculture_irrigation_schemes_view.html')


@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def irrigationSchemes(request):
    irrigation = Irrigation_Schemes.objects.all()

    schemes = []

    if irrigation:
        for scheme in irrigation:
            c = {'ahero_gross_value_of_crop_millions': scheme.ahero_gross_value_of_crop_millions,
                 'ahero_hectares_cropped': scheme.ahero_hectares_cropped,
                 'ahero_number_of_plots_holders': scheme.ahero_number_of_plots_holders, 'ahero_paddy_yields_tonnes': scheme.ahero_paddy_yields_tonnes,
                 'ahero_payments_to_plot_holders_millions': scheme.ahero_payments_to_plot_holders_millions, 'all_schemes_gross_value_of_crop_millions': scheme.all_schemes_gross_value_of_crop_millions,
                 'all_schemes_hectares_cropped': scheme.all_schemes_hectares_cropped, 'all_schemes_number_of_plots_holders': scheme.all_schemes_number_of_plots_holders,
                 'all_schemes_paddy_yields_tonnes': scheme.all_schemes_paddy_yields_tonnes, 'all_schemes_payments_to_plot_holders_millions':scheme.all_schemes_payments_to_plot_holders_millions,
                 'bunyala_gross_value_of_crop_millions': scheme.bunyala_gross_value_of_crop_millions, 'bunyala_hectares_cropped': scheme.bunyala_hectares_cropped,
                 'bunyala_number_of_plots_holders': scheme.bunyala_number_of_plots_holders, 'bunyala_paddy_yields_tonnes': scheme.bunyala_paddy_yields_tonnes,
                 'bunyala_payments_to_plot_holders_millions': scheme.bunyala_payments_to_plot_holders_millions, 'mwea_gross_value_of_crop_millions':scheme.mwea_gross_value_of_crop_millions,
                 'mwea_hectares_cropped': scheme.mwea_hectares_cropped, 'mwea_number_of_plots_holders': scheme.mwea_number_of_plots_holders,
                 'mwea_paddy_yields_tonnes': scheme.mwea_paddy_yields_tonnes, 'mwea_payments_to_plot_holders_million': scheme.mwea_payments_to_plot_holders_million,
                 'perkerra_gross_value_of_crop_millions': scheme.perkerra_gross_value_of_crop_millions, 'perkerra_hectares_cropped': scheme.perkerra_hectares_cropped,
                 'perkerra_number_of_plots_holders': scheme.perkerra_number_of_plots_holders, 'perkerra_payments_to_plot_holders_millions': scheme.perkerra_payments_to_plot_holders_millions,
                 'perkerra_seed_maize_tonnes': scheme.perkerra_seed_maize_tonnes, 'west_kano_gross_value_of_crop_millions': scheme.west_kano_gross_value_of_crop_millions,
                 'west_kano_hectares_cropped': scheme.west_kano_hectares_cropped, 'west_kano_number_of_plots_holders': scheme.west_kano_number_of_plots_holders,
                 'west_kano_paddy_yields_tonnes': scheme.west_kano_paddy_yields_tonnes, 'west_kano_payments_to_plot_holders_millions': scheme.west_kano_payments_to_plot_holders_millions,
                 'year': scheme.year}
            schemes.append(c)
    else:
        pass
    return Response(schemes)

#Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addIrrigationSchemes(request):
    scheme_add = Irrigation_Schemes(ahero_gross_value_of_crop_millions=request.data['ahero_gross'],
                                    ahero_hectares_cropped=request.data['ahero_hectares'], ahero_number_of_plots_holders=request.data['ahero_plots'],
                                    ahero_paddy_yields_tonnes=request.data['ahero_paddy'], ahero_payments_to_plot_holders_millions=request.data['ahero_pay'],
                                    all_schemes_gross_value_of_crop_millions=request.data['all_gross'], all_schemes_hectares_cropped=request.data['all_hectares'],
                                    all_schemes_number_of_plots_holders=request.data['all_plots'], all_schemes_paddy_yields_tonnes=request.data['all_paddy'],
                                    all_schemes_payments_to_plot_holders_millions=request.data['all_pay'], bunyala_gross_value_of_crop_millions=request.data['bunyala_gross'],
                                    bunyala_hectares_cropped=request.data['bunyala_hectares'], bunyala_number_of_plots_holders=request.data['bunyala_plots'],
                                    bunyala_paddy_yields_tonnes=request.data['bunyala_paddy'], bunyala_payments_to_plot_holders_millions=request.data['bunyala_pay'],
                                    mwea_gross_value_of_crop_millions=request.data['mwea_gross'], mwea_hectares_cropped=request.data['mwea_hectares'],
                                    mwea_number_of_plots_holders=request.data['mwea_plots'], mwea_paddy_yields_tonnes=request.data['mwea_paddy'],
                                    mwea_payments_to_plot_holders_million=request.data['mwea_pay'], perkerra_gross_value_of_crop_millions=request.data['perkerra_gross'],
                                    perkerra_hectares_cropped=request.data['perkerra_hectares'], perkerra_number_of_plots_holders=request.data['perkerra_plots'],
                                    perkerra_payments_to_plot_holders_millions=request.data['perkerra_pay'], perkerra_seed_maize_tonnes=request.data['perkerra_seed'],
                                    west_kano_gross_value_of_crop_millions=request.data['west_gross'], west_kano_hectares_cropped=request.data['west_hectares'],
                                    west_kano_number_of_plots_holders=request.data['west_plots'], west_kano_paddy_yields_tonnes=request.data['west_paddy'],
                                    west_kano_payments_to_plot_holders_millions=request.data['west_pay'], year=request.data['year'], )
    if scheme_add:
        scheme_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editIrrigationSchemes(request):
    scheme_edit = Irrigation_Schemes.objects.get(irrigation_schemes_id=request.data['irrigation'])

    if 'ahero_gross' in request.data:
        scheme_edit.ahero_gross_value_of_crop_millions = request.data['ahero_gross']

    if 'ahero_hectares' in request.data:
        scheme_edit.ahero_hectares_cropped = request.data['ahero_hectares']

    if 'ahero_plots' in request.data:
        scheme_edit.ahero_number_of_plots_holders = request.data['ahero_plots']
    if 'ahero_paddy' in request.data:
        scheme_edit.ahero_paddy_yields_tonnes = request.data['ahero_paddy']
    if 'ahero_pay' in request.data:
        scheme_edit.ahero_payments_to_plot_holders_millions = request.data['ahero_pay']

    if 'all_gross' in request.data:
        scheme_edit.all_schemes_gross_value_of_crop_millions = request.data['all_gross']
    if 'all_hectares' in request.data:
        scheme_edit.all_schemes_hectares_cropped = request.data['all_hectares']
    if 'all_plots' in request.data:
        scheme_edit.all_schemes_number_of_plots_holders = request.data['all_plots']
    if 'all_paddy' in request.data:
        scheme_edit.all_schemes_paddy_yields_tonnes = request.data['all_paddy']
    if 'all_pay' in request.data:
        scheme_edit.all_schemes_payments_to_plot_holders_millions = request.data['all_pay']
    if 'bunyala_gross' in request.data:
        scheme_edit.bunyala_gross_value_of_crop_millions = request.data['bunyala_gross']
    if 'bunyala_hectares' in request.data:
        scheme_edit.bunyala_hectares_cropped = request.data['bunyala_hectares']
    if 'bunyala_plots' in request.data:
        scheme_edit.bunyala_number_of_plots_holders = request.data['bunyala_plots']
    if 'bunyala_paddy' in request.data:
        scheme_edit.bunyala_paddy_yields_tonnes = request.data['bunyala_paddy']
    if 'bunyala_pay' in request.data:
        scheme_edit.bunyala_payments_to_plot_holders_millions = request.data['bunyala_pay']
    if 'mwea_gross' in request.data:
        scheme_edit.mwea_gross_value_of_crop_millions = request.data['mwea_gross']
    if 'mwea_hectares' in request.data:
        scheme_edit.mwea_hectares_cropped = request.data['mwea_hectares']
    if 'mwea_plots' in request.data:
        scheme_edit.mwea_number_of_plots_holders = request.data['mwea_plots']
    if 'mwea_paddy' in request.data:
        scheme_edit.mwea_paddy_yields_tonnes = request.data['mwea_paddy']
    if 'mwea_pay' in request.data:
        scheme_edit.mwea_payments_to_plot_holders_million = request.data['mwea_pay']
    if 'perkerra_gross' in request.data:
        scheme_edit.perkerra_gross_value_of_crop_millions = request.data['perkerra_gross']
    if 'perkerra_hectares' in request.data:
        scheme_edit.perkerra_hectares_cropped = request.data['perkerra_hectares']
    if 'perkerra_plots' in request.data:
        scheme_edit.perkerra_number_of_plots_holders = request.data['perkerra_plots']
    if 'perkerra_pay' in request.data:
        scheme_edit.perkerra_payments_to_plot_holders_millions = request.data['perkerra_pay']
    if 'perkerra_seed' in request.data:
        scheme_edit.perkerra_seed_maize_tonnes = request.data['perkerra_seed']
    if 'west_gross' in request.data:
        scheme_edit.west_kano_gross_value_of_crop_millions = request.data['west_gross']
    if 'west_hectares' in request.data:
        scheme_edit.west_kano_hectares_cropped = request.data['west_hectares']
    if 'west_plots' in request.data:
        scheme_edit.west_kano_number_of_plots_holders = request.data['west_plots']
    if 'west_paddy' in request.data:
        scheme_edit.west_kano_paddy_yields_tonnes = request.data['west_paddy']
    if 'west_pay' in request.data:
        scheme_edit.west_kano_payments_to_plot_holders_millions = request.data['west_pay']
    if 'year' in request.data:
        scheme_edit.year = request.data['year']

    scheme_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)


########################################## Price Meat Milk ##########################################
# Launch Page
def viewPriceMeatMilk(request):
    meat_milk = PriceToProducersForMeatMilk.objects.all()

    prices = []

    if meat_milk:
        for price in meat_milk:
            c = {'id': price.price_to_producers_for_meat_milk_id, 'year': price.year, 'beef_third_grade_per_kg': price.beef_third_grade_per_kg,
                 'pig_meat_per_kg': price.pig_meat_per_kg, 'whole_milk_per_litre': price.whole_milk_per_litre}
            prices.append(c)
            context = {'prices': prices}
    return render(request, 'knbs_bi/agriculture_price_to_producers_for_meat_milk.html', context)

#Price Meat Milk Add View
def addPriceMeatMilkView(request):
    return render(request, template_name='knbs_bi/agriculture_price_to_producers_for_meat_milk_add.html')

#Price Meat Milk View
def editPriceMeatMilkView(request):
    return render(request, 'knbs_bi/agriculture_price_to_producers_for_meat_milk_edit.html')

#All Price Meat Milk
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def priceMeatMilk(request):
    meat_milk = PriceToProducersForMeatMilk.objects.all()

    prices = []

    if meat_milk:
        for price in meat_milk:
            c = {'year': price.year, 'beef_third_grade_per_kg': price.beef_third_grade_per_kg,
                 'pig_meat_per_kg': price.pig_meat_per_kg, 'whole_milk_per_litre': price.whole_milk_per_litre}
            prices.append(c)
    else:
        pass
    return Response(prices)


# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addPriceMeatMilk(request):
    meat_milk_add = PriceToProducersForMeatMilk(year=request.data['year'], beef_third_grade_per_kg=request.data['beef'],
                                                pig_meat_per_kg=request.data['pig'], whole_milk_per_litre=request.data['milk'])
    if meat_milk_add:
        meat_milk_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editPriceMeatMilk(request):
    meat_milk_edit = PriceToProducersForMeatMilk.objects.get(price_to_producers_for_meat_milk_id=request.data['price'])

    if 'year' in request.data:
        meat_milk_edit.year = request.data['year']
    if 'beef' in request.data:
        meat_milk_edit.beef_third_grade_per_kg = request.data['beef']
    if 'pig' in request.data:
        meat_milk_edit.pig_meat_per_kg = request.data['pig']
    if 'milk' in request.data:
        meat_milk_edit.whole_milk_per_litre = request.data['milk']

    meat_milk_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)


########################################## Total Share Capital ##########################################
#Launch Page
def shareCapitalView(request):
    share_capital = TotalShareCapital.objects.all()

    shares = []

    if share_capital:
        for share in share_capital:
            c = {'id': share.total_share_capital_id, 'year': share.year, 'coffee': share.coffee, 'cotton': share.cotton, 'pyrethrum': share.pyrethrum,
                 'sugar': share.sugar, 'dairy': share.dairy, 'multi_purpose': share.multi_purpose, 'farm_purchase': share.farm_purchase,
                 'fisheries': share.fisheries, 'other_agricultural': share.other_agricultural, 'total_agriculture': share.total_agriculture,
                 'saccos': share.saccos, 'consumer': share.consumer, 'housing': share.housing, 'craftsmen': share.craftsmen,
                 'transport': share.transport, 'other_non_agricultural': share.other_non_agricultural, 'total_non_agricultural': share.total_non_agricultural,
                 'unions': share.unions}
            shares.append(c)
            context = {'shares': shares}
    else:
        pass
    return render(request, 'knbs_bi/agriculture_total_share_capital.html', context)

#Add View
def addShareCapitalView(request):
    return render(request, template_name='knbs_bi/agriculture_total_share_capital_add.html')

#Edit View
def editShareCapitalView(request):
    return render(request, template_name='knbs_bi/agriculture_total_share_capital_edit.html')

#View More
def viewShareCapital(request):
    return render(request, template_name='knbs_bi/agriculture_total_share_capital_view.html')

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def shareCapital(request):
    share_capital = TotalShareCapital.objects.all()

    shares = []

    if share_capital:
        for share in share_capital:
            c = {'year': share.year, 'coffee': share.coffee, 'cotton': share.cotton, 'pyrethrum': share.pyrethrum,
                 'sugar': share.sugar, 'dairy': share.dairy, 'multi_purpose': share.multi_purpose, 'farm_purchase': share.farm_purchase,
                 'fisheries': share.fisheries, 'other_agricultural': share.other_agricultural, 'total_agriculture': share.total_agriculture,
                 'saccos': share.saccos, 'consumer': share.consumer, 'housing': share.housing, 'craftsmen': share.craftsmen,
                 'transport': share.transport, 'other_non_agricultural': share.other_non_agricultural, 'total_non_agricultural': share.total_non_agricultural,
                 'unions': share.unions}
            shares.append(c)
    else:
        pass
    return Response(shares)

#Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addShareCapital(request):
    capital_add = TotalShareCapital(year=request.data['year'], coffee=request.data['coffee'], cotton=request.data['cotton'],
                            pyrethrum=request.data['pyrethrum'], sugar=request.data['sugar'], dairy=request.data['dairy'],
                            multi_purpose=request.data['purpose'], farm_purchase=request.data['farm'], fisheries=request.data['fisheries'],
                            other_agricultural=request.data['agricultural'], total_agriculture=request.data['total_agriculture'], saccos=request.data['saccos'],
                            consumer=request.data['consumer'],housing=request.data['housing'], craftsmen=request.data['craftsmen'],
                            transport=request.data['transport'],other_non_agricultural=request.data['non_agric'], total_non_agricultural=request.data['total_non'],
                            unions=request.data['unions'] )
    if capital_add:
        capital_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editShareCapital(request):
    capital_edit = TotalShareCapital.objects.get(total_share_capital_id=request.data['capital'])

    if 'year' in request.data:
        capital_edit.year = request.data['year']

    if 'coffee' in request.data:
        capital_edit.coffee = request.data['coffee']

    if 'cotton' in request.data:
        capital_edit.cotton = request.data['cotton']

    if 'pyrethrum' in request.data:
        capital_edit.pyrethrum = request.data['pyrethrum']
    if 'sugar' in request.data:
        capital_edit.sugar = request.data['sugar']
    if 'dairy' in request.data:
        capital_edit.dairy = request.data['dairy']
    if 'purpose' in request.data:
        capital_edit.multi_purpose = request.data['purpose']
    if 'farm' in request.data:
        capital_edit.farm_purchase = request.data['farm']
    if 'fisheries' in request.data:
        capital_edit.fisheries = request.data['fisheries']

    if 'agricultural' in request.data:
        capital_edit.other_agricultural = request.data['agricultural']
    if 'total_agriculture' in request.data:
        capital_edit.total_agriculture = request.data['total_agriculture']
    if 'saccos' in request.data:
        capital_edit.saccos = request.data['saccos']
    if 'consumer' in request.data:
        capital_edit.consumer = request.data['consumer']
    if 'housing' in request.data:
        capital_edit.housing = request.data['housing']
    if 'craftsmen' in request.data:
        capital_edit.craftsmen = request.data['craftsmen']
    if 'transport' in request.data:
        capital_edit.transport = request.data['transport']
    if 'non_agric' in request.data:
        capital_edit.other_non_agricultural = request.data['non_agric']
    if 'total_non' in request.data:
        capital_edit.total_non_agricultural = request.data['total_non']
    if 'unions' in request.data:
        capital_edit.unions = request.data['unions']

    capital_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

########################################## Agricultural Inputs ##########################################
#Launch Page
def agriculturalInputsView(request):
    agricultural = ValueOfAgriculturalInputs.objects.all()

    values = []

    if agricultural:
        for value in agricultural:
            c = {'id': value.value_of_agricultural_inputs_id, 'year': value.year, 'accounting_secretarial_and_auditing_services': value.accounting_secretarial_and_auditing_services,
                 'aerial_spraying': value.aerial_spraying, 'artificial_insemination': value.artificial_insemination, 'bags': value.bags,
                 'farm_planning_and_survey_services': value.farm_planning_and_survey_services, 'fertilizers': value.fertilizers, 'fuel': value.fuel,
                 'government_seed_inspection_services': value.government_seed_inspection_services, 'government_veterinary_inoculation_services': value.government_veterinary_inoculation_services,
                 'insurance': value.insurance, 'livestock_drugs_and_medicines': value.livestock_drugs_and_medicines, 'manufactured_feeds': value.manufactured_feeds,
                 'marketing_research_and_publicity': value.marketing_research_and_publicity, 'office_expenses': value.office_expenses,
                 'other': value.other, 'other_material_inputs': value.other_material_inputs, 'other_agricultural_chemicals': value.other_agricultural_chemicals,
                 'power': value.power, 'private_veterinary_services': value.private_veterinary_services, 'seeds': value.seeds,
                 'small_implements': value.small_implements, 'spares_and_maintenance_of_machinery': value.spares_and_maintenance_of_machinery,
                 'tractor_services': value.tractor_services, 'transportation': value.transportation}
            values.append(c)
            context = {'values': values}
    else:
        pass
    return render(request, 'knbs_bi/agriculture_value_of_agricultural_inputs.html', context)

#Add View
def addAgriculturalInputsView(request):
    return render(request, template_name='knbs_bi/agriculture_value_of_agricultural_inputs_add.html')

#Edit View
def editAgriculturalInputsView(request):
    return render(request, template_name='knbs_bi/agriculture_value_of_agricultural_inputs_edit.html')

#View More
def viewAgriculturalInputs(request):
    return render(request, template_name='knbs_bi/agriculture_value_of_agricultural_inputs_view.html')

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def agriculturalInputs(request):
    agricultural = ValueOfAgriculturalInputs.objects.all()

    values = []

    if agricultural:
        for value in agricultural:
            c = {'year': value.year, 'accounting_secretarial_and_auditing_services': value.accounting_secretarial_and_auditing_services,
                 'aerial_spraying': value.aerial_spraying, 'artificial_insemination': value.artificial_insemination, 'bags': value.bags,
                 'farm_planning_and_survey_services': value.farm_planning_and_survey_services, 'fertilizers': value.fertilizers, 'fuel': value.fuel,
                 'government_seed_inspection_services': value.government_seed_inspection_services, 'government_veterinary_inoculation_services': value.government_veterinary_inoculation_services,
                 'insurance': value.insurance, 'livestock_drugs_and_medicines': value.livestock_drugs_and_medicines, 'manufactured_feeds': value.manufactured_feeds,
                 'marketing_research_and_publicity': value.marketing_research_and_publicity, 'office_expenses': value.office_expenses,
                 'other': value.other, 'other_material_inputs': value.other_material_inputs, 'other_agricultural_chemicals': value.other_agricultural_chemicals,
                 'power': value.power, 'private_veterinary_services': value.private_veterinary_services, 'seeds': value.seeds,
                 'small_implements': value.small_implements, 'spares_and_maintenance_of_machinery': value.spares_and_maintenance_of_machinery,
                 'tractor_services': value.tractor_services, 'transportation': value.transportation}
            values.append(c)
    else:
        pass
    return Response(values)

#Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addAgriculturalInputs(request):
    input_add = ValueOfAgriculturalInputs(year=request.data['year'], accounting_secretarial_and_auditing_services=request.data['accounting'],
                            aerial_spraying=request.data['aerial'], artificial_insemination=request.data['artificial'],
                            bags=request.data['bags'], farm_planning_and_survey_services=request.data['farm'],
                            fertilizers=request.data['fertilizers'], fuel=request.data['fuel'],
                            government_seed_inspection_services=request.data['seed'], government_veterinary_inoculation_services=request.data['veterinary'],
                            insurance=request.data['insurance'], livestock_drugs_and_medicines=request.data['livestock'],
                            manufactured_feeds=request.data['manufactured'], marketing_research_and_publicity=request.data['marketing'],
                            office_expenses=request.data['office'], other=request.data['other'],
                            other_material_inputs=request.data['material'], other_agricultural_chemicals=request.data['agricultural'],
                            power=request.data['power'], private_veterinary_services=request.data['private'],
                            seeds=request.data['seeds'], small_implements=request.data['small'],
                            spares_and_maintenance_of_machinery=request.data['spares'], tractor_services=request.data['tractor'],
                            transportation=request.data['transportation'])
    if input_add:
        input_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editAgriculturalInputs(request):
    input_edit = ValueOfAgriculturalInputs.objects.get(value_of_agricultural_inputs_id=request.data['value'])

    if 'year' in request.data:
        input_edit.year = request.data['year']

    if 'accounting' in request.data:
        input_edit.accounting_secretarial_and_auditing_services = request.data['accounting']

    if 'aerial' in request.data:
        input_edit.aerial_spraying = request.data['aerial']

    if 'artificial' in request.data:
        input_edit.artificial_insemination = request.data['artificial']
    if 'bags' in request.data:
        input_edit.bags = request.data['bags']
    if 'farm' in request.data:
        input_edit.farm_planning_and_survey_services = request.data['farm']
    if 'fertilizers' in request.data:
        input_edit.fertilizers = request.data['fertilizers']
    if 'fuel' in request.data:
        input_edit.fuel = request.data['fuel']
    if 'seed' in request.data:
        input_edit.government_seed_inspection_services = request.data['seed']

    if 'veterinary' in request.data:
        input_edit.government_veterinary_inoculation_services = request.data['veterinary']
    if 'insurance' in request.data:
        input_edit.insurance = request.data['insurance']
    if 'livestock' in request.data:
        input_edit.livestock_drugs_and_medicines = request.data['livestock']
    if 'manufactured' in request.data:
        input_edit.manufactured_feeds = request.data['manufactured']
    if 'marketing' in request.data:
        input_edit.marketing_research_and_publicity = request.data['marketing']
    if 'office' in request.data:
        input_edit.office_expenses = request.data['office']
    if 'other' in request.data:
        input_edit.other = request.data['other']
    if 'material' in request.data:
        input_edit.other_material_inputs = request.data['material']
    if 'agricultural' in request.data:
        input_edit.other_agricultural_chemicals = request.data['agricultural']
    if 'unions' in request.data:
        input_edit.unions = request.data['unions']
    if 'agricultural' in request.data:
        input_edit.other_agricultural = request.data['agricultural']
    if 'power' in request.data:
        input_edit.power = request.data['power']
    if 'private' in request.data:
        input_edit.private_veterinary_services = request.data['private']
    if 'seeds' in request.data:
        input_edit.seeds = request.data['seeds']
    if 'small' in request.data:
        input_edit.small_implements = request.data['small']
    if 'spares' in request.data:
        input_edit.spares_and_maintenance_of_machinery = request.data['spares']
    if 'tractor' in request.data:
        input_edit.tractor_services = request.data['tractor']
    if 'transportation' in request.data:
        input_edit.transportation = request.data['transportation']

    input_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)


########################################## Land Potential ##########################################
# Launch Page
def viewLandPotential(request):
    land_potential = Land_Potential.objects.all()

    pieces = []

    if land_potential:
        for piece in land_potential:
            county = Counties.objects.get(county_id=piece.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=piece.subcounty_id)
            potential = Land_Potential_Ids.objects.get(potential_id=piece.potential_id)

            if subcounty:
                for sc in subcounty:
                    c = {'id': piece.land_id, 'county': county.county_name, 'subcounty': sc.subcounty_name,
                         'potential': potential.landPotential, 'value': piece.value}
                    pieces.append(c)
                    context = {'pieces': pieces}
    return render(request, 'knbs_bi/agriculture_land_potential.html', context)

# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def landPotential(request):
    land_potential = Land_Potential.objects.all()

    pieces = []

    if land_potential:
        for piece in land_potential:
            county = Counties.objects.get(county_id=piece.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=piece.subcounty_id)
            potential = Land_Potential_Ids.objects.get(potential_id=piece.potential_id)

            if subcounty:
                for sc in subcounty:
                    c = {'county': county.county_name, 'subcounty': sc.subcounty_name,
                         'potential': potential.landPotential, 'value': piece.value}
                    pieces.append(c)
    else:
        pass

    return Response(pieces)

# Add View
def addLandPotentialView(request):
    all_counties = Counties.objects.all()
    subcounty = SubCounty.objects.all()
    potential = Land_Potential_Ids.objects.all()
    context = {'counties': all_counties, 'sub': subcounty, 'potential': potential}
    return render(request, 'knbs_bi/agriculture_land_potential_add.html', context)


# Edit View
def editLandPotentialView(request):
    all_counties = Counties.objects.all()
    subcounty = SubCounty.objects.all()
    potential = Land_Potential_Ids.objects.all()
    context = {'counties': all_counties, 'sub': subcounty, 'potential': potential}
    return render(request, 'knbs_bi/agriculture_land_potential_edit.html', context)


# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addLandPotential(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    subcounty = SubCounty.objects.get(subcounty_name=request.data['sub_county'])
    potential = Land_Potential_Ids.objects.get(landPotential=request.data['potential'])

    if counties and subcounty and potential:
        kaunti = counties.county_id
        sub_kaunti = subcounty.subcounty_id
        pot = potential.potential_id

        land_potential_add = Land_Potential(county_id=kaunti, subcounty_id=sub_kaunti,
                                                             potential_id=pot, value=request.data['value'])
    if land_potential_add:
        land_potential_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editLandPotential(request):
    land_potential_edit = Land_Potential.objects.get(land_id=request.data['land'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            land_potential_edit.county_id = counties.county_id

    if 'sub_county' in request.data:
        subcounty = SubCounty.objects.get(subcounty_name=request.data['sub_county'])
        if subcounty:
            land_potential_edit.subcounty_id = subcounty.subcounty_id

    if 'potential' in request.data:
        potential = Land_Potential_Ids.objects.get(landPotential=request.data['potential'])
        if potential:
            land_potential_edit.potential_id = potential.potential_id

    if 'value' in request.data:
        land_potential_edit.value = request.data['value']


    land_potential_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

########################################## Area Under Sugarcane ##########################################
# Launch Page
def viewAreaSugarcane(request):
    area = Area_Under_Sugarcane_Harvested_Production_Avg_Yield.objects.all()

    productions = []

    if area:
        for production in area:

            c = {'id': production.area_id, 'cane': production.area_under_cane_ha, 'harvested': production.area_harvested_ha,
                'tonnes': production.production_tonnes, 'average': production.average_yield_tonnes_per_ha,
                 'year': production.year}
            productions.append(c)
            context = {'productions': productions}
    return render(request, 'knbs_bi/agriculture_area_under_sugarcane_harvested_production_avg_yield.html', context)

# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def areaSugarcane(request):
    area = Area_Under_Sugarcane_Harvested_Production_Avg_Yield.objects.all()

    productions = []

    if area:
        for production in area:

            c = {'cane': production.area_under_cane_ha, 'harvested': production.area_harvested_ha,
                'tonnes': production.production_tonnes, 'average': production.average_yield_tonnes_per_ha,
                 'year': production.year}
            productions.append(c)
    else:
        pass

    return Response(productions)

# Add View
def addAreaSugarcaneView(request):
    return render(request, 'knbs_bi/agriculture_area_under_sugarcane_harvested_production_avg_yield_add.html')

# Edit View
def editAreaSugarcaneView(request):
    return render(request, 'knbs_bi/agriculture_area_under_sugarcane_harvested_production_avg_yield_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addAreaSugarcane(request):
    area_add = Area_Under_Sugarcane_Harvested_Production_Avg_Yield(area_under_cane_ha = request.data['cane'], area_harvested_ha = request.data['harvested'],
                                                                   production_tonnes = request.data['tonnes'], average_yield_tonnes_per_ha = request.data['average'],
                                                                   year = request.data['year'],)
    if area_add:
        area_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editAreaSugarcane(request):
    area_edit = Area_Under_Sugarcane_Harvested_Production_Avg_Yield.objects.get(area_id = request.data['area'])

    if 'cane' in request.data:
        area_edit.area_under_cane_ha = request.data['cane']

    if 'harvested' in request.data:
        area_edit.area_harvested_ha = request.data['harvested']

    if 'tonnes' in request.data:
        area_edit.production_tonnes = request.data['tonnes']

    if 'average' in request.data:
        area_edit.average_yield_tonnes_per_ha = request.data['average']

    if 'year' in request.data:
        area_edit.year = request.data['year']


    area_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

########################################## Categories of Agricultural Land ##########################################
# Launch Page
def viewAgriculturalLand(request):
    land = Categories_Of_Agricultural_Land.objects.all()

    categories = []

    if land:
        for category in land:
            county = Counties.objects.get(county_id=category.county_id)

            c = {'id': category.land_id, 'county': county.county_name, 'high_potential': category.high_potential,
                 'medium_potential': category.medium_potential, 'low_potential': category.low_potential,
                'total_land': category.total_land, 'all_other_land': category.all_other_land,
                 'total_land_area': category.total_land_area}
            categories.append(c)
            context = {'categories': categories}
    return render(request, 'knbs_bi/agriculture_categories_of_agricultural_land.html', context)

# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def agriculturalLand(request):
    land = Categories_Of_Agricultural_Land.objects.all()

    categories = []

    if land:
        for category in land:
            county = Counties.objects.get(county_id=category.county_id)

            c = {'county': county.county_name, 'high_potential': category.high_potential,
                 'medium_potential': category.medium_potential, 'low_potential': category.low_potential,
                'total_land': category.total_land, 'all_other_land': category.all_other_land,
                 'total_land_area': category.total_land_area}
            categories.append(c)
    else:
        pass

    return Response(categories)

# Add View
def addAgriculturalLandView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/agriculture_categories_of_agricultural_land_add.html', context)

# Edit View
def editAgriculturalLandView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/agriculture_categories_of_agricultural_land_edit.html', context)

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addAgriculturalLand(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id

        land_add = Categories_Of_Agricultural_Land(county_id = kaunti, high_potential = request.data['high_potential'],
                                                   medium_potential = request.data['medium_potential'], low_potential = request.data['low_potential'],
                                                   total_land = request.data['total_land'], all_other_land = request.data['all_other_land'],
                                                   total_land_area = request.data['total_land_area'],)
    if land_add:
        land_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editAgriculturalLand(request):
    land_edit = Categories_Of_Agricultural_Land.objects.get(land_id = request.data['land'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            land_edit.county_id = counties.county_id

    if 'high_potential' in request.data:
        land_edit.high_potential = request.data['high_potential']

    if 'medium_potential' in request.data:
        land_edit.medium_potential = request.data['medium_potential']

    if 'low_potential' in request.data:
        land_edit.low_potential = request.data['low_potential']

    if 'total_land' in request.data:
        land_edit.total_land = request.data['total_land']

    if 'all_other_land' in request.data:
        land_edit.all_other_land = request.data['all_other_land']

    if 'total_land_area' in request.data:
        land_edit.total_land_area = request.data['total_land_area']


    land_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

########################################## Production Area and Average Yield of Coffee ##########################################
# Launch Page
def areaCoffeeView(request):
    area = Production_Area_Average_Yield_Coffee_Type_Of_Grower.objects.all()

    productions = []

    if area:
        for production in area:

            c = {'id': production.category_id, 'category': production.category, 'cooperatives': production.cooperatives,
                'estates': production.estates, 'unit': production.unit,
                 'year': production.year}
            productions.append(c)
            context = {'productions': productions}
    return render(request, 'knbs_bi/agriculture_production_area_average_yield_coffee_type_of_grower.html', context)

# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def areaCoffee(request):
    area = Production_Area_Average_Yield_Coffee_Type_Of_Grower.objects.all()

    productions = []

    if area:
        for production in area:

            c = {'category': production.category, 'cooperatives': production.cooperatives,
                'estates': production.estates, 'unit': production.unit,
                 'year': production.year}
            productions.append(c)
    else:
        pass

    return Response(productions)

# Add View
def addAreaCoffeeView(request):
    return render(request, 'knbs_bi/agriculture_production_area_average_yield_coffee_type_of_grower_add.html')

# Edit View
def editAreaCoffeeView(request):
    return render(request, 'knbs_bi/agriculture_production_area_average_yield_coffee_type_of_grower_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addAreaCoffee(request):
    area_add = Production_Area_Average_Yield_Coffee_Type_Of_Grower(category = request.data['category'], cooperatives = request.data['cooperatives'],
                                                                   estates = request.data['estates'], unit = request.data['unit'],
                                                                   year = request.data['year'],)
    if area_add:
        area_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editAreaCoffee(request):
    area_edit = Production_Area_Average_Yield_Coffee_Type_Of_Grower.objects.get(category_id = request.data['coffee'])

    if 'category' in request.data:
        area_edit.category = request.data['category']

    if 'cooperatives' in request.data:
        area_edit.cooperatives = request.data['cooperatives']

    if 'estates' in request.data:
        area_edit.estates = request.data['estates']

    if 'unit' in request.data:
        area_edit.unit = request.data['unit']

    if 'year' in request.data:
        area_edit.year = request.data['year']


    area_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

########################################## Production Area and Average Yield of Tea ##########################################
# Launch Page
def areaTeaView(request):
    area = Production_Area_Average_Yield_Tea_Type_Grower.objects.all()

    productions = []

    if area:
        for production in area:

            c = {'id': production.category_id, 'category': production.category, 'smallholders': production.smallholders,
                'estates': production.estates, 'unit': production.unit,
                 'year': production.year}
            productions.append(c)
            context = {'productions': productions}
    return render(request, 'knbs_bi/agriculture_production_area_average_yield_tea_type_grower.html', context)

# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def areaTea(request):
    area = Production_Area_Average_Yield_Tea_Type_Grower.objects.all()

    productions = []

    if area:
        for production in area:

            c = {'category': production.category, 'smallholders': production.smallholders,
                'estates': production.estates, 'unit': production.unit,
                 'year': production.year}
            productions.append(c)
    else:
        pass

    return Response(productions)

# Add View
def addAreaTeaView(request):
    return render(request, 'knbs_bi/agriculture_production_area_average_yield_tea_type_grower_add.html')

# Edit View
def editAreaTeaView(request):
    return render(request, 'knbs_bi/agriculture_production_area_average_yield_tea_type_grower_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addAreaTea(request):
    area_add = Production_Area_Average_Yield_Tea_Type_Grower(category = request.data['category'], smallholders = request.data['smallholders'],
                                                                   estates = request.data['estates'], unit = request.data['unit'],
                                                                   year = request.data['year'],)
    if area_add:
        area_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editAreaTea(request):
    area_edit = Production_Area_Average_Yield_Tea_Type_Grower.objects.get(category_id = request.data['tea'])

    if 'category' in request.data:
        area_edit.category = request.data['category']

    if 'smallholders' in request.data:
        area_edit.smallholders = request.data['smallholders']

    if 'estates' in request.data:
        area_edit.estates = request.data['estates']

    if 'unit' in request.data:
        area_edit.unit = request.data['unit']

    if 'year' in request.data:
        area_edit.year = request.data['year']


    area_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

########################################## Production of Livestock and Dairy Products ##########################################
# Launch Page
def livestockProductsView(request):
    livestock = Production_Of_Livestock_And_Dairy_Products.objects.all()

    products = []

    if livestock:
        for product in livestock:

            c = {'id': product.product_id, 'category': product.category, 'by_product': product.by_product,
                'unit': product.unit, 'value': product.value,
                 'year': product.year}
            products.append(c)
            context = {'products': products}
    return render(request, 'knbs_bi/agriculture_production_of_livestock_and_dairy_products.html', context)

# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def livestockProducts(request):
    livestock = Production_Of_Livestock_And_Dairy_Products.objects.all()

    products = []

    if livestock:
        for product in livestock:

            c = {'category': product.category, 'by_product': product.by_product,
                'unit': product.unit, 'value': product.value,
                 'year': product.year}
            products.append(c)
    else:
        pass

    return Response(products)

# Add View
def addLivestockProductsView(request):
    return render(request, 'knbs_bi/agriculture_production_of_livestock_and_dairy_products_add.html')

# Edit View
def editLivestockProductsView(request):
    return render(request, 'knbs_bi/agriculture_production_of_livestock_and_dairy_products_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addLivestockProducts(request):
    livestock_add = Production_Of_Livestock_And_Dairy_Products(category = request.data['category'], by_product = request.data['by_product'],
                                                                   unit = request.data['unit'], value = request.data['value'],
                                                                   year = request.data['year'],)
    if livestock_add:
        livestock_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editLivestockProducts(request):
    product_edit = Production_Of_Livestock_And_Dairy_Products.objects.get(product_id = request.data['product'])

    if 'category' in request.data:
        product_edit.category = request.data['category']

    if 'by_product' in request.data:
        product_edit.by_product = request.data['by_product']

    if 'unit' in request.data:
        product_edit.unit = request.data['unit']

    if 'value' in request.data:
        product_edit.value = request.data['value']

    if 'year' in request.data:
        product_edit.year = request.data['year']


    product_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)
