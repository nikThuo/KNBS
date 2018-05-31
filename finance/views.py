from django.shortcuts import render

# Create your views here.
from rest_framework import status

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from finance.models import County_Revenue, County_Expenditure, Economic_Classification_Revenue, \
    Outstanding_Debt_International_Organization, Outstanding_Debt_Lending_Country, Excise_Revenue_Commodity, \
    County_Budget_Allocation, National_Government_Expenditure, National_Government_Expenditure_Purpose, Cdf_Allocation, \
    Cdf_Allocation_By_Constituency

from health.models import Counties, SubCounty

# CountyRevenue, CountyExpenditure, EconomicClassificationRevenue, \
    # OutstandingDebtInternationalOrganization, OutstandingDebtLendingCountry, ExciseRevenueCommodity, \
    # CountyBudgetAllocation, NationalGovernmentExpenditure, NationalGovernmentExpenditurePurpose

def finance(request):
    return render(request, template_name="knbs_bi/finance.html")

#===============================PUBLIC FINANCE===============================

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def cdfAllocation(request):
    cdf_allocation = Cdf_Allocation.objects.all()

    allocations = []

    if cdf_allocation:
        for allocation in cdf_allocation:
            counties = Counties.objects.get(county_id=allocation.county_id)
            subcounty = SubCounty.objects.get(subcounty_id=allocation.subcounty_id)
            c = {'county': counties.county_name, 'sub_county': subcounty.subcounty_name,
                 'cdf_allocation': allocation.cdfallocation, 'year': allocation.year}
            allocations.append(c)
    else:
        pass

    return Response(allocations)

# @api_view(http_method_names=['GET'])
# @renderer_classes((JSONRenderer,))
# def bankingIndex(request):
#     banking_index = Money_Banking_Index.objects.all()
#
#     indexes = []
#
#     if banking_index:
#         for index in banking_index:
#             c = {'financial Institution': index.financial_institution}
#             indexes.append(c)
#     else:
#         pass
#     return Response(indexes)
#
# @api_view(http_method_names=['GET'])
# @renderer_classes((JSONRenderer,))
# def bankingInstitution(request):
#     banking_inst = Money_Banking_Institutions.objects.all()
#
#     institutions = []
#
#     if banking_inst:
#         for institution in banking_inst:
#             counties = Counties.objects.get(county_id=institution.county_id)
#             subcounty = SubCounty.objects.get(subcounty_id=institution.subcounty_id)
#             inst = Money_Banking_Index.objects.get(institution_id=institution.institution_id)
#             c = {'county': counties.county_name, 'sub_county': subcounty.subcounty_name,
#                  'financial institution': inst.financial_institution, 'number': institution.number}
#             institutions.append(c)
#     else:
#         pass
#     return Response(institutions)

#===============================COUNTY REVENUE===============================
#All County Revenue

#Launch Page
def viewCountyRevenue(request):
    all_revenue = County_Revenue.objects.all()

    revenues = []

    if all_revenue:
        for revenue in all_revenue:
            counties = Counties.objects.get(county_id=revenue.county_id)
            c = {'revenue_id': revenue.county_revenue_id, 'rev_estimates': revenue.revenue_estimates, 'grants': revenue.conditional_grant,
                 'county': counties.county_name, 'share': revenue.equitable_share, 'total': revenue.total_revenue,
                 'year': revenue.year}
            revenues.append(c)
            context = {'revenues': revenues}
    return render(request, 'knbs_bi/finance_county_revenue_history.html', context)


@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def allCountyRevenue(request):
    all_revenue = County_Revenue.objects.all()

    revenues = []

    if all_revenue:
        for revenue in all_revenue:
            counties = Counties.objects.get(county_id=revenue.county_id)
            c = {'estimates': revenue.revenue_estimates, 'grants':revenue.conditional_grant, 'county':counties.county_name, 'share':revenue.equitable_share,
                 'total_revenue':revenue.total_revenue, 'year':revenue.year}
            revenues.append(c)
    else:
        pass

    return Response(revenues)

