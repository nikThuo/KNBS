from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from building_and_construction.models import Industry_Id, Amount, Quarterly_Civil_Engineering_Cost_Index, \
    Quarterly_Non_Residential_Build_Cost, Quarterly_Overal_Construction_Cost, Quarterly_Residential_Bulding_Cost
from health.models import Counties

def building_and_construction(request):
    return render(request, template_name="knbs_bi/building_and_construction.html")

#===============================Industry ID===============================
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def idIndustry(request):
    industry_id = Industry_Id.objects.all()

    industries = []

    if industry_id:
        for industry in industry_id:
            c = {'industry_name': industry.industry}
            industries.append(c)
    else:
        pass
    return Response(industries)

#===============================Amount===============================

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def amountBuilding(request):
    building = Amount.objects.all()

    prices = []

    if building:
        for price in building:
            county = Counties.objects.get(county_id=price.county_id)
            industry = Industry_Id.objects.get(industry_id=price.industry_id)

            c = {'county': county.county_name, 'industry': industry.industry, 'amount': price.amount,
                 'year': price.year}
            prices.append(c)
    else:
        pass
    return Response(prices)

#Launch Page
def viewAmountBuilding(request):
    building = Amount.objects.all()

    prices = []

    if building:
        for price in building:
            county = Counties.objects.get(county_id=price.county_id)
            industry = Industry_Id.objects.get(industry_id=price.industry_id)

            c = {'id': price.buildingandconstruction_id, 'county': county.county_name, 'industry': industry.industry, 'amount': price.amount,
                 'year': price.year}
            prices.append(c)
            context = {'prices': prices}
    return render(request, 'knbs_bi/building_and_construction_amount.html', context)



