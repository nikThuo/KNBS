from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from health.models import Counties
from trade_and_commerce.models import Revenue_Collection_By_Title, Revenue_Collection_By_Id, \
    Revenue_Collection_By_Amount

def trade_and_commerce(request):
    return render(request, template_name='knbs_bi/trade_and_commerce.html')

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def tradeTitle(request):
    trade_title = Revenue_Collection_By_Title.objects.all()

    titles = []

    if trade_title:
        for title in trade_title:
            c = {'trade_and_commerce_title': title.tradeandcommerce_title}
            titles.append(c)
    else:
        pass

    return Response(titles)

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def tradeID(request):
    trade_id = Revenue_Collection_By_Id.objects.all()

    ids = []

    if trade_id:
        for id in trade_id:
            c = {'revenue_collection_title': id.revenuecollection_title}
            ids.append(c)
    else:
        pass

    return Response(ids)

#===============================Trade and Commerce Amount===============================
#Launch Page
def tradeAmountView(request):
    trade_amount = Revenue_Collection_By_Amount.objects.all()

    prices = []
    context={}

    if trade_amount:
        for price in trade_amount:
            county = Counties.objects.get(county_id=price.county_id)
            revenue = Revenue_Collection_By_Id.objects.get(revenuecollection_id=price.revenuecollection_id)
            c = {'county': county.county_name, 'revenue_collection_industry': revenue.revenuecollection_title,
                 'amount': price.amount, 'year': price.year}
            prices.append(c)
            context = {'prices': prices}

    return render(request, 'knbs_bi/trade_and_commerce_revenue_collection_by_amount.html', context)


#Trade and Commerce Add View
def addTradeAmountView(request):
    all_counties = Counties.objects.all()
    revenue = Revenue_Collection_By_Id.objects.all()
    context = {'counties': all_counties, 'revenues': revenue}
    # translation.activate('en')
    return render(request, 'knbs_bi/trade_and_commerce_revenue_collection_by_amount_add.html', context)

#Trade and Commerce Edit View
def editTradeAmountView(request):
    all_counties = Counties.objects.all()
    revenue = Revenue_Collection_By_Id.objects.all()
    context = {'counties': all_counties, 'revenues': revenue}
    return render(request, 'knbs_bi/trade_and_commerce_revenue_collection_by_amount_edit.html', context)

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def tradeAmount(request):
    trade_amount = Revenue_Collection_By_Amount.objects.all()

    prices = []

    if trade_amount:
        for price in trade_amount:
            county = Counties.objects.get(county_id=price.county_id)
            revenue = Revenue_Collection_By_Id.objects.get(revenuecollection_id=price.revenuecollection_id)
            c = {'county': county.county_name, 'revenue_collection_industry': revenue.revenuecollection_title,
                 'amount': price.amount, 'year': price.year}
            prices.append(c)
    else:
        pass

    return Response(prices)

# Add Trade and Commerce
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addTradeAmount(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    revenue = Revenue_Collection_By_Id.objects.get(revenuecollection_title=request.data['revenue'])

    if counties and revenue:
        kaunti = counties.county_id
        rev_id = revenue.revenuecollection_id

        trade_add = Revenue_Collection_By_Amount(county_id=kaunti, revenuecollection_id=rev_id, amount=request.data['amount'],
                                              year=request.data['year'])

        if trade_add:
            trade_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Trade and Commerce
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editTradeAmount(request):
    trade_edit = Revenue_Collection_By_Amount.objects.get(tradeandcommerce_id=request.data['trade_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            trade_edit.county_id = counties.county_id

    if 'revenue' in request.data:
        revenue = Revenue_Collection_By_Id.objects.get(revenuecollection_title=request.data['revenue'])
        if revenue:
            trade_edit.revenuecollection_id = revenue.revenuecollection_id

    if 'amount' in request.data:
        trade_edit.amount = request.data['amount']
    if 'year' in request.data:
        trade_edit.year = request.data['year']

    trade_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)
