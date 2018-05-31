from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

#from knbs_api.models import Sectors, Counties
from health.models import Counties #, Sectors
from labour.models import Employment_Public_Sector, Sectors


def labour(request):
    return render(request, template_name='knbs_bi/labour.html')

def no_records(request):
    datasets = Sectors.objects.order_by('Labour').count()
    context = {'labour_count': datasets}
    return render(request, 'knbs_bi/index.html', context)

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def allSectors(request):
    all_sectors = Sectors.objects.all()

    sectors = []

    if all_sectors:
        for sector in all_sectors:
            c = {'sector_name': sector.sector_name}
            sectors.append(c)
    else:
        pass
    return Response(sectors)

#===============================Employment Public Sector===============================
#Launch Page
def allPublicSectorView(request):
    public_sector = Employment_Public_Sector.objects.all()

    p_sectors = []

    if public_sector:
        for sector in public_sector:
            county = Counties.objects.get(county_id=sector.county_id)
            s_id = Sectors.objects.get(sector_id=sector.sector_id)

            c = {'id':sector.wage_employment_id, 'county': county.county_name, 'year': sector.year,
                 'sector': s_id.sector_name, 'wage_employment': sector.wage_employment}

            p_sectors.append(c)
            context = {'sectors': p_sectors}
    return render(request, 'knbs_bi/labour_employment_public_sector.html', context)

#Public Sector Add View
def addPublicSectorView(request):
    all_counties = Counties.objects.all()
    all_sectors = Sectors.objects.all()
    context = {'counties': all_counties, 'sectors': all_sectors}
    # translation.activate('en')
    return render(request, 'knbs_bi/labour_employment_public_sector_add.html', context)

#Public Sector Edit View
def editPublicSectorView(request):
    all_counties = Counties.objects.all()
    all_sectors = Sectors.objects.all()
    context = {'counties': all_counties, 'sectors': all_sectors}
    return render(request, 'knbs_bi/labour_employment_public_sector_edit.html', context)

# All Public Sector
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def publicSector(request):
    public_sector = Employment_Public_Sector.objects.all()

    p_sectors = []

    if public_sector:
        for sector in public_sector:
            county = Counties.objects.get(county_id=sector.county_id)
            s_id = Sectors.objects.get(sector_id=sector.sector_id)

            c = {'county': county.county_name, 'year': sector.year,
                 'sector': s_id.sector_name, 'wage_employment': sector.wage_employment_id}

            p_sectors.append(c)
    else:
        pass
    return Response(p_sectors)

# Add Public Sector
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addPublicSector(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    sectors = Sectors.objects.get(sector_name=request.data['sector'])

    if counties and sectors:
        kaunti = counties.county_id
        sekta = sectors.sector_id

        public_add = Employment_Public_Sector(county_id=kaunti, year=request.data['year'], sector_id=sekta,
                                              wage_employment=request.data['wage'])

        if public_add:
            public_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Public Sector
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editPublicSector(request):
    public_edit = Employment_Public_Sector.objects.get(wage_employment_id=request.data['wage_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        #print("Got it")
        if counties:
            public_edit.county_id = counties.county_id

    if 'year' in request.data:
        public_edit.year = request.data['year']
    if 'sector' in request.data:
        s_id = Sectors.objects.get(sector_name=request.data['sector'])

        if s_id:
            public_edit.sector_id = s_id.sector_id
    if 'wage' in request.data:
        public_edit.wage_employment = request.data['wage']

    public_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

#===============================Average_Wage_Earnings_Per_Employee_Private_Sector===============================
#Launch Page
def avgEarningsPrivateView(request):
    a = Average_Wage_Earnings_Per_Employee_Private_Sector.objects.all()

    indicators = []

    if monetary:
        for indicator in monetary:
            c = {'id':indicator.domestic_credit_id, 'year': indicator.year,
                 'private_and_other_public_bodies': indicator.private_and_other_public_bodies,
                 'national_government': indicator.national_government, 'total': indicator.total}
            indicators.append(c)
            context = {'indicators': indicators}
    else:
        pass
    return render(request, 'knbs_bi/money_and_banking_monetary_indicators_domestic_credit.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def monetaryIndicatorsDomestic(request):
    monetary = Monetary_Indicators_Domestic_Credit.objects.all()

    indicators = []

    if monetary:
        for indicator in monetary:
            c = {'year': indicator.year,
                 'private_and_other_public_bodies': indicator.private_and_other_public_bodies,
                 'national_government': indicator.national_government, 'total': indicator.total}
            indicators.append(c)
    else:
        pass
    return Response(indicators)

# Add View
def addMonetaryIndicatorsDomesticView(request):
    return render(request, 'knbs_bi/money_and_banking_monetary_indicators_domestic_credit_add.html')

# Edit View
def editMonetaryIndicatorsDomesticView(request):
    return render(request, 'knbs_bi/money_and_banking_monetary_indicators_domestic_credit_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addMonetaryIndicatorsDomestic(request):

    monetary_add = Monetary_Indicators_Domestic_Credit(year = request.data['year'],
                                                       private_and_other_public_bodies = request.data['private'],
                                                       national_government = request.data['national'],
                                                       total = request.data['total'])

    if monetary_add:
        monetary_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editMonetaryIndicatorsDomestic(request):
    monetary_edit = Monetary_Indicators_Domestic_Credit.objects.get(domestic_credit_id = request.data['domestic'])

    if 'year' in request.data:
        monetary_edit.year = request.data['year']

    if 'private' in request.data:
        monetary_edit.private_and_other_public_bodies = request.data['private']

    if 'national' in request.data:
        monetary_edit.national_government = request.data['national']

    if 'total' in request.data:
        monetary_edit.total = request.data['total']

    monetary_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)