#Add County Revenue
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addAmountBuilding(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    industry = Industry_Id.objects.get(industry=request.data['industry'])

    if counties and industry:
        kaunti = counties.county_id

        amount_add = Amount(county_id = kaunti, industry_id=industry.industry_id, amount= request.data['amount'], year= request.data['year'])

        if amount_add:
            amount_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit County Revenue
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editAmountBuilding(request):

    amount_update = Amount.objects.get(buildingandconstruction_id= request.data['amount_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            amount_update.county_id = counties.county_id

    if 'industry' in request.data:
        industry = Industry_Id.objects.get(industry=request.data['industry'])
        if industry:
            amount_update.industry_id = industry.industry_id

    if 'amount' in request.data:
        amount_update.amount = request.data['amount']

    if 'year' in request.data:
        amount_update.year = request.data['year']

    amount_update.save()
    response = {'Updated Successfully'}
    return Response(response)

#County Revenue Add View
def addAmountBuildingView(request):
    all_counties = Counties.objects.all()
    industries = Industry_Id.objects.all()
    context = {'counties': all_counties, 'industries': industries}
    # translation.activate('en')
    return render(request, 'knbs_bi/building_and_construction_amount_add.html', context)

#County Revenue Edit View
def editAmountBuildingView(request):
    all_counties = Counties.objects.all()
    industries = Industry_Id.objects.all()
    context = {'counties': all_counties, 'industries': industries}
    return render(request, 'knbs_bi/building_and_construction_amount_edit.html', context)

########################################## Quarterly Civil Engineering Cost Index ##########################################
#Launch Page
def quarterlyCivilView(request):
    quarterly = Quarterly_Civil_Engineering_Cost_Index.objects.all()

    costs = []

    if quarterly:
        for cost in quarterly:
            c = {'id':cost.cost_index_id, 'category': cost.category, 'march': cost.march, 'june': cost.june,
                 'sept': cost.sept, 'december': cost.december, 'year': cost.year}
            costs.append(c)
            context = {'costs': costs}
    else:
        pass
    return render(request, 'knbs_bi/building_and_construction_quarterly_civil_engineering_cost_index.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def quarterlyCivil(request):
    quarterly = Quarterly_Civil_Engineering_Cost_Index.objects.all()

    costs = []

    if quarterly:
        for cost in quarterly:
            c = {'category': cost.category, 'march': cost.march, 'june': cost.june,
                 'sept': cost.sept, 'december': cost.december, 'year': cost.year}
            costs.append(c)
    else:
        pass
    return Response(costs)

# Add View
def addQuarterlyCivilView(request):
    return render(request, 'knbs_bi/building_and_construction_quarterly_civil_engineering_cost_index_add.html')

# Edit View
def editQuarterlyCivilView(request):
    return render(request, 'knbs_bi/building_and_construction_quarterly_civil_engineering_cost_index_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addQuarterlyCivil(request):
    cost_add = Quarterly_Civil_Engineering_Cost_Index(category = request.data['category'], march = request.data['march'],
                                                      june = request.data['june'], sept = request.data['sept'],
                                                      december = request.data['december'], year = request.data['year'])
    if cost_add:
        cost_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editQuarterlyCivil(request):
    cost_edit = Quarterly_Civil_Engineering_Cost_Index.objects.get(cost_index_id = request.data['cost'])

    if 'category' in request.data:
        cost_edit.category = request.data['category']

    if 'march' in request.data:
        cost_edit.march = request.data['march']

    if 'june' in request.data:
        cost_edit.june = request.data['june']

    if 'sept' in request.data:
        cost_edit.sept = request.data['sept']

    if 'december' in request.data:
        cost_edit.december = request.data['december']

    if 'year' in request.data:
        cost_edit.year = request.data['year']


    cost_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

########################################## Quarterly Non Residential Cost ##########################################
#Launch Page
def quarterlyNonResidentialView(request):
    quarterly = Quarterly_Non_Residential_Build_Cost.objects.all()

    costs = []

    if quarterly:
        for cost in quarterly:
            c = {'id':cost.cost_index_id, 'category': cost.category, 'march': cost.march, 'june': cost.june,
                 'sept': cost.sept, 'december': cost.december, 'year': cost.year}
            costs.append(c)
            context = {'costs': costs}
    else:
        pass
    return render(request, 'knbs_bi/building_and_construction_quarterly_non_residential_build_cost.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def quarterlyNonResidential(request):
    quarterly = Quarterly_Non_Residential_Build_Cost.objects.all()

    costs = []

    if quarterly:
        for cost in quarterly:
            c = {'category': cost.category, 'march': cost.march, 'june': cost.june,
                 'sept': cost.sept, 'december': cost.december, 'year': cost.year}
            costs.append(c)
    else:
        pass
    return Response(costs)

# Add View
def addQuarterlyNonResidentialView(request):
    return render(request, 'knbs_bi/building_and_construction_quarterly_non_residential_build_cost_add.html')

# Edit View
def editQuarterlyNonResidentialView(request):
    return render(request, 'knbs_bi/building_and_construction_quarterly_non_residential_build_cost_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addQuarterlyNonResidential(request):
    cost_add = Quarterly_Non_Residential_Build_Cost(category = request.data['category'], march = request.data['march'],
                                                      june = request.data['june'], sept = request.data['sept'],
                                                      december = request.data['december'], year = request.data['year'])
    if cost_add:
        cost_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editQuarterlyNonResidential(request):
    cost_edit = Quarterly_Non_Residential_Build_Cost.objects.get(cost_index_id = request.data['cost'])

    if 'category' in request.data:
        cost_edit.category = request.data['category']

    if 'march' in request.data:
        cost_edit.march = request.data['march']

    if 'june' in request.data:
        cost_edit.june = request.data['june']

    if 'sept' in request.data:
        cost_edit.sept = request.data['sept']

    if 'december' in request.data:
        cost_edit.december = request.data['december']

    if 'year' in request.data:
        cost_edit.year = request.data['year']


    cost_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

########################################## Quarterly Overall Construction Cost ##########################################
#Launch Page
def quarterlyOverallView(request):
    quarterly = Quarterly_Overal_Construction_Cost.objects.all()

    costs = []

    if quarterly:
        for cost in quarterly:
            c = {'id':cost.category_id, 'category': cost.category, 'march': cost.march, 'june': cost.june,
                 'sept': cost.sept, 'december': cost.december, 'year': cost.year}
            costs.append(c)
            context = {'costs': costs}
    else:
        pass
    return render(request, 'knbs_bi/building_and_construction_quarterly_overal_construction_cost.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def quarterlyOverall(request):
    quarterly = Quarterly_Non_Residential_Build_Cost.objects.all()

    costs = []

    if quarterly:
        for cost in quarterly:
            c = {'category': cost.category, 'march': cost.march, 'june': cost.june,
                 'sept': cost.sept, 'december': cost.december, 'year': cost.year}
            costs.append(c)
    else:
        pass
    return Response(costs)

# Add View
def addQuarterlyOverallView(request):
    return render(request, 'knbs_bi/building_and_construction_quarterly_overal_construction_cost_add.html')

# Edit View
def editQuarterlyOverallView(request):
    return render(request, 'knbs_bi/building_and_construction_quarterly_overal_construction_cost_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addQuarterlyOverall(request):
    cost_add = Quarterly_Overal_Construction_Cost(category = request.data['category'], march = request.data['march'],
                                                      june = request.data['june'], sept = request.data['sept'],
                                                      december = request.data['december'], year = request.data['year'])
    if cost_add:
        cost_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editQuarterlyOverall(request):
    cost_edit = Quarterly_Overal_Construction_Cost.objects.get(category_id = request.data['cat'])

    if 'category' in request.data:
        cost_edit.category = request.data['category']

    if 'march' in request.data:
        cost_edit.march = request.data['march']

    if 'june' in request.data:
        cost_edit.june = request.data['june']

    if 'sept' in request.data:
        cost_edit.sept = request.data['sept']

    if 'december' in request.data:
        cost_edit.december = request.data['december']

    if 'year' in request.data:
        cost_edit.year = request.data['year']


    cost_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

########################################## Quarterly Residential Building Cost ##########################################
#Launch Page
def quarterlyResidentialView(request):
    quarterly = Quarterly_Residential_Bulding_Cost.objects.all()

    costs = []

    if quarterly:
        for cost in quarterly:
            c = {'id':cost.building_construction_id, 'category': cost.category, 'march': cost.march, 'june': cost.june,
                 'sept': cost.september, 'december': cost.december, 'year': cost.year}
            costs.append(c)
            context = {'costs': costs}
    else:
        pass
    return render(request, 'knbs_bi/building_and_construction_quarterly_residential_bulding_cost.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def quarterlyResidential(request):
    quarterly = Quarterly_Residential_Bulding_Cost.objects.all()

    costs = []

    if quarterly:
        for cost in quarterly:
            c = {'category': cost.category, 'march': cost.march, 'june': cost.june,
                 'sept': cost.september, 'december': cost.december, 'year': cost.year}
            costs.append(c)
    else:
        pass
    return Response(costs)

# Add View
def addQuarterlyResidentialView(request):
    return render(request, 'knbs_bi/building_and_construction_quarterly_residential_bulding_cost_add.html')

# Edit View
def editQuarterlyResidentialView(request):
    return render(request, 'knbs_bi/building_and_construction_quarterly_residential_bulding_cost_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addQuarterlyResidential(request):
    cost_add = Quarterly_Residential_Bulding_Cost(category = request.data['category'], march = request.data['march'],
                                                      june = request.data['june'], september = request.data['sept'],
                                                      december = request.data['december'], year = request.data['year'])
    if cost_add:
        cost_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editQuarterlyResidential(request):
    cost_edit = Quarterly_Residential_Bulding_Cost.objects.get(building_construction_id = request.data['building'])

    if 'category' in request.data:
        cost_edit.category = request.data['category']

    if 'march' in request.data:
        cost_edit.march = request.data['march']

    if 'june' in request.data:
        cost_edit.june = request.data['june']

    if 'sept' in request.data:
        cost_edit.september = request.data['sept']

    if 'december' in request.data:
        cost_edit.december = request.data['december']

    if 'year' in request.data:
        cost_edit.year = request.data['year']


    cost_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)