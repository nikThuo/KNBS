from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


from health.models import Months, Counties, SubCounty
from money_and_banking.models import Commercial_Banks_Bills_Loans_Advances, Inflation_Rates, Interest_Rates, \
    Monetary_Indicators_Broad_Money_Supply, Monetary_Indicators_Domestic_Credit, Nairobi_Securities_Exchange, \
    Institutions, Index


# Create your views here.

def money_and_banking(request):
    return render(request, template_name="knbs_bi/money_and_banking.html")

########################################## Commercial Banks, Bills and Loans Advances ##########################################
#Launch Page
def commercialBanksView(request):
    banks = Commercial_Banks_Bills_Loans_Advances.objects.all()

    loans = []

    if banks:
        for loan in banks:
            month = Months.objects.get(month_id = loan.month_id)

            c = {'id':loan.bills_loans_advances_id, 'sector': loan.sector, 'sub': loan.sub_sector, 'amount': loan.amount,
                 'month': month.month, 'year': loan.year}
            loans.append(c)
            context = {'loans': loans}
    else:
        pass
    return render(request, 'knbs_bi/money_and_banking_commercial_banks_bills_loans_advances.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def commercialBanks(request):
    banks = Commercial_Banks_Bills_Loans_Advances.objects.all()

    loans = []

    if banks:
        for loan in banks:
            month = Months.objects.get(month_id=loan.month_id)

            c = {'sector': loan.sector, 'sub': loan.sub_sector,
                 'amount': loan.amount,
                 'month': month.month, 'year': loan.year}
            loans.append(c)
    else:
        pass
    return Response(loans)

# Add View
def addCommercialBanksView(request):
    all_months = Months.objects.all()
    context = {'months': all_months}
    return render(request, 'knbs_bi/money_and_banking_commercial_banks_bills_loans_advances_add.html', context)

# Edit View
def editCommercialBanksView(request):
    all_months = Months.objects.all()
    context = {'months': all_months}
    return render(request, 'knbs_bi/money_and_banking_commercial_banks_bills_loans_advances_edit.html', context)

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addCommercialBanks(request):
    month = Months.objects.get(month = request.data['month'])

    if month:

        loan_add = Commercial_Banks_Bills_Loans_Advances(sector = request.data['sector'], sub_sector = request.data['sub'],
                                                          amount = request.data['amount'], month_id = month.month_id,
                                                          year = request.data['year'])
        if loan_add:
            loan_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editCommercialBanks(request):
    loan_edit = Commercial_Banks_Bills_Loans_Advances.objects.get(bills_loans_advances_id = request.data['loans'])

    if 'sector' in request.data:
        loan_edit.sector = request.data['sector']

    if 'sub' in request.data:
        loan_edit.sub_sector = request.data['sub']

    if 'amount' in request.data:
        loan_edit.amount = request.data['amount']

    if 'month' in request.data:
        month = Months.objects.get(month=request.data['month'])
        if month:
            loan_edit.month_id = month.month_id

    if 'year' in request.data:
        loan_edit.year = request.data['year']


    loan_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

########################################## Inflation Rates ##########################################
#Launch Page
def inflationRatesView(request):
    inflation = Inflation_Rates.objects.all()

    rates = []

    if inflation:
        for rate in inflation:
            c = {'id':rate.inflation_rate_id, 'inflation_rate': rate.inflation_rate, 'year': rate.year}
            rates.append(c)
            context = {'rates': rates}
    else:
        pass
    return render(request, 'knbs_bi/money_and_banking_inflation_rates.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def inflationRates(request):
    inflation = Inflation_Rates.objects.all()

    rates = []

    if inflation:
        for rate in inflation:
            c = {'inflation_rate': rate.inflation_rate, 'year': rate.year}
            rates.append(c)
    else:
        pass
    return Response(rates)

# Add View
def addInflationRatesView(request):
    return render(request, 'knbs_bi/money_and_banking_inflation_rates_add.html')

# Edit View
def editInflationRatesView(request):
    return render(request, 'knbs_bi/money_and_banking_inflation_rates_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addInflationRates(request):

    rate_add = Inflation_Rates(inflation_rate = request.data['rate'], year = request.data['year'])

    if rate_add:
        rate_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editInflationRates(request):
    rate_edit = Inflation_Rates.objects.get(inflation_rate_id = request.data['inflation'])

    if 'rate' in request.data:
        rate_edit.inflation_rate = request.data['rate']

    if 'year' in request.data:
        rate_edit.year = request.data['year']

    rate_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

########################################## Interest Rates ##########################################
#Launch Page
def interestRatesView(request):
    inflation = Interest_Rates.objects.all()

    rates = []

    if inflation:
        for rate in inflation:
            month = Months.objects.get(month_id=rate.month_id)

            c = {'id':rate.interest_rates_id, 'bank_loans_and_advances_weighted_average_rates': rate.bank_loans_and_advances_weighted_average_rates,
                 'average_deposit_rate':rate.average_deposit_rate, 'month':month.month,
                 'year': rate.year}
            rates.append(c)
            context = {'rates': rates}
    else:
        pass
    return render(request, 'knbs_bi/money_and_banking_interest_rates.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def interestRates(request):
    inflation = Interest_Rates.objects.all()

    rates = []

    if inflation:
        for rate in inflation:
            month = Months.objects.get(month_id=rate.month_id)

            c = {'bank_loans_and_advances_weighted_average_rates': rate.bank_loans_and_advances_weighted_average_rates,
                 'average_deposit_rate': rate.average_deposit_rate, 'month': month.month,
                 'year': rate.year}
            rates.append(c)
    else:
        pass
    return Response(rates)

# Add View
def addInterestRatesView(request):
    all_months = Months.objects.all()
    context = {'months': all_months}
    return render(request, 'knbs_bi/money_and_banking_interest_rates_add.html', context)

# Edit View
def editInterestRatesView(request):
    all_months = Months.objects.all()
    context = {'months': all_months}
    return render(request, 'knbs_bi/money_and_banking_interest_rates_edit.html', context)

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addInterestRates(request):
    month = Months.objects.get(month=request.data['month'])

    if month:

        rate_add = Interest_Rates(bank_loans_and_advances_weighted_average_rates = request.data['bank'],
                                  average_deposit_rate = request.data['rate'], month_id = month.month_id,
                                  year = request.data['year'])

        if rate_add:
            rate_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editInterestRates(request):
    rate_edit = Interest_Rates.objects.get(interest_rates_id = request.data['interest'])

    if 'bank' in request.data:
        rate_edit.bank_loans_and_advances_weighted_average_rates = request.data['bank']

    if 'rate' in request.data:
        rate_edit.average_deposit_rate = request.data['rate']

    if 'month' in request.data:
        month = Months.objects.get(month=request.data['month'])
        if month:
            rate_edit.month_id = month.month_id

    if 'year' in request.data:
        rate_edit.year = request.data['year']

    rate_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

########################################## Monetary Indicators Broad Money Supply ##########################################
#Launch Page
def monetaryIndicatorsView(request):
    monetary = Monetary_Indicators_Broad_Money_Supply.objects.all()

    indicators = []

    if monetary:
        for indicator in monetary:
            c = {'id':indicator.broad_money_supply_id, 'year': indicator.year, 'broad_money_supply': indicator.broad_money_supply}
            indicators.append(c)
            context = {'indicators': indicators}
    else:
        pass
    return render(request, 'knbs_bi/money_and_banking_monetary_indicators_broad_money_supply.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def monetaryIndicators(request):
    monetary = Monetary_Indicators_Broad_Money_Supply.objects.all()

    indicators = []

    if monetary:
        for indicator in monetary:
            c = {'year': indicator.year, 'broad_money_supply': indicator.broad_money_supply}
            indicators.append(c)
    else:
        pass
    return Response(indicators)

# Add View
def addMonetaryIndicatorsView(request):
    return render(request, 'knbs_bi/money_and_banking_monetary_indicators_broad_money_supply_add.html')

# Edit View
def editMonetaryIndicatorsView(request):
    return render(request, 'knbs_bi/money_and_banking_monetary_indicators_broad_money_supply_edit.html')

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addMonetaryIndicators(request):

    monetary_add = Monetary_Indicators_Broad_Money_Supply(year = request.data['year'], broad_money_supply = request.data['broad'])

    if monetary_add:
        monetary_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editMonetaryIndicators(request):
    monetary_edit = Monetary_Indicators_Broad_Money_Supply.objects.get(broad_money_supply_id = request.data['money'])

    if 'year' in request.data:
        monetary_edit.year = request.data['year']

    if 'broad' in request.data:
        monetary_edit.broad_money_supply = request.data['broad']

    monetary_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

########################################## Monetary Indicators Domestic Credit ##########################################
#Launch Page
def monetaryIndicatorsDomesticView(request):
    monetary = Monetary_Indicators_Domestic_Credit.objects.all()

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

########################################## Nairobi Securities Exchange ##########################################
#Launch Page
def securitiesExchangeView(request):
    exchange = Nairobi_Securities_Exchange.objects.all()

    securities = []

    if exchange:
        for security in exchange:
            month = Months.objects.get(month_id = security.month_id)

            c = {'id':security.nse_id, 'month': month.month, 'nse_20_share_index': security.nse_20_share_index,
                  'year': security.year}
            securities.append(c)
            context = {'securities': securities}
    else:
        pass
    return render(request, 'knbs_bi/money_and_banking_nairobi_securities_exchange.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def securitiesExchange(request):
    exchange = Nairobi_Securities_Exchange.objects.all()

    securities = []

    if exchange:
        for security in exchange:
            month = Months.objects.get(month_id = security.month_id)

            c = {'month': month.month, 'nse_20_share_index': security.nse_20_share_index,
                  'year': security.year}
            securities.append(c)
    else:
        pass
    return Response(securities)

# Add View
def addSecuritiesExchangeView(request):
    all_months = Months.objects.all()
    context = {'months': all_months}
    return render(request, 'knbs_bi/money_and_banking_nairobi_securities_exchange_add.html', context)

# Edit View
def editSecuritiesExchangeView(request):
    all_months = Months.objects.all()
    context = {'months': all_months}
    return render(request, 'knbs_bi/money_and_banking_nairobi_securities_exchange_edit.html', context)

# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addSecuritiesExchange(request):
    month = Months.objects.get(month = request.data['month'])

    if month:

        sec_add = Nairobi_Securities_Exchange(month_id = month.month_id, nse_20_share_index = request.data['nse'],
                                              year = request.data['year'])
        if sec_add:
            sec_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editSecuritiesExchange(request):
    sec_edit = Nairobi_Securities_Exchange.objects.get(nse_id = request.data['share'])

    if 'month' in request.data:
        month = Months.objects.get(month=request.data['month'])
        if month:
            sec_edit.month_id = month.month_id

    if 'nse' in request.data:
        sec_edit.nse_20_share_index = request.data['nse']

    if 'year' in request.data:
        sec_edit.year = request.data['year']

    sec_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

#===============================MONEY BANKING INSTITUTIONS===============================
#All Money Banking Institutions
#Launch Page
def viewBankingInstitution(request):
    all_banks = Institutions.objects.all()

    revenues = []

    if all_banks:
        for revenue in all_banks:
            counties = Counties.objects.get(county_id=revenue.county_id)
            institution = Index.objects.get(institution_id=revenue.institution_id)
            subcounty = SubCounty.objects.filter(subcounty_id=revenue.subcounty_id)
            if subcounty:
                for sc in subcounty:
                    c = {'id': revenue.moneybanking_id, 'county': counties.county_name, 'subcounty': sc.subcounty_name, 'institution': institution.financial_institution,
                         'number': revenue.number}
                    revenues.append(c)
                    context = {'institutions': revenues}
    else:
        pass
    return render(request, 'knbs_bi/money_and_banking_institutions.html', context)

#Money Banking Institutions Add View
def addBankingInstitutionView(request):
    all_counties = Counties.objects.all()
    sub_county = SubCounty.objects.all()
    institution = Index.objects.all()
    context = {'counties': all_counties, 'sub': sub_county, 'inst': institution}
    # translation.activate('en')
    return render(request, 'knbs_bi/money_and_banking_institutions_add.html', context)

#Money Banking Institutions Edit View
def editBankingInstitutionView(request):
    all_counties = Counties.objects.all()
    sub_county = SubCounty.objects.all()
    institution = Index.objects.all()
    context = {'counties': all_counties, 'sub': sub_county, 'inst': institution}
    return render(request, 'knbs_bi/money_and_banking_institutions_edit.html', context)

#All County Budget Allocation
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def bankingInstitution(request):
    all_banks = Institutions.objects.all()

    revenues = []

    if all_banks:
        for revenue in all_banks:
            counties = Counties.objects.get(county_id=revenue.county_id)
            institution = Index.objects.get(institution_id=revenue.institution_id)
            subcounty = SubCounty.objects.filter(subcounty_id=revenue.subcounty_id)
            if subcounty:
                for sc in subcounty:
                    c = {'county': counties.county_name, 'subcounty': sc.subcounty_name, 'institution': institution.financial_institution,
                         'number': revenue.number}
                    revenues.append(c)
    else:
        pass

    return Response(revenues)

#Add County Budget Allocation
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addBankingInstitution(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])
    institution = Index.objects.get(financial_institution=request.data['institution'])

    if counties and sub and institution:
        kaunti = counties.county_id
        sub_kaunti = sub.subcounty_id
        instituti = institution.institution_id

        institution_add = Institutions(county_id = kaunti, subcounty_id = sub_kaunti, institution_id = instituti,
                                                number = request.data['number'])

        if institution_add:
            institution_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit County Budget Allocation
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editBankingInstitution(request):
    institution_edit = Institutions.objects.get(moneybanking_id = request.data['money_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            institution_edit.county_id = counties.county_id

    if 'sub_county' in request.data:
        sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])
        if sub:
            institution_edit.subcounty_id = sub.subcounty_id

    if 'institution' in request.data:
        institution = Index.objects.get(financial_institution=request.data['institution'])
        if institution:
            institution_edit.institution_id = institution.institution_id
    if 'number' in request.data:
        institution_edit.number = request.data['number']

    institution_edit.save()

    return Response(status=status.HTTP_201_CREATED)