#Add County Revenue
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addCountyRevenue(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id

        revenue_add = County_Revenue(revenue_estimates = request.data['estimates'], conditional_grant = request.data['grants'], county_id = kaunti,
                                    equitable_share = request.data['share'], total_revenue = request.data['revenue'], year = request.data['year'])

        if revenue_add:
            revenue_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit County Revenue
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editCountyRevenue(request):

    revenue_update = County_Revenue.objects.get(county_revenue_id = request.data['resource_id'])

    if 'estimates' in request.data:
        revenue_update.revenue_estimates = request.data['estimates']
    if 'grants' in request.data:
        revenue_update.conditional_grant = request.data['grants']
    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            revenue_update.county_id = counties.county_id
    if 'share' in request.data:
        revenue_update.equitable_share = request.data['share']
    if 'revenue' in request.data:
        revenue_update.total_revenue = request.data['revenue']
    if 'year' in request.data:
        revenue_update.year = request.data['year']

    revenue_update.save()
    response = {'estimates': revenue_update.revenue_estimates, 'grants': revenue_update.conditional_grant, 'county': revenue_update.county_id,
                'share': revenue_update.equitable_share, 'revenue': revenue_update.total_revenue, 'year': revenue_update.year}
    return Response(response)

#County Revenue Add View
def addCountyRevenueView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    # translation.activate('en')
    return render(request, 'knbs_bi/finance_county_revenue_add.html', context)

#County Revenue Edit View
def editCountyRevenueView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/finance_county_revenue_edit.html', context)

#===============================COUNTY EXPENDITURE===============================
#Launch County Expenditure
def allCountyExpenditureView(request):
    all_expenditure = County_Expenditure.objects.all()

    expenditures = []

    if all_expenditure:
        for espenditure in all_expenditure:
            counties = Counties.objects.get(county_id=espenditure.county_id)
            c = {'id': espenditure.countyexpenditure_id, 'county': counties.county_name, 'employees':espenditure.compensation_employees, 'services':espenditure.goods_services, 'subsidies':espenditure.subsidies,
                 'international':espenditure.grants_internationalorganisation, 'government':espenditure.grants_governmentunits,
                 'other_grants': espenditure.othergrants, 'capital_grants':espenditure.capitalgrants,
                 'benefits': espenditure.socialbenefits, 'expense':espenditure.otherexpense,
                 'structures': espenditure.buildingstructures, 'equipment':espenditure.plantmachinery_equipment,
                 'inventory': espenditure.inventories, 'assets':espenditure.otherassets,
                 'financial_assets': espenditure.acquisition_financialassets, 'debt':espenditure.interest_debt,
                 'total': espenditure.total_expenditure, 'year':espenditure.year}
            expenditures.append(c)
            context = {'expenditures': expenditures}
    else:
        pass

    return render(request, 'knbs_bi/finance_county_expenditure.html', context)

# View All County Expenditure
def viewExpenditure(request):
    return render(request, template_name='knbs_bi/finance_county_expenditure_view.html')

#All County Expenditure
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def allCountyExpenditure(request):
    all_expenditure = County_Expenditure.objects.all()

    espenditures = []

    if all_expenditure:
        for espenditure in all_expenditure:
            counties = Counties.objects.get(county_id=espenditure.county_id)
            c = {'county_id': counties.county_name, 'employees':espenditure.compensation_employees, 'services':espenditure.goods_services, 'subsidies':espenditure.subsidies,
                 'international':espenditure.grants_internationalorganisation, 'government':espenditure.grants_governmentunits,
                 'other_grants': espenditure.othergrants, 'capital_grants':espenditure.capitalgrants,
                 'benefits': espenditure.socialbenefits, 'expense':espenditure.otherexpense,
                 'structures': espenditure.buildingstructures, 'equipment':espenditure.plantmachinery_equipment,
                 'inventory': espenditure.inventories, 'assets':espenditure.otherassets,
                 'financial_assets': espenditure.acquisition_financialassets, 'debt':espenditure.interest_debt,
                 'total': espenditure.total_expenditure, 'year':espenditure.year,}
            espenditures.append(c)
    else:
        pass

    return Response(espenditures)

#Add County Expenditure
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addCountyExpenditure(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        expenditure_add = County_Expenditure(county_id = counties.county_id, compensation_employees = request.data['employees'], goods_services = request.data['services'],
                                            subsidies = request.data['subsidies'], grants_internationalorganisation = request.data['international'],
                                            grants_governmentunits = request.data['government'], othergrants = request.data['other_grants'],
                                            capitalgrants=request.data['capital_grants'], socialbenefits = request.data['benefits'],
                                            otherexpense=request.data['expense'], buildingstructures = request.data['structures'],
                                            plantmachinery_equipment=request.data['equipment'], inventories = request.data['inventory'],
                                            otherassets=request.data['assets'], acquisition_financialassets = request.data['financial_assets'],
                                            interest_debt=request.data['debt'], total_expenditure = request.data['total'],
                                            year=request.data['year'],)

        if expenditure_add:
            expenditure_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit County Expenditure
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editCountyExpenditure(request):

    expenditure_update = County_Expenditure.objects.get(countyexpenditure_id = request.data['expenditure'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            expenditure_update.county_id = counties.county_id
    if 'employees' in request.data:
        expenditure_update.compensation_employees = request.data['employees']
    if 'services' in request.data:
        expenditure_update.goods_services = request.data['services']
    if 'subsidies' in request.data:
        expenditure_update.subsidies = request.data['subsidies']
    if 'international' in request.data:
        expenditure_update.grants_internationalorganisation = request.data['international']
    if 'government' in request.data:
        expenditure_update.grants_governmentunits = request.data['government']
    if 'other_grants' in request.data:
        expenditure_update.othergrants = request.data['other_grants']
    if 'capital_grants' in request.data:
        expenditure_update.capitalgrants = request.data['capital_grants']
    if 'benefits' in request.data:
        expenditure_update.socialbenefits = request.data['benefits']
    if 'expense' in request.data:
        expenditure_update.otherexpense = request.data['expense']
    if 'structures' in request.data:
        expenditure_update.buildingstructures = request.data['structures']
    if 'equipment' in request.data:
        expenditure_update.plantmachinery_equipment = request.data['equipment']
    if 'inventory' in request.data:
        expenditure_update.inventories = request.data['inventory']
    if 'assets' in request.data:
        expenditure_update.otherassets = request.data['assets']
    if 'financial_assets' in request.data:
        expenditure_update.acquisition_financialassets = request.data['financial_assets']
    if 'debt' in request.data:
        expenditure_update.interest_debt = request.data['debt']
    if 'total' in request.data:
        expenditure_update.total_expenditure = request.data['total']
    if 'year' in request.data:
        expenditure_update.year = request.data['year']

    expenditure_update.save()
    response = {'county': expenditure_update.county_id, 'employees': expenditure_update.compensation_employees, 'services': expenditure_update.goods_services,
                'subsidies': expenditure_update.subsidies, 'international': expenditure_update.grants_internationalorganisation,
                'government': expenditure_update.grants_governmentunits, 'other_grants': expenditure_update.othergrants,
                'capital_grants': expenditure_update.capitalgrants, 'benefits': expenditure_update.socialbenefits,
                'expense': expenditure_update.otherexpense, 'structures': expenditure_update.buildingstructures,
                'equipment': expenditure_update.plantmachinery_equipment, 'inventory': expenditure_update.inventories,
                'assets': expenditure_update.otherassets, 'financial_assets': expenditure_update.acquisition_financialassets,
                'debt': expenditure_update.interest_debt, 'total': expenditure_update.total_expenditure,
                'year': expenditure_update.year,}
    return Response(response)

#County Expenditure Add View
def addCountyExpenditureView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    # translation.activate('en')
    return render(request, 'knbs_bi/finance_county_expenditure_add.html', context)

#County Expenditure Edit View
def editCountyExpenditureView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/finance_county_expenditure_edit.html', context)

#===============================ECONOMIC CLASIFICATION REVENUE===============================
#All Economic Revenue
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def allEconomicRevenue(request):
    all_economic = Economic_Classification_Revenue.objects.all()

    economics = []

    if all_economic:
        for economic in all_economic:
            c = {'tax_income': economic.taxes_income_profits_capitalgains, 'tax_property':economic.taxes_property, 'tax_vat':economic.taxes_vat, 'tax_good':economic.taxes_othergoodsandservices,
                 'tax_trade':economic.taxes_internationaltrade_transactions, 'other_tax':economic.other_taxes_notelsewhereclasified,
                 'total_tax': economic.totaltax_revenue, 'security':economic.socialsecuritycontributions,
                 'income': economic.property_income, 'sales':economic.sale_goodsandservices,
                 'fines': economic.fines_penaltiesandforfeitures, 'repayment':economic.repayments_domesticlending,
                 'receipts': economic.other_receiptsnotelsewhereclassified, 'revenue':economic.total_nontax_revenue,
                 'total': economic.total, 'year':economic.year}
            economics.append(c)
    else:
        pass

    return Response(economics)

#Launch Page
def allEconomicRevenueView(request):
    all_economic = Economic_Classification_Revenue.objects.all()

    economics = []

    if all_economic:
        for economic in all_economic:
            c = {'id': economic.economicrevenue_id, 'tax_income': economic.taxes_income_profits_capitalgains, 'tax_property':economic.taxes_property, 'tax_vat':economic.taxes_vat, 'tax_good':economic.taxes_othergoodsandservices,
                 'tax_trade':economic.taxes_internationaltrade_transactions, 'other_tax':economic.other_taxes_notelsewhereclasified,
                 'total_tax': economic.totaltax_revenue, 'security':economic.socialsecuritycontributions,
                 'income': economic.property_income, 'sales':economic.sale_goodsandservices,
                 'fines': economic.fines_penaltiesandforfeitures, 'repayment':economic.repayments_domesticlending,
                 'receipts': economic.other_receiptsnotelsewhereclassified, 'revenue':economic.total_nontax_revenue,
                 'total': economic.total, 'year':economic.year}
            economics.append(c)
            context = {'economics': economics}
    else:
        pass

    return render(request, 'knbs_bi/finance_economic_classification_revenue.html', context)

#Outstanding Economic Revenue Add View
def addEconomicRevenueView(request):
    return render(request, 'knbs_bi/finance_economic_classification_revenue_add.html')

#Outstanding Economic Revenue Edit View
def editEconomicRevenueView(request):
    return render(request, 'knbs_bi/finance_economic_classification_revenue_edit.html')

# View All Economic Revenue
def viewEconomicRevenue(request):
    return render(request, template_name='knbs_bi/finance_economic_classification_revenue_view.html')

#Add Economic Revenue
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addEconomicRevenue(request):
    if request.method == 'POST':
        economic_add = Economic_Classification_Revenue(taxes_income_profits_capitalgains = request.data['tax_income'], taxes_property = request.data['tax_property'], taxes_vat = request.data['tax_vat'],
                                                     taxes_othergoodsandservices = request.data['tax_good'], taxes_internationaltrade_transactions = request.data['tax_trade'],
                                                     other_taxes_notelsewhereclasified = request.data['other_tax'], totaltax_revenue = request.data['total_tax'],
                                                     socialsecuritycontributions=request.data['security'], property_income = request.data['income'],
                                                     sale_goodsandservices=request.data['sales'], fines_penaltiesandforfeitures = request.data['fines'],
                                                     repayments_domesticlending=request.data['repayment'], other_receiptsnotelsewhereclassified = request.data['receipts'],
                                                     total_nontax_revenue=request.data['revenue'], total = request.data['total'],
                                                     year=request.data['year'])

        if economic_add:
            economic_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Economic Revenue
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editEconomicRevenue(request):
    economic_update = Economic_Classification_Revenue.objects.get(economicrevenue_id = request.data['economic'])

    if 'tax_income' in request.data:
        economic_update.taxes_income_profits_capitalgains = request.data['tax_income']
    if 'tax_property' in request.data:
        economic_update.taxes_property = request.data['tax_property']
    if 'tax_vat' in request.data:
        economic_update.taxes_vat = request.data['tax_vat']
    if 'tax_good' in request.data:
        economic_update.taxes_othergoodsandservices = request.data['tax_good']
    if 'tax_trade' in request.data:
        economic_update.taxes_internationaltrade_transactions = request.data['tax_trade']
    if 'other_tax' in request.data:
        economic_update.other_taxes_notelsewhereclasified = request.data['other_tax']
    if 'total_tax' in request.data:
        economic_update.totaltax_revenue = request.data['total_tax']
    if 'security' in request.data:
        economic_update.socialsecuritycontributions = request.data['security']
    if 'income' in request.data:
        economic_update.property_income = request.data['income']
    if 'sales' in request.data:
        economic_update.sale_goodsandservices = request.data['sales']
    if 'fines' in request.data:
        economic_update.fines_penaltiesandforfeitures = request.data['fines']
    if 'repayment' in request.data:
        economic_update.repayments_domesticlending = request.data['repayment']
    if 'receipts' in request.data:
        economic_update.other_receiptsnotelsewhereclassified = request.data['receipts']
    if 'revenue' in request.data:
        economic_update.total_nontax_revenue = request.data['revenue']
    if 'total' in request.data:
        economic_update.total = request.data['total']
    if 'year' in request.data:
        economic_update.year = request.data['year']

    economic_update.save()
    response = {'tax_income': economic_update.taxes_income_profits_capitalgains, 'tax_property': economic_update.taxes_property, 'tax_vat': economic_update.taxes_vat,
                'tax_good': economic_update.taxes_othergoodsandservices, 'tax_trade': economic_update.taxes_internationaltrade_transactions,
                'other_tax': economic_update.other_taxes_notelsewhereclasified, 'total_tax': economic_update.totaltax_revenue,
                'security': economic_update.socialsecuritycontributions, 'income': economic_update.property_income,
                'sales': economic_update.sale_goodsandservices, 'fines': economic_update.fines_penaltiesandforfeitures,
                'repayment': economic_update.repayments_domesticlending, 'receipts': economic_update.other_receiptsnotelsewhereclassified,
                'revenue': economic_update.total_nontax_revenue, 'total': economic_update.total_nontax_revenue,
                'year': economic_update.year}
    return Response(response)

#===============================OUTSTANDING DEBT INTERNATIONAL ORGANISATION===============================
#All Outstanding Debt International
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def allDebtInternational(request):
    all_international = Outstanding_Debt_International_Organization.objects.all()

    debts = []

    if all_international:
        for debt in all_international:
            c = {'ida': debt.ida, 'eec':debt.eec_eib, 'imf':debt.imf, 'adb':debt.adf_adb,
                 'banks':debt.commercial_banks, 'others':debt.others, 'year':debt.year}
            debts.append(c)
    else:
        pass

    return Response(debts)

#Launch Page
def allDebtInternationalView(request):
    all_international = Outstanding_Debt_International_Organization.objects.all()

    debts = []

    if all_international:
        for debt in all_international:
            c = {'id': debt.outstanding_debt_id, 'ida': debt.ida, 'eec':debt.eec_eib, 'imf':debt.imf, 'adb':debt.adf_adb,
                 'banks':debt.commercial_banks, 'others':debt.others, 'year':debt.year}
            debts.append(c)
            context = {'debts': debts}
    else:
        pass

    return render(request, 'knbs_bi/finance_outstanding_debt_international_organization.html', context)

#Outstanding Debt International Add View
def addDebtInternationalView(request):
    return render(request, 'knbs_bi/finance_outstanding_debt_international_organization_add.html')

#Outstanding Debt International Edit View
def editDebtInternationalView(request):
    return render(request, 'knbs_bi/finance_outstanding_debt_international_organization_edit.html')

#Add Outstanding Debt International
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addDebtInternational(request):
    if request.method == 'POST':
        international_add = Outstanding_Debt_International_Organization(ida = request.data['ida'], eec_eib = request.data['eec'], imf = request.data['imf'],
                                                                     adf_adb = request.data['adb'], commercial_banks = request.data['banks'],
                                                                     others = request.data['others'], year = request.data['year'])

        if international_add:
            international_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Outstanding Debt International
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editDebtInternational(request):
    international_update = Outstanding_Debt_International_Organization.objects.get(outstanding_debt_id=request.data['debt'])

    if 'ida' in request.data:
        international_update.ida = request.data['ida']
    if 'eec' in request.data:
        international_update.eec_eib = request.data['eec']
    if 'imf' in request.data:
        international_update.imf = request.data['imf']
    if 'adb' in request.data:
        international_update.adf_adb = request.data['adb']
    if 'banks' in request.data:
        international_update.commercial_banks = request.data['banks']
    if 'others' in request.data:
        international_update.others = request.data['others']
    if 'year' in request.data:
        international_update.year = request.data['year']

    international_update.save()
    response = {'ida': international_update.ida, 'eec': international_update.eec_eib, 'imf': international_update.imf,
                'adb': international_update.adf_adb, 'banks': international_update.commercial_banks,
                'others': international_update.others, 'year': international_update.year}
    return Response(response)

#===============================OUTSTANDING DEBT LENDING COUNTRY===============================
#Launch Page
def allDebtLendingView(request):
    all_lending = Outstanding_Debt_Lending_Country.objects.all()

    debts = []

    if all_lending:
        for debt in all_lending:
            c = {'id':debt.lending_country_id, 'germany': debt.germany, 'japan':debt.japan, 'france':debt.france, 'usa':debt.usa,
                 'netherlands':debt.netherlands, 'denmark':debt.denmark, 'finland':debt.finland,
                 'china': debt.china, 'belgium':debt.belgium, 'other':debt.other, 'year':debt.year}
            debts.append(c)
            context = {'debts': debts}
    else:
        pass

    return render(request, 'knbs_bi/finance_outstanding_debt_lending_country.html', context)

#All Outstanding Debt Lending
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def allDebtLending(request):
    all_lending = Outstanding_Debt_Lending_Country.objects.all()

    debts = []

    if all_lending:
        for debt in all_lending:
            c = {'germany': debt.germany, 'japan':debt.japan, 'france':debt.france, 'usa':debt.usa,
                 'netherlands':debt.netherlands, 'denmark':debt.denmark, 'finland':debt.finland,
                 'china': debt.china, 'belgium':debt.belgium, 'other':debt.other, 'year':debt.year}
            debts.append(c)
    else:
        pass

    return Response(debts)

#Add Outstanding Debt Lending
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addDebtLending(request):
    if request.method == 'POST':
        lending_add = Outstanding_Debt_Lending_Country(germany = request.data['germany'], japan = request.data['japan'], france = request.data['france'],
                                                                     usa = request.data['usa'], netherlands = request.data['netherlands'],
                                                                     denmark = request.data['denmark'], finland = request.data['finland'],
                                                               china=request.data['china'], belgium = request.data['belgium'],
                                                               other=request.data['other'], year = request.data['year'])

        if lending_add:
            lending_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Outstanding Debt Lending
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editDebtLending(request):
    lending_update = Outstanding_Debt_Lending_Country.objects.get(lending_country_id = request.data['lending'])

    if 'germany' in request.data:
        lending_update.germany = request.data['germany']
    if 'japan' in request.data:
        lending_update.japan = request.data['japan']
    if 'france' in request.data:
        lending_update.france = request.data['france']
    if 'usa' in request.data:
        lending_update.usa = request.data['usa']
    if 'netherlands' in request.data:
        lending_update.netherlands = request.data['netherlands']
    if 'denmark' in request.data:
        lending_update.denmark = request.data['denmark']
    if 'finland' in request.data:
        lending_update.finland = request.data['finland']
    if 'china' in request.data:
        lending_update.china = request.data['china']
    if 'belgium' in request.data:
        lending_update.belgium = request.data['belgium']
    if 'other' in request.data:
        lending_update.other = request.data['other']
    if 'year' in request.data:
        lending_update.year = request.data['year']

    lending_update.save()
    response = {'germany': lending_update.germany, 'japan': lending_update.japan, 'france': lending_update.france,
                'usa': lending_update.usa, 'netherlands': lending_update.netherlands,
                'denmark': lending_update.denmark, 'finland': lending_update.finland,
                'china': lending_update.china, 'belgium': lending_update.belgium,
                'other': lending_update.other, 'year': lending_update.year}
    return Response(response)

#Outstanding Debt Lending Add View
def addDebtLendingView(request):
    return render(request, 'knbs_bi/finance_outstanding_debt_lending_country_add.html')

#Outstanding Debt Lending Edit View
def editDebtLendingView(request):
    return render(request, 'knbs_bi/finance_outstanding_debt_lending_country_edit.html')

#===============================EXCISE REVENUE COMMODITY===============================
#Launch Page
def allExciseRevenueView(request):
    all_excise = Excise_Revenue_Commodity.objects.all()

    commodities = []

    if all_excise:
        for commodity in all_excise:
            c = {'id':commodity.excise_id, 'year': commodity.year, 'beer':commodity.beer, 'cigarettes':commodity.cigarettes, 'waters':commodity.mineral_waters,
                 'spirits':commodity.wines_spirits, 'commodities':commodity.other_commodities, 'total':commodity.total}
            commodities.append(c)
            context = {'commodities':commodities}
    else:
        pass

    return render(request, 'knbs_bi/finance_excise_revenue_commodity.html', context)


#All Excise Commodity
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def allExciseRevenue(request):
    all_excise = Excise_Revenue_Commodity.objects.all()

    commodities = []

    if all_excise:
        for commodity in all_excise:
            c = {'year': commodity.year, 'beer':commodity.beer, 'cigarettes':commodity.cigarettes, 'waters':commodity.mineral_waters,
                 'spirits':commodity.wines_spirits, 'commodities':commodity.other_commodities, 'total':commodity.total}
            commodities.append(c)
    else:
        pass

    return Response(commodities)

#Add Excise Commodity
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addExciseRevenue(request):
    if request.method == 'POST':
        excise_add = Excise_Revenue_Commodity(year = request.data['year'], beer = request.data['beer'], cigarettes = request.data['cigarettes'],
                                            mineral_waters = request.data['waters'], wines_spirits = request.data['spirits'],
                                            other_commodities = request.data['commodities'], total = request.data['total'])

        if excise_add:
            excise_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Excise Commodity
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editExciseRevenue(request):
    excise = Excise_Revenue_Commodity.objects.get(excise_id = request.data['excise'])

    if 'year' in request.data:
        excise.year = request.data['year']
    if 'beer' in request.data:
        excise.beer = request.data['beer']
    if 'cigarettes' in request.data:
        excise.cigarettes = request.data['cigarettes']
    if 'waters' in request.data:
        excise.mineral_waters = request.data['waters']
    if 'spirits' in request.data:
        excise.wines_spirits = request.data['spirits']
    if 'commodities' in request.data:
        excise.other_commodities = request.data['commodities']
    if 'total' in request.data:
        excise.total = request.data['total']

    excise.save()
    response = {'year': excise.year, 'beer': excise.beer, 'cigarettes': excise.cigarettes,
                'waters': excise.mineral_waters, 'spirits': excise.wines_spirits,
                'commodities': excise.other_commodities, 'total': excise.total}
    return Response(response)

#Excise Commodity Add View
def addExciseRevenueView(request):
    return render(request, 'knbs_bi/finance_excise_revenue_commodity_add.html')

#Excise Commodity Edit View
def editExciseRevenueView(request):
    return render(request, 'knbs_bi/finance_excise_revenue_commodity_edit.html')
#===============================COUNTY BUDGET ALLOCATION===============================
#All County Budget Allocation
from health.models import Counties, SubCounty
#Launch Page
def viewCountyAllocation(request):
    all_allocation = County_Budget_Allocation.objects.all();

    revenues = []

    if all_allocation:
        for revenue in all_allocation:
            counties = Counties.objects.get(county_id=revenue.county_id)
            c = {'id':revenue.budget_allocation_id, 'county': counties.county_name, 'recurrent': revenue.recurrent, 'development': revenue.development,
                 'total': revenue.total_allocation, 'year': revenue.year}
            revenues.append(c)
            context = {'allocations': revenues}
    return render(request, 'knbs_bi/finance_county_budget_allocation.html', context)

#County Budget Allocation Add View
def addCountyAllocationView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    # translation.activate('en')
    return render(request, 'knbs_bi/finance_county_budget_allocation_add.html', context)

#County Budget Allocation Edit View
def editCountyAllocationView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/finance_county_budget_allocation_edit.html', context)

#All County Budget Allocation
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def allCountyAllocation(request):
    all_allocation = County_Budget_Allocation.objects.all()

    allocations = []

    if all_allocation:
        for allocation in all_allocation:
            counties = Counties.objects.get(county_id=allocation.county_id)
            c = {'county': counties.county_name, 'recurrent':allocation.recurrent, 'development':allocation.development,
                 'total':allocation.total_allocation, 'year':allocation.year}
            allocations.append(c)
    else:
        pass

    return Response(allocations)

#Add County Budget Allocation
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addCountyAllocation(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id
        allocation_add = County_Budget_Allocation(county_id = kaunti, recurrent = request.data['recurrent'], development = request.data['development'],
                                                total_allocation = request.data['total'], year = request.data['year'])

        if allocation_add:
            allocation_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit County Budget Allocation
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editCountyAllocation(request):
    allocation = County_Budget_Allocation.objects.get(budget_allocation_id = request.data['allocation_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            allocation.county_id = counties.county_id
    if 'recurrent' in request.data:
        allocation.recurrent = request.data['recurrent']
    if 'development' in request.data:
        allocation.development = request.data['development']
    if 'total' in request.data:
        allocation.total_allocation = request.data['total']
    if 'year' in request.data:
        allocation.year = request.data['year']

    allocation.save()
    # response = {'county': allocation.county_id, 'recurrent': allocation.recurrent, 'development': allocation.development,
    #             'total': allocation.total, 'year': allocation.year}
    return Response(status=status.HTTP_201_CREATED)

#===============================NATIONAL GOVERNMENT EXPENDITURE===============================
#All National Expenditure
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def allNationalExpenditure(request):
    all_expenditure = National_Government_Expenditure.objects.all()

    expenditures = []

    if all_expenditure:
        for expenditure in all_expenditure:
            c = {'non_financial': expenditure.acquisition_nonfinancial_assets, 'financial':expenditure.acquisition_financial_assets, 'loans':expenditure.loans_repayments,
                 'compensation':expenditure.compensation_employees, 'goods':expenditure.goods_services, 'subsidies':expenditure.subsidies,
                 'interest': expenditure.interest, 'grants':expenditure.grants, 'expenses':expenditure.other_expense,
                 'benefits': expenditure.social_benefits, 'capital':expenditure.capital_grants, 'total':expenditure.total,
                 'year': expenditure.year}
            expenditures.append(c)
    else:
        pass

    return Response(expenditures)

#Launch Page
def allNationalExpenditureView(request):
    all_expenditure = National_Government_Expenditure.objects.all()

    expenditures = []

    if all_expenditure:
        for expenditure in all_expenditure:
            c = {'id': expenditure.government_expenditure_id, 'non_financial': expenditure.acquisition_nonfinancial_assets, 'financial':expenditure.acquisition_financial_assets, 'loans':expenditure.loans_repayments,
                 'compensation':expenditure.compensation_employees, 'goods':expenditure.goods_services, 'subsidies':expenditure.subsidies,
                 'interest': expenditure.interest, 'grants':expenditure.grants, 'expenses':expenditure.other_expense,
                 'benefits': expenditure.social_benefits, 'capital':expenditure.capital_grants, 'total':expenditure.total,
                 'year': expenditure.year}
            expenditures.append(c)
            context = {'expenditures': expenditures}
    else:
        pass

    return render(request, 'knbs_bi/finance_national_government_expenditure.html', context)

#National Expenditure Purpose Add View
def addNationalExpenditureView(request):
    return render(request, 'knbs_bi/finance_national_government_expenditure_add.html')

#National Expenditure Purpose Edit View
def editNationalExpenditureView(request):
    return render(request, 'knbs_bi/finance_national_government_expenditure_edit.html')

# View All National Expenditure Purpose
def viewNationalExpenditure(request):
    return render(request, template_name='knbs_bi/finance_national_government_expenditure_view.html')

#Add National Expenditure
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addNationalExpenditure(request):
    if request.method == 'POST':
        expenditure_add = National_Government_Expenditure(acquisition_nonfinancial_assets = request.data['non_financial'], acquisition_financial_assets = request.data['financial'], loans_repayments = request.data['loans'],
                                                 compensation_employees = request.data['compensation'], goods_services = request.data['goods'],
                                                 subsidies=request.data['subsidies'], interest = request.data['interest'],
                                                 grants=request.data['grants'], other_expense = request.data['expenses'],
                                                 social_benefits=request.data['benefits'], capital_grants = request.data['capital'],
                                                 total=request.data['total'], year = request.data['year'])

        if expenditure_add:
            expenditure_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit National Expenditure
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editNationalExpenditure(request):
    expenditure = National_Government_Expenditure.objects.get(government_expenditure_id = request.data['expenditure'])

    if 'non_financial' in request.data:
        expenditure.acquisition_nonfinancial_assets = request.data['non_financial']
    if 'financial' in request.data:
        expenditure.acquisition_financial_assets = request.data['financial']
    if 'loans' in request.data:
        expenditure.loans_repayments = request.data['loans']
    if 'compensation' in request.data:
        expenditure.compensation_employees = request.data['compensation']
    if 'goods' in request.data:
        expenditure.goods_services = request.data['goods']
    if 'subsidies' in request.data:
        expenditure.subsidies = request.data['subsidies']
    if 'interest' in request.data:
        expenditure.interest = request.data['interest']
    if 'grants' in request.data:
        expenditure.grants = request.data['grants']
    if 'expenses' in request.data:
        expenditure.other_expense = request.data['expenses']
    if 'benefits' in request.data:
        expenditure.social_benefits = request.data['benefits']
    if 'capital' in request.data:
        expenditure.capital_grants = request.data['capital']
    if 'total' in request.data:
        expenditure.total = request.data['total']
    if 'year' in request.data:
        expenditure.year = request.data['year']

    expenditure.save()
    response = {'nonfinancial': expenditure.acquisition_nonfinancial_assets, 'financial': expenditure.acquisition_financial_assets, 'loans': expenditure.loans_repayments,
                'compensation': expenditure.compensation_employees, 'goods': expenditure.goods_services,
                'subsidies': expenditure.subsidies, 'interest': expenditure.interest,
                'grants': expenditure.grants, 'expenses': expenditure.other_expense,
                'benefits': expenditure.social_benefits, 'capital': expenditure.capital_grants,
                'total': expenditure.total, 'year': expenditure.year}
    return Response(response)

#===============================NATIONAL GOVERNMENT EXPENDITURE PURPOSE===============================
#All National Expenditure Purpose
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def allNationalPurpose(request):
    all_purpose = National_Government_Expenditure_Purpose.objects.all()

    purposes = []

    if all_purpose:
        for purpose in all_purpose:
            c = {'year': purpose.year, 'general':purpose.general_publicservices, 'public':purpose.public_debttransactions,
                 'transfers':purpose.transfers, 'defense':purpose.defense, 'orders':purpose.order_safety,
                 'economic': purpose.economic_commercial_labor, 'agriculture':purpose.agriculture, 'fuel':purpose.fuel_energy,
                 'mining': purpose.mining_manufacturing_construction, 'transport':purpose.transport, 'communication':purpose.communication,
                 'other': purpose.other_industries, 'environmental': purpose.environmental_protection, 'housing': purpose.housing_communityamenities,
                 'health': purpose.health, 'recreation': purpose.recreation_culture_religion, 'education': purpose.education,
                 'social': purpose.socialprotection}
            purposes.append(c)
    else:
        pass

    return Response(purposes)

#Launch Page
def allNationalPurposeView(request):
    all_purpose = National_Government_Expenditure_Purpose.objects.all()

    purposes = []

    if all_purpose:
        for purpose in all_purpose:
            c = {'id': purpose.purpose_id, 'year': purpose.year, 'general':purpose.general_publicservices, 'public':purpose.public_debttransactions,
                 'transfers':purpose.transfers, 'defense':purpose.defense, 'orders':purpose.order_safety,
                 'economic': purpose.economic_commercial_labor, 'agriculture':purpose.agriculture, 'fuel':purpose.fuel_energy,
                 'mining': purpose.mining_manufacturing_construction, 'transport':purpose.transport, 'communication':purpose.communication,
                 'other': purpose.other_industries, 'environmental': purpose.environmental_protection, 'housing': purpose.housing_communityamenities,
                 'health': purpose.health, 'recreation': purpose.recreation_culture_religion, 'education': purpose.education,
                 'social': purpose.socialprotection}
            purposes.append(c)
            context = {'purposes': purposes}
    else:
        pass

    return render(request, 'knbs_bi/finance_national_government_expenditure_purpose.html', context)

#National Expenditure Purpose Add View
def addNationalPurposeView(request):
    return render(request, 'knbs_bi/finance_national_government_expenditure_purpose_add.html')

#National Expenditure Purpose Edit View
def editNationalPurposeView(request):
    return render(request, 'knbs_bi/finance_national_government_expenditure_purpose_edit.html')

# View All National Expenditure Purpose
def viewNationalPurpose(request):
    return render(request, template_name='knbs_bi/finance_national_government_expenditure_purpose_view.html')


#Add National Expenditure Purpose
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addNationalPurpose(request):
    if request.method == 'POST':
        purpose_add = National_Government_Expenditure_Purpose(year = request.data['year'], general_publicservices = request.data['general'], public_debttransactions = request.data['public'],
                                                           transfers = request.data['transfers'], defense = request.data['defense'],
                                                           order_safety=request.data['orders'], economic_commercial_labor = request.data['economic'],
                                                           agriculture=request.data['agriculture'], fuel_energy = request.data['fuel'],
                                                           mining_manufacturing_construction=request.data['mining'], transport = request.data['transport'],
                                                           communication=request.data['communication'], other_industries = request.data['other'],
                                                           environmental_protection=request.data['environmental'], housing_communityamenities = request.data['housing'],
                                                           health=request.data['health'], recreation_culture_religion = request.data['recreation'],
                                                           education=request.data['education'], socialprotection = request.data['social'])

        if purpose_add:
            purpose_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit National Expenditure Purpose
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editNationalPurpose(request):
    purpose = National_Government_Expenditure_Purpose.objects.get(purpose_id = request.data['purpose'])

    if 'year' in request.data:
        purpose.year = request.data['year']
    if 'general' in request.data:
        purpose.general_publicservices = request.data['general']
    if 'public' in request.data:
        purpose.public_debttransactions = request.data['public']
    if 'transfers' in request.data:
        purpose.transfers = request.data['transfers']
    if 'defense' in request.data:
        purpose.defense = request.data['defense']
    if 'orders' in request.data:
        purpose.order_safety = request.data['orders']
    if 'economic' in request.data:
        purpose.economic_commercial_labor = request.data['economic']
    if 'agriculture' in request.data:
        purpose.agriculture = request.data['agriculture']
    if 'fuel' in request.data:
        purpose.fuel_energy = request.data['fuel']
    if 'mining' in request.data:
        purpose.mining_manufacturing_construction = request.data['mining']
    if 'transport' in request.data:
        purpose.transport = request.data['transport']
    if 'communication' in request.data:
        purpose.communication = request.data['communication']
    if 'other' in request.data:
        purpose.other_industries = request.data['other']
    if 'environmental' in request.data:
        purpose.environmental_protection = request.data['environmental']
    if 'housing' in request.data:
        purpose.housing_communityamenities = request.data['housing']
    if 'health' in request.data:
        purpose.health = request.data['health']
    if 'recreation' in request.data:
        purpose.recreation_culture_religion = request.data['recreation']
    if 'education' in request.data:
        purpose.education = request.data['education']
    if 'social' in request.data:
        purpose.socialprotection = request.data['social']

    purpose.save()
    response = {'year': purpose.year, 'general': purpose.general_publicservices, 'public': purpose.public_debttransactions,
                'transfers': purpose.transfers, 'defense': purpose.defense,
                'orders': purpose.order_safety, 'economic': purpose.economic_commercial_labor,
                'agriculture': purpose.agriculture, 'fuel': purpose.fuel_energy,
                'mining': purpose.mining_manufacturing_construction, 'transport': purpose.transport,
                'communication': purpose.communication, 'other': purpose.other_industries,
                'environmental': purpose.environmental_protection, 'housing': purpose.housing_communityamenities,
                'health': purpose.health, 'recreation': purpose.recreation_culture_religion,
                'education': purpose.education, 'social': purpose.socialprotection}
    return Response(response)

#===============================CDF ALLOCATION===============================
#All County Budget Allocation
from health.models import Counties, SubCounty
#Launch Page
def viewCdfAllocation(request):
    all_allocation = Cdf_Allocation_By_Constituency.objects.all();

    revenues = []

    if all_allocation:
        for revenue in all_allocation:
            counties = Counties.objects.get(county_id=revenue.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=revenue.subcounty_id)
            if subcounty:
                for sc in subcounty:
                    c = {'id': revenue.cdf_allocation_id, 'county': counties.county_name, 'subcounty': sc.subcounty_name, 'cdf_amount': revenue.cdf_amount,
                         'year': revenue.year}
                    revenues.append(c)
                    context = {'allocations': revenues}
    else:
        pass
    return render(request, 'knbs_bi/finance_cdf_allocation.html', context)

#Cdf Allocation Add View
def addCdfAllocationView(request):
    all_counties = Counties.objects.all()
    sub_county = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': sub_county}
    # translation.activate('en')
    return render(request, 'knbs_bi/finance_cdf_allocation_add.html', context)

#Cdf Allocation Edit View
def editCdfAllocationView(request):
    all_counties = Counties.objects.all()
    sub_county = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': sub_county}
    return render(request, 'knbs_bi/finance_cdf_allocation_edit.html', context)

#All County Budget Allocation
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def allCdfAllocation(request):
    all_allocation = Cdf_Allocation_By_Constituency.objects.all();

    revenues = []

    if all_allocation:
        for revenue in all_allocation:
            counties = Counties.objects.get(county_id=revenue.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=revenue.subcounty_id)
            if subcounty:
                for sc in subcounty:
                    c = {'county': counties.county_name,
                         'subcounty': sc.subcounty_name, 'cdf_amount': revenue.cdf_amount,
                         'year': revenue.year}
                    revenues.append(c)
    else:
        pass

    return Response(revenues)

#Add Cdf Allocation
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addCdfAllocation(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])

    if counties and sub:
        kaunti = counties.county_id
        sub_kaunti = sub.subcounty_id
        allocation_add = Cdf_Allocation_By_Constituency(county_id = kaunti, subcounty_id = sub_kaunti, cdf_amount = request.data['allocation'],
                                                year = request.data['year'])

        if allocation_add:
            allocation_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Edit Cdf Allocation
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editCdfAllocation(request):
    allocation_edit = Cdf_Allocation_By_Constituency.objects.get(cdf_allocation_id = request.data['allocation_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            allocation_edit.county_id = counties.county_id

    if 'sub_county' in request.data:
        sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])
        if sub:
            allocation_edit.subcounty_id = sub.subcounty_id
    if 'allocation' in request.data:
        allocation_edit.cdf_amount = request.data['allocation']
    if 'year' in request.data:
        allocation_edit.year = request.data['year']

    allocation_edit.save()

    return Response(status=status.HTTP_201_CREATED)

#===============================MONEY BANKING INSTITUTIONS===============================
# #All Money Banking Institutions
# from health.models import Counties, SubCounty
# #Launch Page
# def viewBankingInstitution(request):
#     all_banks = Money_Banking_Institutions.objects.all();
#
#     revenues = []
#
#     if all_banks:
#         for revenue in all_banks:
#             counties = Counties.objects.get(county_id=revenue.county_id)
#             institution = Money_Banking_Index.objects.get(institution_id=revenue.institution_id)
#             subcounty = SubCounty.objects.filter(subcounty_id=revenue.subcounty_id)
#             if subcounty:
#                 for sc in subcounty:
#                     c = {'id': revenue.moneybanking_id, 'county': counties.county_name, 'subcounty': sc.subcounty_name, 'institution': institution.financial_institution,
#                          'number': revenue.number}
#                     revenues.append(c)
#                     context = {'institutions': revenues}
#     else:
#         pass
#     return render(request, 'knbs_bi/finance_money_banking_institutions.html', context)
#
# #Money Banking Institutions Add View
# def addBankingInstitutionView(request):
#     all_counties = Counties.objects.all()
#     sub_county = SubCounty.objects.all()
#     institution = Money_Banking_Index.objects.all()
#     context = {'counties': all_counties, 'sub': sub_county, 'inst': institution}
#     # translation.activate('en')
#     return render(request, 'knbs_bi/finance_money_banking_institutions_add.html', context)
#
# #Money Banking Institutions Edit View
# def editBankingInstitutionView(request):
#     all_counties = Counties.objects.all()
#     sub_county = SubCounty.objects.all()
#     institution = Money_Banking_Index.objects.all()
#     context = {'counties': all_counties, 'sub': sub_county, 'inst': institution}
#     return render(request, 'knbs_bi/finance_money_banking_institutions_edit.html', context)
#
# # #All County Budget Allocation
# # @api_view(http_method_names=['GET'])
# # @renderer_classes((JSONRenderer,))
# # def allCdfAllocation(request):
# #     all_allocation = County_Budget_Allocation.objects.all()
# #
# #     allocations = []
# #
# #     if all_allocation:
# #         for allocation in all_allocation:
# #             counties = Counties.objects.get(county_id=allocation.county_id)
# #             c = {'county': counties.county_name, 'recurrent':allocation.recurrent, 'development':allocation.development,
# #                  'total':allocation.total, 'year':allocation.year}
# #             allocations.append(c)
# #     else:
# #         pass
# #
# #     return Response(allocations)
#
# #Add County Budget Allocation
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def addBankingInstitution(request):
#     counties = Counties.objects.get(county_name=request.data['county'])
#     sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])
#     institution = Money_Banking_Index.objects.get(financial_institution=request.data['institution'])
#
#     if counties and sub and institution:
#         kaunti = counties.county_id
#         sub_kaunti = sub.subcounty_id
#         instituti = institution.institution_id
#
#         institution_add = Money_Banking_Institutions(county_id = kaunti, subcounty_id = sub_kaunti, institution_id = instituti,
#                                                 number = request.data['number'])
#
#         if institution_add:
#             institution_add.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
# #Edit County Budget Allocation
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def editBankingInstitution(request):
#     institution_edit = Money_Banking_Institutions.objects.get(moneybanking_id = request.data['money_id'])
#
#     if 'county' in request.data:
#         counties = Counties.objects.get(county_name=request.data['county'])
#         if counties:
#             institution_edit.county_id = counties.county_id
#
#     if 'sub_county' in request.data:
#         sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])
#         if sub:
#             institution_edit.subcounty_id = sub.subcounty_id
#
#     if 'institution' in request.data:
#         institution = Money_Banking_Index.objects.get(financial_institution=request.data['institution'])
#         if institution:
#             institution_edit.institution_id = institution.institution_id
#     if 'number' in request.data:
#         institution_edit.number = request.data['number']
#
#     institution_edit.save()
#
#     return Response(status=status.HTTP_201_CREATED)
#
