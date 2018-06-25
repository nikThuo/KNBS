"""knbs_bi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from CPI.views import averageRetail, addAverageRetail, editAverageRetail, cpi, averageRetailView, addAverageRetailView, \
    editAverageRetailView, addConsumerPriceView, editConsumerPriceView, viewConsumerPrice, consumerPriceView, \
    consumerPrice, addConsumerPrice, editConsumerPrice, elementaryWeightsView, addElementaryWeightsView, \
    editElementaryWeightsView, elementaryWeights, addElementaryWeights, editElementaryWeights, editGroupWeights, \
    addGroupWeights, groupWeights, groupWeightsView, addGroupWeightsView, editGroupWeightsView, groupWeightsKenyaView, \
    addGroupWeightsKenyaView, editGroupWeightsKenyaView, groupWeightsKenya, addGroupWeightsKenya, editGroupWeightsKenya
from administrative.views import allUnit, administrative, allUnitView, addUnitView, editUniView, editAdministrative, \
    addAdministrative
from agriculture.views import chemicalFeed, cooperatives, marketProduction, irrigationSchemes, priceMeatMilk, \
    shareCapital, agriculturalInputs, agriculture, editPriceMeatMilkView, addPriceMeatMilkView, viewPriceMeatMilk, \
    viewLandPotential, chemicalFeedView, viewChemFeed, cooperativesView, viewCooperatives, marketProductionView, \
    viewMarketProduction, irrigationSchemesView, viewIrrigationSchemes, shareCapitalView, viewShareCapital, \
    agriculturalInputsView, viewAgriculturalInputs, editLandPotentialView, addLandPotentialView, editLandPotential, \
    addLandPotential, editPriceMeatMilk, addPriceMeatMilk, editChemicalFeedView, addChemicalFeedView, editChemicalFeed, \
    addChemicalFeed, addCooperatives, editCooperatives, addCooperativesView, editCooperativesView, addMarketProduction, \
    editMarketProduction, addMarketProductionView, editMarketProductionView, addIrrigationSchemesView, \
    editIrrigationSchemesView, addIrrigationSchemes, editIrrigationSchemes, addShareCapital, editShareCapital, \
    addShareCapitalView, editShareCapitalView, addAgriculturalInputsView, editAgriculturalInputsView, \
    addAgriculturalInputs, editAgriculturalInputs, areaSugarcane, addAreaSugarcaneView, editAreaSugarcaneView, \
    landPotential, viewAreaSugarcane, addAreaSugarcane, editAreaSugarcane, agriculturalLand, addAgriculturalLand, \
    editAgriculturalLand, viewAgriculturalLand, addAgriculturalLandView, editAgriculturalLandView, areaCoffeeView, \
    addAreaCoffeeView, editAreaCoffeeView, areaCoffee, addAreaCoffee, editAreaCoffee, areaTea, addAreaTea, editAreaTea, \
    areaTeaView, addAreaTeaView, editAreaTeaView, livestockProductsView, addLivestockProductsView, \
    editLivestockProductsView, livestockProducts, addLivestockProducts, editLivestockProducts
from building_and_construction.views import idIndustry, amountBuilding, editAmountBuilding, addAmountBuilding, \
    building_and_construction, viewAmountBuilding, addAmountBuildingView, editAmountBuildingView, \
    editQuarterlyCivilView, addQuarterlyCivilView, quarterlyCivilView, quarterlyCivil, addQuarterlyCivil, \
    editQuarterlyCivil, editQuarterlyNonResidential, addQuarterlyNonResidential, quarterlyNonResidential, \
    editQuarterlyNonResidentialView, addQuarterlyNonResidentialView, quarterlyNonResidentialView, \
    editQuarterlyOverallView, addQuarterlyOverallView, quarterlyOverallView, quarterlyOverall, addQuarterlyOverall, \
    editQuarterlyOverall, editQuarterlyResidential, addQuarterlyResidential, quarterlyResidential, \
    quarterlyResidentialView, addQuarterlyResidentialView, editQuarterlyResidentialView
from education.views import diplomaDegree, trendsKcse, numInstitutions, studentEnrollment, \
    studentEnrollmentPublic, secSchoolEnrollment, adultEducationCentres, adultEducationEnrolment, \
    adultEducationProficiency, ecdeCategorySubCounty, primaryEnrollmentIndicators, primaryEnrollmentSexCounty, \
    primaryCategorySubCounty, secondaryEnrollmentIndicators, secondaryEnrollmentSexCounty, secondaryCategorySubCounty, \
    studentEnrollmentPolytechnic, teacherTrainingColleges, polytechnicCategorySubcounty, education, \
    viewSecSchoolEnrollment, addSecSchoolEnrollment, editSecSchoolEnrollment, editSchoolEnrollment, addSchoolEnrollment, \
    primaryCategorySubCountyView, addCategorySubCountyView, editCategorySubCountyView, editPrimaryCategorySubCounty, \
    addPrimaryCategorySubCounty, editSecondaryEnrollmentIndicatorsView, addSecondaryEnrollmentIndicatorsView, \
    secondaryEnrollmentIndicatorsView, studentEnrollmentPolytechnicView, teacherTrainingCollegesView, \
    ecdeCategorySubCountyView, primaryEnrollmentIndicatorsView, adultEducationCentresView, adultEducationEnrolmentView, \
    adultEducationProficiencyView, editSecondaryEnrollmentIndicators, addSecondaryEnrollmentIndicators, \
    editPrimaryEnrollmentSexCounty, addPrimaryEnrollmentSexCounty, morePrimaryEnrollmentSexCounty, \
    editPrimaryEnrollmentSexCountyView, addPrimaryEnrollmentSexCountyView, primaryEnrollmentSexCountyView, \
    addTeacherTrainingCollegesView, editTeacherTrainingCollegesView, editTeacherTrainingColleges, \
    addTeacherTrainingColleges, editStudentEnrollmentPolytechnic, addStudentEnrollmentPolytechnic, \
    editStudentEnrollmentPolytechnicView, addStudentEnrollmentPolytechnicView, editPolytechnicCategorySubcountyView, \
    addPolytechnicCategorySubcountyView, polytechnicCategorySubcountyView, editPolytechnicCategorySubcounty, \
    addPolytechnicCategorySubcounty, editAdultEducationProficiency, addAdultEducationProficiency, \
    editAdultEducationProficiencyView, addAdultEducationProficiencyView, addEcdeCategorySubCountyView, \
    editEcdeCategorySubCountyView, editEcdeCategorySubCounty, addEcdeCategorySubCounty, \
    addSecondaryEnrollmentSexCountyView, editSecondaryEnrollmentSexCountyView, secondaryEnrollmentSexCountyView, \
    addSecondaryEnrollmentSexCounty, editSecondaryEnrollmentSexCounty, addPrimaryEnrollmentIndicators, \
    editPrimaryEnrollmentIndicators, addPrimaryEnrollmentIndicatorsView, editPrimaryEnrollmentIndicatorsView, \
    addAdultEducationCentresView, editAdultEducationCentresView, addAdultEducationCentres, editAdultEducationCentres, \
    addAdultEducationEnrolment, editAdultEducationEnrolment, addAdultEducationEnrolmentView, \
    editAdultEducationEnrolmentView, addDiplomaDegree, editDiplomaDegree, diplomaDegreeView, addDiplomaDegreeView, \
    editDiplomaDegreeView, studentEnrollmentPublicView, addStudentEnrollmentPublicView, editStudentEnrollmentPublicView, \
    addStudentEnrollmentPublic, editStudentEnrollmentPublic, addStudentEnrollment, editStudentEnrollment, \
    studentEnrollmentView, addStudentEnrollmentView, editStudentEnrollmentView, ecdeEnrollmentEdstat, addEcdeEnrollment, \
    editEcdeEnrollment, ecdeEnrollmentView, addEcdeEnrollmentView, editEcdeEnrollmentView, primaryEnrollmentView, \
    addPrimaryEnrollmentView, editPrimaryEnrollmentView, primaryEnrollmentEdstat, addPrimaryEnrollment, \
    editPrimarynrollment, secondaryEnrollmentEdstat, addSecondaryEnrollment, editSecondarynrollment, \
    secondaryEnrollmentView, addSecondaryEnrollmentView, editSecondaryEnrollmentView, kcpeCandidatureView, \
    addKcpeCandidatureView, editKcpeCandidatureView, kcpeCandidature, addKcpeCandidature, editKcpeCandidature, \
    kcpeResults, addKcpeResults, editKcpeResults, kcpeResultsView, addKcpeResultsView, editKcpeResultsView, \
    addKcseResultsView, editKcseResultsView, kcseResults, addKcseResults, editKcseResults
from energy.views import pumpPricesFuel, averagePrices, addAveragePrices, editAveragePrices, energy, averagePricesView, \
    addAveragePricesView, editAveragePricesView, addDomesticSaleView, editDomesticSaleView, domesticSale, \
    addDomesticSale, editDomesticSale, domesticSaleView, editValueQuantityView, addValueQuantityView, valueQuantityView, \
    valueQuantity, addValueQuantity, editValueQuantity, petroleumSupply, addPetroleumSupply, editPetroleumSupply, \
    petroleumSupplyView, addPetroleumSupplyView, editPetroleumSupplyView, editInstalledCapacityView, \
    addInstalledCapacityView, installedCapacityView, installedCapacity, addInstalledCapacity, editInstalledCapacity, \
    generalImports, addGeneralImports, editGeneralImports, generalImportsView, addGeneralImportsView, \
    editGeneralImportsView, electricityDemandView, addElectricityDemandView, editElectricityDemandView, \
    electricityDemand, addElectricityDemand, editElectricityDemand
from finance.views import finance, allCountyRevenue, addCountyRevenue, editCountyRevenue, editCountyExpenditure, \
    addCountyExpenditure, allCountyExpenditure, allEconomicRevenue, addEconomicRevenue, editEconomicRevenue, \
    allDebtInternational, addDebtInternational, editDebtInternational, allDebtLending, addDebtLending, editDebtLending, \
    allExciseRevenue, addExciseRevenue, editExciseRevenue, allCountyAllocation, addCountyAllocation, \
    editCountyAllocation, allNationalExpenditure, addNationalExpenditure, editNationalExpenditure, allNationalPurpose, \
    addNationalPurpose, editNationalPurpose, cdfAllocation, addCountyRevenueView, \
    editCountyRevenueView, viewCountyRevenue, editCountyAllocationView, addCountyAllocationView, viewCountyAllocation, \
    viewCdfAllocation, addCdfAllocationView, editCdfAllocationView, editCdfAllocation, addCdfAllocation, \
    allCountyExpenditureView, viewExpenditure, allDebtLendingView, allExciseRevenueView, editCountyExpenditureView, \
    addCountyExpenditureView, addExciseRevenueView, editExciseRevenueView, addDebtLendingView, editDebtLendingView, \
    allDebtInternationalView, addDebtInternationalView, editDebtInternationalView, allEconomicRevenueView, \
    addEconomicRevenueView, editEconomicRevenueView, viewEconomicRevenue, allNationalPurposeView, \
    addNationalPurposeView, editNationalPurposeView, viewNationalPurpose, allNationalExpenditureView, \
    addNationalExpenditureView, editNationalExpenditureView, viewNationalExpenditure, allCdfAllocation
from general.views import getYear, getCount, requestDataSet
from governance.views import governance, crimesReportedView, offenceSexView, registeredVotersCountyView, \
    casesVariousCourtsView, prisonersOffencesexView, environmentalCrimesView, casesEACCView, casesForwardedActediew, \
    convictedPrisonAgeSexView, policePrisonsProbationView, offenceMoralityView, homicideSexView, robberyTheftView, \
    addCrimesReportedView, editCrimesReportedView, addCrimesReported, editCrimesReported, addOffenceSexView, \
    editOffenceSexView, editOffenceSex, addOffenceSex, editRegisteredVotersCountyView, addRegisteredVotersCountyView, \
    editRegisteredVotersCounty, addRegisteredVotersCounty, casesForwardedActed, casesVariousCourts, casesEACC, \
    crimesReported, offenceSex, registeredVotersCounty, prisonersOffencesex, environmentalCrimes, convictedPrisonAgeSex, \
    policePrisonsProbation, offenceMorality, homicideSex, robberyTheft, dailyAvearge, fireArms, idCards, courtStaff, \
    murderCases, refugeeAgeSex, offendersServing, passportPermits, personsReported, prisonPopulation, publicAssets
from health.views import aboveFive, diseaseList, allDiseases, Deaths, belowFive, allHealthFacilities, allPersonnel, \
    allMembers, allNhifResources, immunizationRate, health, allImmunizationRate, addImmunizationView, \
    editImmunizationView, addImmunization, editImmunization, morbidityBelow, addMorbidityView, editMorbidityView, \
    editMorbidityAboveView, addMorbidityAboveView, morbidityAbove, index, addBelowFive, editBelowFive, addAboveFive, \
    editAboveFive, healthFacility, editHealthOwnershipView, addHealthOwnershipView, healthFacilityView, \
    registeredMedicalPersonnelView, hospitalBedsCotsView, allNhifResourcesView, allMembersView, \
    editHospitalBedsCotsView, addHospitalBedsCotsView, editHospitalBedsCots, addHospitalBedsCots, hospitalBedsCots, \
    contraceptionUseCounty, addContraceptionUseCounty, editContraceptionUseCounty, contraceptionUseCountyView, \
    addContraceptionUseCountyView, editContraceptionUseCountyView, distributionOutpatientProviderView, \
    addDistributionOutpatientProviderView, editDistributionOutpatientProviderView, distributionOutpatientProvider, \
    addDistributionOutpatientProvider, editDistributionOutpatientProvider, insuranceCoverage, addInsuranceCoverage, \
    editInsuranceCoverage, insuranceCoverageView, addInsuranceCoverageView, editInsuranceCoverageView, maternalCareView, \
    addMaternalCareView, editMaternalCareView, maternalCare, addMaternalCare, editMaternalCare, nutritionChildren, \
    addNutritionChildren, editNutritionChildren, nutritionChildrenView, addNutritionChildrenView, \
    editNutritionChildrenView, nutritionWomen, addNutritionWomen, editNutritionWomen, nutritionWomenView, \
    addNutritionWomenView, editNutritionWomenView, registeredLabs, addRegisteredLabs, editRegisteredLabs, \
    registeredLabsView, addRegisteredLabsView, editRegisteredLabsView, editMosquitoNets, addMosquitoNets, mosquitoNets, \
    mosquitoNetsView, addMosquitoNetsView, editMosquitoNetsView, editHivAwarenessView, addHivAwarenessView, \
    hivAwarenessView, hivAwareness, addHivAwareness, editHivAwareness, editNhifActiveMembers, addNhifActiveMembers, \
    nhifActiveMembers, nhifActiveMembersView, addNhifActiveMembersView, editNhifActiveMembersView, healthSectors
from knbs_api import views
#from knbs_api.models import Sectors
# from knbs_api.views import health, health_life_expectancy, health_birth_all, health_death_all, health_birth_add, \
#     health_birth_update, health_birth_delete, health_births, registered_births, index, registered_births_add, \
#     registered_births_update, health_birth_update_load, allDeaths, addDeaths, updateDeaths, registered_deaths, \
#     addDeathsView, editDeathsView, plusDeaths, alterDeaths,  \
#      addDisease, editDisease, addFacility, editFacility,  addPersonnel, \
#     editPersonnel, addMember, editMember, editNhifResource, addNhifResource
#allDiseases, Deaths, , allHealthFacilities allPersonnel, , allMembers , allNhifResources
from labour.views import allSectors, publicSector, labour, addPublicSector, \
    allPublicSectorView, addPublicSectorView, editPublicSectorView, editPublicSector
from land_and_climate.views import editSurfaceArea, addSurfaceArea, land_and_climate, addSurfaceAreaView, \
    editSurfaceAreaView, addTemperature, editTemperature, addTemperatureView, editTemperatureView, editRainfall, \
    addRainfall, viewRainfall, addRainfallView, editRainfallView, viewTemperature, viewSurfaceArea, \
    addTopograhyAltitude, editTopograhyAltitude, editTopograhyAltitudeView, addTopograhyAltitudeView, \
    viewTopograhyAltitude, surfaceArea, Temperature, Temperatures, rain_fall, topograhyAltitude
from manufacturing.views import percentageChange, addPercentageChange, editPercentageChange, quantumIndices, \
    addQuantumIndices, editQuantumIndices, manufacturing, percentageChangeView, addPercentageChangeView, \
    editPercentageChangeView, quantumIndicesView, addQuantumIndicesView, editQuantumIndicesView
from money_and_banking.views import commercialBanks, addCommercialBanks, editCommercialBanks, editCommercialBanksView, \
    addCommercialBanksView, commercialBanksView, money_and_banking, editInflationRatesView, addInflationRatesView, \
    editInflationRates, addInflationRates, inflationRates, interestRates, addInterestRates, editInterestRates, \
    editInterestRatesView, addInterestRatesView, interestRatesView, editMonetaryIndicatorsView, \
    addMonetaryIndicatorsView, monetaryIndicatorsView, monetaryIndicators, addMonetaryIndicators, \
    editMonetaryIndicators, monetaryIndicatorsDomesticView, addMonetaryIndicatorsDomestic, \
    editMonetaryIndicatorsDomestic, editMonetaryIndicatorsDomesticView, addMonetaryIndicatorsDomesticView, \
    monetaryIndicatorsDomestic, editSecuritiesExchange, addSecuritiesExchange, securitiesExchange, \
    securitiesExchangeView, addSecuritiesExchangeView, editSecuritiesExchangeView, bankingInstitution, \
    addBankingInstitution, editBankingInstitution, viewBankingInstitution, addBankingInstitutionView, \
    editBankingInstitutionView, inflationRatesView
from political.views import allUnits, editUnitsView, addUnitsView, allUnitsView, political, editPolitical, addPolitical
from population.views import populationSpecialGroup, populationSelectedAge, populationSex
from tourism.models import Visitors_To_Museums
from tourism.views import TouristArrivals, ConferencesHeld, TouristDepartures, TourismEarnings, \
    Hotel_Occupancy_By_Residences, Hotels_By_Zone, All_Visitor_To_Parks, All_Visitors_To_Museums, \
    All_Population_Proportion_That_Took_Trip
from trade_and_commerce.views import tradeAmount, tradeID, tradeTitle, editTradeAmountView, addTradeAmountView, \
    tradeAmountView, trade_and_commerce, addTradeAmount, editTradeAmount
from transport_and_communication.views import editTransportCommunication, addTransportCommunication, \
    editTransportCommunicationView, addTransportCommunicationView, viewTransportCommunication, \
    transport_and_communication, TransportCommunication, telephoneCoverage, postalCoverage
from vital_statistics.views import topTenDeathCauses, deathCauses, expectedBirthsDeaths, sexBirthsDeaths, \
    topTenDeathCausesView, expectedBirthsDeathsView, sexBirthsDeathsView, vital_statistics, editSexBirthsDeathsView, \
    addSexBirthsDeathsView, editSexBirthsDeaths, addSexBirthsDeaths, editExpectedBirthsDeathsView, \
    addExpectedBirthsDeathsView, editExpectedBirthsDeaths, addExpectedBirthsDeaths, editTopTenDeathCausesView, \
    addTopTenDeathCausesView, editTopTenDeathCauses, addTopTenDeathCauses, populationSelectedAgeGroupView, \
    addPopulationSelectedAgeGroupView, editPopulationSelectedAgeGroupView, viewPopulationSelectedAgeGroup, \
    populationSelectedAgeGroup, addPopulationSelectedAgeGroup, editPopulationSelectedAgeGroup, \
    populationSpecialAgeGroupView, addPopulationSpecialAgeGroupView, editPopulationSpecialAgeGroupView, \
    viewPopulationSpecialAgeGroup, populationSpecialAgeGroup, addPopulationSpecialAgeGroup, \
    editPopulationSpecialAgeGroup

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^counties/', views.CountiesList.as_view()),
    # url(r'^health/births$', health_birth_all),
    # url(r'^health/filter$', health_births),
    # url(r'^health/addbirths$', health_birth_add),
    # url(r'^health/updatebirths$', health_birth_update),
    # url(r'^health/loadupdatebirths$', health_birth_update_load),
    # url(r'^health/deletebirths$', health_birth_delete),
    # url(r'^health/deaths$', health_death_all),
    # url(r'^health/adddeaths', addDeaths),
    # url(r'^health/editdeaths', updateDeaths),
    url(r'^health/all_sectors', healthSectors),
    url(r'^health/all_deaths', Deaths),
    #url(r'^health/plusdeaths', plusDeaths),
    # url(r'^health/alterdeaths', alterDeaths),
    url(r'^health/all_diseases', allDiseases),
    #url(r'^health/add_diseases', addDisease),
    #url(r'^health/edit_diseases', editDisease),
    url(r'^health/all_facilities', allHealthFacilities),
    #url(r'^health/add_facility', addFacility),
    #url(r'^health/edit_facility', editFacility),
    url(r'^health/all_personnel', allPersonnel),
    #url(r'^health/add_personnel', addPersonnel),
    #url(r'^health/edit_personnel', editPersonnel),
    url(r'^health/all_nhif_members', allMembers),
    #url(r'^health/add_nhif_member', addMember),
    #url(r'^health/edit_nhif_member', editMember),
    url(r'^health/all_nhif_resources', allNhifResources),
    #url(r'^health/add_nhif_resource', addNhifResource),
    #url(r'^health/edit_nhif_resource', editNhifResource),
    url(r'^health/all_above_five', aboveFive),
    url(r'^health/add_above_five', addAboveFive),
    url(r'^health/edit_above_five', editAboveFive),
    url(r'^health/all_below_five', belowFive),
    url(r'^health/add_below_five', addBelowFive),
    url(r'^health/edit_below_five', editBelowFive),
    url(r'^health/all_disease_list', diseaseList),
    url(r'^health/all_immunization', immunizationRate),
    url(r'^health/add_immunization', addImmunization),
    url(r'^health/edit_immunization', editImmunization),
    url(r'^health/all_hospital_beds_and_cots', hospitalBedsCots),
    url(r'^health/add_hospital_beds_and_cots', addHospitalBedsCots),
    url(r'^health/edit_hospital_beds_and_cots', editHospitalBedsCots),
    url(r'^health/all_current_use_of_contraception_by_county', contraceptionUseCounty),
    url(r'^health/add_current_use_of_contraception_by_county', addContraceptionUseCounty),
    url(r'^health/edit_current_use_of_contraception_by_county', editContraceptionUseCounty),
    url(r'^health/all_distribution_of_outpatient_visits_by_type_of_healthcare_provider', distributionOutpatientProvider),
    url(r'^health/add_distribution_of_outpatient_visits_by_type_of_healthcare_provider', addDistributionOutpatientProvider),
    url(r'^health/edit_distribution_of_outpatient_visits_by_type_of_healthcare_provider', editDistributionOutpatientProvider),
    url(r'^health/all_health_insurance_coverage_by_counties_and_types', insuranceCoverage),
    url(r'^health/add_health_insurance_coverage_by_counties_and_types', addInsuranceCoverage),
    url(r'^health/edit_health_insurance_coverage_by_counties_and_types', editInsuranceCoverage),
    url(r'^health/all_maternal_care', maternalCare),
    url(r'^health/add_maternal_care', addMaternalCare),
    url(r'^health/edit_maternal_care', editMaternalCare),
    url(r'^health/all_nutritional_status_of_children', nutritionChildren),
    url(r'^health/add_nutritional_status_of_children', addNutritionChildren),
    url(r'^health/edit_nutritional_status_of_children', editNutritionChildren),
    url(r'^health/all_nutritional_status_of_women', nutritionWomen),
    url(r'^health/add_nutritional_status_of_women', addNutritionWomen),
    url(r'^health/edit_nutritional_status_of_women', editNutritionWomen),
    url(r'^health/all_registered_medical_laboratories_by_counties', registeredLabs),
    url(r'^health/add_registered_medical_laboratories_by_counties', addRegisteredLabs),
    url(r'^health/edit_registered_medical_laboratories_by_counties', editRegisteredLabs),
    url(r'^health/all_use_of_mosquito_nets_by_children', mosquitoNets),
    url(r'^health/add_use_of_mosquito_nets_by_children', addMosquitoNets),
    url(r'^health/edit_use_of_mosquito_nets_by_children', editMosquitoNets),
    url(r'^health/all_hiv_aids_awareness_and_testing', hivAwareness),
    url(r'^health/add_hiv_aids_awareness_and_testing', addHivAwareness),
    url(r'^health/edit_hiv_aids_awareness_and_testing', editHivAwareness),
    url(r'^health/all_registered_active_nhif_members_by_county', nhifActiveMembers),
    url(r'^health/add_registered_active_nhif_members_by_county', addNhifActiveMembers),
    url(r'^health/edit_registered_active_nhif_members_by_county', editNhifActiveMembers),
    url(r'^finance/all_county_revenue', allCountyRevenue),
    url(r'^finance/add_county_revenue', addCountyRevenue),
    url(r'^finance/edit_county_revenue', editCountyRevenue),
    url(r'^finance/all_county_expenditure', allCountyExpenditure),
    url(r'^finance/add_county_expenditure', addCountyExpenditure),
    url(r'^finance/edit_county_expenditure', editCountyExpenditure),
    url(r'^finance/all_economic_revenue', allEconomicRevenue),
    url(r'^finance/add_economic_revenue', addEconomicRevenue),
    url(r'^finance/edit_economic_revenue', editEconomicRevenue),
    url(r'^finance/all_debt_international', allDebtInternational),
    url(r'^finance/add_debt_international', addDebtInternational),
    url(r'^finance/edit_debt_international', editDebtInternational),
    url(r'^finance/all_debt_lending', allDebtLending),
    url(r'^finance/add_debt_lending', addDebtLending),
    url(r'^finance/edit_debt_lending', editDebtLending),
    url(r'^finance/all_excise_revenue', allExciseRevenue),
    url(r'^finance/add_excise_revenue', addExciseRevenue),
    url(r'^finance/edit_excise_revenue', editExciseRevenue),
    url(r'^finance/all_county_allocation', allCountyAllocation),
    url(r'^finance/add_county_allocation', addCountyAllocation),
    url(r'^finance/edit_county_allocation', editCountyAllocation),
    url(r'^finance/all_national_expenditure', allNationalExpenditure),
    url(r'^finance/add_national_expenditure', addNationalExpenditure),
    url(r'^finance/edit_national_expenditure', editNationalExpenditure),
    url(r'^finance/all_national_purpose', allNationalPurpose),
    url(r'^finance/add_national_purpose', addNationalPurpose),
    url(r'^finance/edit_national_purpose', editNationalPurpose),
    url(r'^finance/all_cdf_allocation', allCdfAllocation),
    url(r'^finance/add_cdf_allocation', addCdfAllocation),
    url(r'^finance/edit_cdf_allocation', editCdfAllocation),
    # url(r'^finance/all_banking_index', bankingIndex),
    # url(r'^finance/all_banking_institution', bankingInstitution),
    # url(r'^finance/add_banking_institution', addBankingInstitution),
    # url(r'^finance/edit_banking_institution', editBankingInstitution),
    url(r'^labour/all_sectors', allSectors),
    url(r'^labour/all_public_sector', publicSector),
    url(r'^labour/add_public_sector', addPublicSector),
    url(r'^labour/edit_public_sector', editPublicSector),
    url(r'^population/all_population_by_sex', populationSex),
    url(r'^population/all_population_by_selected_age', populationSelectedAge),
    url(r'^population/all_population_by_special_group', populationSpecialGroup),
    url(r'^education/all_diploma_degree', diplomaDegree),
    url(r'^education/add_diploma_degree', addDiplomaDegree),
    url(r'^education/edit_diploma_degree', editDiplomaDegree),
    # url(r'^education/all_enrollment_secondary_school', secondaryLevelSex),
    url(r'^education/all_national_trend_kcse', trendsKcse),
    url(r'^education/all_number_educational_institutions', numInstitutions),
    url(r'^education/all_student_enrollment_sex', studentEnrollment),
    url(r'^education/add_student_enrollment_sex', addStudentEnrollment),
    url(r'^education/edit_student_enrollment_sex', editStudentEnrollment),
    url(r'^education/all_student_enrollment_public_universities', studentEnrollmentPublic),
    url(r'^education/add_student_enrollment_public_universities', addStudentEnrollmentPublic),
    url(r'^education/edit_student_enrollment_public_universities', editStudentEnrollmentPublic),
    url(r'^education/all_total_secondary_school_enrollment', secSchoolEnrollment),
    url(r'^education/add_total_secondary_school_enrollment', addSchoolEnrollment),
    url(r'^education/edit_total_secondary_school_enrollment', editSchoolEnrollment),
    url(r'^education/all_adult_edu_centres_subcounty', adultEducationCentres),
    url(r'^education/add_adult_edu_centres_subcounty', addAdultEducationCentres),
    url(r'^education/edit_adult_edu_centres_subcounty', editAdultEducationCentres),
    url(r'^education/all_adult_education_enrollment', adultEducationEnrolment),
    url(r'^education/add_adult_education_enrollment', addAdultEducationEnrolment),
    url(r'^education/edit_adult_education_enrollment', editAdultEducationEnrolment),
    url(r'^education/all_adult_education_proficiency', adultEducationProficiency),
    url(r'^education/add_adult_education_proficiency', addAdultEducationProficiency),
    url(r'^education/edit_adult_education_proficiency', editAdultEducationProficiency),
    url(r'^education/all_ecde_centres_category_subcounty', ecdeCategorySubCounty),
    url(r'^education/add_ecde_centres_category_subcounty', addEcdeCategorySubCounty),
    url(r'^education/edit_ecde_centres_category_subcounty', editEcdeCategorySubCounty),
    url(r'^education/all_primary_enrollment_indicators', primaryEnrollmentIndicators),
    url(r'^education/add_primary_enrollment_indicators', addPrimaryEnrollmentIndicators),
    url(r'^education/edit_primary_enrollment_indicators', editPrimaryEnrollmentIndicators),
    url(r'^education/all_primary_enrollment_sex_county', primaryEnrollmentSexCounty),
    url(r'^education/add_primary_enrollment_sex_county', addPrimaryEnrollmentSexCounty),
    url(r'^education/edit_primary_enrollment_sex_county', editPrimaryEnrollmentSexCounty),
    url(r'^education/all_primary_category_subcounty', primaryCategorySubCounty),
    url(r'^education/add_primary_category_subcounty', addPrimaryCategorySubCounty),
    url(r'^education/edit_primary_category_subcounty', editPrimaryCategorySubCounty),
    url(r'^education/all_secondary_enrollment_indicators', secondaryEnrollmentIndicators),
    url(r'^education/add_secondary_enrollment_indicators', addSecondaryEnrollmentIndicators),
    url(r'^education/edit_secondary_enrollment_indicators', editSecondaryEnrollmentIndicators),
    url(r'^education/all_secondary_enrollment_class_sex_county', secondaryEnrollmentSexCounty),
    url(r'^education/add_secondary_enrollment_class_sex_county', addSecondaryEnrollmentSexCounty),
    url(r'^education/edit_secondary_enrollment_class_sex_county', editSecondaryEnrollmentSexCounty),
    url(r'^education/all_secondary_category_subcounty', secondaryCategorySubCounty),
    url(r'^education/all_student_enrollment_polytechnics', studentEnrollmentPolytechnic),
    url(r'^education/add_student_enrollment_polytechnics', addStudentEnrollmentPolytechnic),
    url(r'^education/edit_student_enrollment_polytechnics', editStudentEnrollmentPolytechnic),
    url(r'^education/all_teacher_training_colleges', teacherTrainingColleges),
    url(r'^education/add_teacher_training_colleges', addTeacherTrainingColleges),
    url(r'^education/edit_teacher_training_colleges', editTeacherTrainingColleges),
    url(r'^education/all_polytechnic_category_subcounty', polytechnicCategorySubcounty),
    url(r'^education/add_polytechnic_category_subcounty', addPolytechnicCategorySubcounty),
    url(r'^education/edit_polytechnic_category_subcounty', editPolytechnicCategorySubcounty),
    url(r'^education/all_edstat_ecde_enrollment_and_enrollment_rates_by_county', ecdeEnrollmentEdstat),
    url(r'^education/add_edstat_ecde_enrollment_and_enrollment_rates_by_county', addEcdeEnrollment),
    url(r'^education/edit_edstat_ecde_enrollment_and_enrollment_rates_by_county', editEcdeEnrollment),
    url(r'^education/all_edstat_primary_enrollment_and_enrollment_rates_by_county', primaryEnrollmentEdstat),
    url(r'^education/add_edstat_primary_enrollment_and_enrollment_rates_by_county', addPrimaryEnrollment),
    url(r'^education/edit_edstat_primary_enrollment_and_enrollment_rates_by_county', editPrimarynrollment),
    url(r'^education/all_edstat_secondary_enrollment_and_enrollment_rates_by_county', secondaryEnrollmentEdstat),
    url(r'^education/add_edstat_secondary_enrollment_and_enrollment_rates_by_county', addSecondaryEnrollment),
    url(r'^education/edit_edstat_secondary_enrollment_and_enrollment_rates_by_county', editSecondarynrollment),
    url(r'^education/all_edstat_kcpe_examination_candidature', kcpeCandidature),
    url(r'^education/add_edstat_kcpe_examination_candidature', addKcpeCandidature),
    url(r'^education/edit_edstat_kcpe_examination_candidature', editKcpeCandidature),
    url(r'^education/all_edstat_kcpe_examination_results_by_subject', kcpeResults),
    url(r'^education/add_edstat_kcpe_examination_results_by_subject', addKcpeResults),
    url(r'^education/edit_edstat_kcpe_examination_results_by_subject', editKcpeResults),
    url(r'^education/all_edstat_kcse_examination_results', kcseResults),
    url(r'^education/add_edstat_kcse_examination_results', addKcseResults),
    url(r'^education/edit_edstat_kcse_examination_results', editKcseResults),
    url(r'^agriculture/all_chemical_feeds', chemicalFeed),
    url(r'^agriculture/add_chemical_feeds', addChemicalFeed),
    url(r'^agriculture/edit_chemical_feeds', editChemicalFeed),
    url(r'^agriculture/all_cooperatives', cooperatives),
    url(r'^agriculture/add_cooperatives', addCooperatives),
    url(r'^agriculture/edit_cooperatives', editCooperatives),
    url(r'^agriculture/all_market_production', marketProduction),
    url(r'^agriculture/add_market_production', addMarketProduction),
    url(r'^agriculture/edit_market_production', editMarketProduction),
    url(r'^agriculture/all_irrigation_schemes', irrigationSchemes),
    url(r'^agriculture/add_irrigation_schemes', addIrrigationSchemes),
    url(r'^agriculture/edit_irrigation_schemes', editIrrigationSchemes),
    url(r'^agriculture/all_price_meat_milk', priceMeatMilk),
    url(r'^agriculture/add_price_meat_milk', addPriceMeatMilk),
    url(r'^agriculture/edit_price_meat_milk', editPriceMeatMilk),
    url(r'^agriculture/all_share_capital', shareCapital),
    url(r'^agriculture/add_share_capital', addShareCapital),
    url(r'^agriculture/edit_share_capital', editShareCapital),
    url(r'^agriculture/all_agricultural_inputs', agriculturalInputs),
    url(r'^agriculture/add_agricultural_inputs', addAgriculturalInputs),
    url(r'^agriculture/edit_agricultural_inputs', editAgriculturalInputs),
    url(r'^agriculture/all_land_potential', landPotential),
    url(r'^agriculture/add_land_potential', addLandPotential),
    url(r'^agriculture/edit_land_potential', editLandPotential),
    url(r'^agriculture/all_area_under_sugarcane_harvested_production_avg_yield', areaSugarcane),
    url(r'^agriculture/add_area_under_sugarcane_harvested_production_avg_yield', addAreaSugarcane),
    url(r'^agriculture/edit_area_under_sugarcane_harvested_production_avg_yield', editAreaSugarcane),
    url(r'^agriculture/all_categories_of_agricultural_land', agriculturalLand),
    url(r'^agriculture/add_categories_of_agricultural_land', addAgriculturalLand),
    url(r'^agriculture/edit_categories_of_agricultural_land', editAgriculturalLand),
    url(r'^agriculture/all_production_area_average_yield_coffee_type_of_grower', areaCoffee),
    url(r'^agriculture/add_production_area_average_yield_coffee_type_of_grower', addAreaCoffee),
    url(r'^agriculture/edit_production_area_average_yield_coffee_type_of_grower', editAreaCoffee),
    url(r'^agriculture/all_production_area_average_yield_tea_type_grower', areaTea),
    url(r'^agriculture/add_production_area_average_yield_tea_type_grower', addAreaTea),
    url(r'^agriculture/edit_production_area_average_yield_tea_type_grower', editAreaTea),
    url(r'^agriculture/all_production_of_livestock_and_dairy_products', livestockProducts),
    url(r'^agriculture/add_production_of_livestock_and_dairy_products', addLivestockProducts),
    url(r'^agriculture/edit_production_of_livestock_and_dairy_products', editLivestockProducts),
    url(r'^administrative/all_units', allUnit),
    url(r'^administrative/add_units', addAdministrative),
    url(r'^administrative/edit_units', editAdministrative),
    url(r'^political/all_units', allUnits),
    url(r'^political/add_units', addPolitical),
    url(r'^political/edit_units', editPolitical),
    url(r'^energy/all_pump_prices_fuel', pumpPricesFuel),
    url(r'^population/all_population_projections_by_selected_age_group', populationSelectedAgeGroup),
    url(r'^population/add_population_projections_by_selected_age_group', addPopulationSelectedAgeGroup),
    url(r'^population/edit_population_projections_by_selected_age_group', editPopulationSelectedAgeGroup),
    url(r'^population/all_population_projections_by_special_age_groups', populationSpecialAgeGroup),
    url(r'^population/add_population_projections_by_special_age_groups', addPopulationSpecialAgeGroup),
    url(r'^population/edit_population_projections_by_special_age_groups', editPopulationSpecialAgeGroup),
    url(r'^vital/all_births_deaths_by_sex', sexBirthsDeaths),
    url(r'^vital/add_births_deaths_by_sex', addSexBirthsDeaths),
    url(r'^vital/edit_births_deaths_by_sex', editSexBirthsDeaths),
    url(r'^vital/all_expected_births_deaths', expectedBirthsDeaths),
    url(r'^vital/add_expected_births_deaths', addExpectedBirthsDeaths),
    url(r'^vital/edit_expected_births_deaths', editExpectedBirthsDeaths),
    url(r'^vital/all_death_causes', deathCauses),
    url(r'^vital/all_top_ten_death_causes', topTenDeathCauses),
    url(r'^vital/add_top_ten_death_causes', addTopTenDeathCauses),
    url(r'^vital/edit_top_ten_death_causes', editTopTenDeathCauses),
    url(r'^building_and_construction/all_industry_id', idIndustry),
    url(r'^building_and_construction/all_industry_amount', amountBuilding),
    url(r'^building_and_construction/add_industry_amount', addAmountBuilding),
    url(r'^building_and_construction/edit_industry_amount', editAmountBuilding),
    url(r'^building_and_construction/all_quarterly_civil_engineering_cost_index', quarterlyCivil),
    url(r'^building_and_construction/add_quarterly_civil_engineering_cost_index', addQuarterlyCivil),
    url(r'^building_and_construction/edit_quarterly_civil_engineering_cost_index', editQuarterlyCivil),
    url(r'^building_and_construction/all_quarterly_non_residential_build_cost', quarterlyNonResidential),
    url(r'^building_and_construction/add_quarterly_non_residential_build_cost', addQuarterlyNonResidential),
    url(r'^building_and_construction/edit_quarterly_non_residential_build_cost', editQuarterlyNonResidential),
    url(r'^building_and_construction/all_quarterly_overal_construction_cost', quarterlyOverall),
    url(r'^building_and_construction/add_quarterly_overal_construction_cost', addQuarterlyOverall),
    url(r'^building_and_construction/edit_quarterly_overal_construction_cost', editQuarterlyOverall),
    url(r'^building_and_construction/all_quarterly_residential_bulding_cost', quarterlyResidential),
    url(r'^building_and_construction/add_quarterly_residential_bulding_cost', addQuarterlyResidential),
    url(r'^building_and_construction/edit_quarterly_residential_bulding_cost', editQuarterlyResidential),
    url(r'^trade_and_commerce/all_trade_title', tradeTitle),
    url(r'^trade_and_commerce/all_trade_id', tradeID),
    url(r'^trade_and_commerce/all_trade_amount', tradeAmount),
    url(r'^trade_and_commerce/add_trade_amount', addTradeAmount),
    url(r'^trade_and_commerce/edit_trade_amount', editTradeAmount),
    url(r'^governance/all_crimes_reported_to_police_by_command_stations', crimesReported),
    url(r'^governance/add_crimes_reported_to_police_by_command_stations', addCrimesReported),
    url(r'^governance/edit_crimes_reported_to_police_by_command_stations', editCrimesReported),
    url(r'^governance/all_offence_by_sex_and_command_stations', offenceSex),
    url(r'^governance/add_offence_by_sex_and_command_stations', addOffenceSex),
    url(r'^governance/edit_offence_by_sex_and_command_stations', editOffenceSex),
    url(r'^governance/all_registered_voters_by_county_and_by_sex', registeredVotersCounty),
    url(r'^governance/add_registered_voters_by_county_and_by_sex', addRegisteredVotersCounty),
    url(r'^governance/edit_registered_voters_by_county_and_by_sex', editRegisteredVotersCounty),
    url(r'^governance/all_casesforwarded_and_actiontaken', casesForwardedActed),
    url(r'^governance/all_cases_handled_by_various_courts', casesVariousCourts),
    url(r'^governance/all_cases_handled_by_ethics_commision', casesEACC),
    url(r'^governance/all_convicted_prisoners_by_type_of_offence_and_sex', prisonersOffencesex),
    url(r'^governance/all_environmental_crimes_reported_to_nema', environmentalCrimes),
    url(r'^governance/all_convicted_prison_population_by_age_and_sex', convictedPrisonAgeSex),
    url(r'^governance/all_number_of_police_prisons_and_probation_officers', policePrisonsProbation),
    url(r'^governance/all_offences_committed_against_morality', offenceMorality),
    url(r'^governance/all_persons_reported_to_have_committed_homicide_by_sex', homicideSex),
    url(r'^governance/all_persons_reported_to_have_committed_robbery_and_theft', robberyTheft),
    url(r'^governance/all_daily_average_population_of_prisoners_by_sex', dailyAvearge),
    url(r'^governance/all_firearms_and_ammunition_recovered_or_surrendered', fireArms),
    url(r'^governance/all_identity_cards_made_processed_and_collected', idCards),
    url(r'^governance/all_magistrates_judges_and_practicing_lawyers', courtStaff),
    url(r'^governance/all_murder_cases_and_convictions_obtained_by_high_court', murderCases),
    url(r'^governance/all_number_of_refugees_by_age_and_sex', refugeeAgeSex),
    url(r'^governance/all_offenders_serving', offendersServing),
    url(r'^governance/all_passports_work_permits_and_foreigners_registered', passportPermits),
    url(r'^governance/all_persons_reported_to_have_committed_offences_related_to_drugs', personsReported),
    url(r'^governance/all_prison_population_by_sentence_duration_and_sex', prisonPopulation),
    url(r'^governance/all_public_assets_traced_recovered_and_loss_averted', publicAssets),
    url(r'^land_and_climate/all_surface_area_by_category', surfaceArea),
    url(r'^land_and_climate/add_surface_area_by_category', addSurfaceArea),
    url(r'^land_and_climate/edit_surface_area_by_category', editSurfaceArea),
    url(r'^land_and_climate/all_temperature', Temperatures),
    url(r'^land_and_climate/add_temperature', addTemperature),
    url(r'^land_and_climate/edit_temperature', editTemperature),
    url(r'^land_and_climate/all_rainfall', rain_fall),
    url(r'^land_and_climate/add_rainfall', addRainfall),
    url(r'^land_and_climate/edit_rainfall', editRainfall),
    url(r'^land_and_climate/all_topography_altitude', topograhyAltitude),
    url(r'^land_and_climate/add_topography_altitude', addTopograhyAltitude),
    url(r'^land_and_climate/edit_topography_altitude', editTopograhyAltitude),
    url(r'^transport_and_communication/all_road_coverage_by_type_and_distance', TransportCommunication),
    url(r'^transport_and_communication/add_road_coverage_by_type_and_distance', addTransportCommunication),
    url(r'^transport_and_communication/edit_road_coverage_by_type_and_distance', editTransportCommunication),
    url(r'^transport_and_communication/all_coverage_of_telephone_services', telephoneCoverage),
    url(r'^transport_and_communication/all_coverage_of_postal_services', postalCoverage),
    url(r'^manufacturing/all_per_change_in_quantum_indices_of_man_production', percentageChange),
    url(r'^manufacturing/add_per_change_in_quantum_indices_of_man_production', addPercentageChange),
    url(r'^manufacturing/edit_per_change_in_quantum_indices_of_man_production', editPercentageChange),
    url(r'^manufacturing/all_quantum_indices_of_manufacturing_production', quantumIndices),
    url(r'^manufacturing/add_quantum_indices_of_manufacturing_production', addQuantumIndices),
    url(r'^manufacturing/edit_quantum_indices_of_manufacturing_production', editQuantumIndices),
    url(r'^energy/all_average_retail_prices_of_selected_petroleum_products', averagePrices),
    url(r'^energy/add_average_retail_prices_of_selected_petroleum_products', addAveragePrices),
    url(r'^energy/edit_average_retail_prices_of_selected_petroleum_products', editAveragePrices),
    url(r'^energy/all_net_domestic_sale_of_petroleum_fuels_by_consumer_category', domesticSale),
    url(r'^energy/add_net_domestic_sale_of_petroleum_fuels_by_consumer_category', addDomesticSale),
    url(r'^energy/edit_net_domestic_sale_of_petroleum_fuels_by_consumer_category', editDomesticSale),
    url(r'^energy/all_value_and_quantity_of_imports_exports', valueQuantity),
    url(r'^energy/add_value_and_quantity_of_imports_exports', addValueQuantity),
    url(r'^energy/edit_value_and_quantity_of_imports_exports', editValueQuantity),
    url(r'^energy/all_petroleum_supply_and_demand', petroleumSupply),
    url(r'^energy/add_petroleum_supply_and_demand', addPetroleumSupply),
    url(r'^energy/edit_petroleum_supply_and_demand', editPetroleumSupply),
    url(r'^energy/all_installed_and_effective_capacity_of_electricity', installedCapacity),
    url(r'^energy/add_installed_and_effective_capacity_of_electricity', addInstalledCapacity),
    url(r'^energy/edit_installed_and_effective_capacity_of_electricity', editInstalledCapacity),
    url(r'^energy/all_generation_and_imports_of_electricity', generalImports),
    url(r'^energy/add_generation_and_imports_of_electricity', addGeneralImports),
    url(r'^energy/edit_generation_and_imports_of_electricity', editGeneralImports),
    url(r'^energy/all_electricity_demand_and_supply', electricityDemand),
    url(r'^energy/add_electricity_demand_and_supply', addElectricityDemand),
    url(r'^energy/edit_electricity_demand_and_supply', editElectricityDemand),
    url(r'^cpi/all_annual_avg_retail_prices_of_certain_consumer_goods_in_kenya', averageRetail),
    url(r'^cpi/add_annual_avg_retail_prices_of_certain_consumer_goods_in_kenya', addAverageRetail),
    url(r'^cpi/edit_annual_avg_retail_prices_of_certain_consumer_goods_in_kenya', editAverageRetail),
    url(r'^cpi/all_consumer_price_index', consumerPrice),
    url(r'^cpi/add_consumer_price_index', addConsumerPrice),
    url(r'^cpi/edit_consumer_price_index', editConsumerPrice),
    url(r'^cpi/all_elementary_aggregates_weights_in_the_cpi_baskets', elementaryWeights),
    url(r'^cpi/add_elementary_aggregates_weights_in_the_cpi_baskets', addElementaryWeights),
    url(r'^cpi/edit_elementary_aggregates_weights_in_the_cpi_baskets', editElementaryWeights),
    url(r'^cpi/all_group_weights_for_kenya_cpi_febuary_base_2009', groupWeights),
    url(r'^cpi/add_group_weights_for_kenya_cpi_febuary_base_2009', addGroupWeights),
    url(r'^cpi/edit_group_weights_for_kenya_cpi_febuary_base_2009', editGroupWeights),
    url(r'^cpi/all_group_weights_for_kenya_cpi_october_base_1997', groupWeightsKenya),
    url(r'^cpi/add_group_weights_for_kenya_cpi_october_base_1997', addGroupWeightsKenya),
    url(r'^cpi/edit_group_weights_for_kenya_cpi_october_base_1997', editGroupWeightsKenya),
    url(r'^money_and_banking/all_commercial_banks_bills_loans_advances', commercialBanks),
    url(r'^money_and_banking/add_commercial_banks_bills_loans_advances', addCommercialBanks),
    url(r'^money_and_banking/edit_commercial_banks_bills_loans_advances', editCommercialBanks),
    url(r'^money_and_banking/all_inflation_rates', inflationRates),
    url(r'^money_and_banking/add_inflation_rates', addInflationRates),
    url(r'^money_and_banking/edit_inflation_rates', editInflationRates),
    url(r'^money_and_banking/all_interest_rates', interestRates),
    url(r'^money_and_banking/add_interest_rates', addInterestRates),
    url(r'^money_and_banking/edit_interest_rates', editInterestRates),
    url(r'^money_and_banking/all_monetary_indicators_broad_money_supply', monetaryIndicators),
    url(r'^money_and_banking/add_monetary_indicators_broad_money_supply', addMonetaryIndicators),
    url(r'^money_and_banking/edit_monetary_indicators_broad_money_supply', editMonetaryIndicators),
    url(r'^money_and_banking/all_monetary_indicators_domestic_credit', monetaryIndicatorsDomestic),
    url(r'^money_and_banking/add_monetary_indicators_domestic_credit', addMonetaryIndicatorsDomestic),
    url(r'^money_and_banking/edit_monetary_indicators_domestic_credit', editMonetaryIndicatorsDomestic),
    url(r'^money_and_banking/all_nairobi_securities_exchange', securitiesExchange),
    url(r'^money_and_banking/add_nairobi_securities_exchange', addSecuritiesExchange),
    url(r'^money_and_banking/edit_nairobi_securities_exchange', editSecuritiesExchange),
    url(r'^money_and_banking/all_banking_institution', bankingInstitution),
    url(r'^money_and_banking/add_banking_institution', addBankingInstitution),
    url(r'^money_and_banking/edit_banking_institution', editBankingInstitution),
    url(r'^tourism/all_arrivals', TouristArrivals),
    url(r'^tourism/all_conferences', ConferencesHeld),
    url(r'^tourism/all_departures', TouristDepartures),
    url(r'^tourism/all_earnings', TourismEarnings),
    url(r'^tourism/all_hotel_occupancy', Hotel_Occupancy_By_Residences),
    url(r'^tourism/all_hotels_by_zone', Hotels_By_Zone),
    url(r'^tourism/all_visitors_to_parks', All_Visitor_To_Parks),
    url(r'^tourism/all_visitors_to_museums', All_Visitors_To_Museums),
    url(r'^tourism/All_Population_Proportion_That_Took_Trip', All_Population_Proportion_That_Took_Trip),
    url(r'^home', index),
    url(r'^health$', health),
    url(r'^immunization_history$', allImmunizationRate),
    url(r'^immunization_add$', addImmunizationView),
    url(r'^immunization_edit$', editImmunizationView),
    url(r'^morbidity_below_history$', morbidityBelow),
    url(r'^morbidity_below_add$', addMorbidityView),
    url(r'^morbidity_below_edit$', editMorbidityView),
    url(r'^morbidity_above_history$', morbidityAbove),
    url(r'^morbidity_above_add$', addMorbidityAboveView),
    url(r'^morbidity_above_edit$', editMorbidityAboveView),
    url(r'^facility_ownership$', healthFacility),
    url(r'^facility_ownership_edit$', editHealthOwnershipView),
    url(r'^facility_ownership_add$', addHealthOwnershipView),
    url(r'^facilities$', healthFacilityView),
    url(r'^registered_medical_personnel$', registeredMedicalPersonnelView),
    url(r'^hospital_beds_and_cots$', hospitalBedsCotsView),
    url(r'^hospital_beds_and_cots_add$', addHospitalBedsCotsView),
    url(r'^hospital_beds_and_cots_edit$', editHospitalBedsCotsView),
    url(r'^current_use_of_contraception_by_county$', contraceptionUseCountyView),
    url(r'^current_use_of_contraception_by_county_add$', addContraceptionUseCountyView),
    url(r'^current_use_of_contraception_by_county_edit$', editContraceptionUseCountyView),
    url(r'^distribution_of_outpatient_visits_by_type_of_healthcare_provider$', distributionOutpatientProviderView),
    url(r'^distribution_of_outpatient_visits_by_type_of_healthcare_provider_add$', addDistributionOutpatientProviderView),
    url(r'^distribution_of_outpatient_visits_by_type_of_healthcare_provider_edit$', editDistributionOutpatientProviderView),
    url(r'^health_insurance_coverage_by_counties_and_types$', insuranceCoverageView),
    url(r'^health_insurance_coverage_by_counties_and_types_add$', addInsuranceCoverageView),
    url(r'^health_insurance_coverage_by_counties_and_types_edit$', editInsuranceCoverageView),
    url(r'^maternal_care$', maternalCareView),
    url(r'^maternal_care_add$', addMaternalCareView),
    url(r'^maternal_care_edit$', editMaternalCareView),
    url(r'^nutritional_status_of_children$', nutritionChildrenView),
    url(r'^nutritional_status_of_children_add$', addNutritionChildrenView),
    url(r'^nutritional_status_of_children_edit$', editNutritionChildrenView),
    url(r'^nutritional_status_of_women$', nutritionWomenView),
    url(r'^nutritional_status_of_women_add$', addNutritionWomenView),
    url(r'^nutritional_status_of_women_edit$', editNutritionWomenView),
    url(r'^registered_medical_laboratories_by_counties$', registeredLabsView),
    url(r'^registered_medical_laboratories_by_counties_add$', addRegisteredLabsView),
    url(r'^registered_medical_laboratories_by_counties_edit$', editRegisteredLabsView),
    url(r'^use_of_mosquito_nets_by_children$', mosquitoNetsView),
    url(r'^use_of_mosquito_nets_by_children_add$', addMosquitoNetsView),
    url(r'^use_of_mosquito_nets_by_children_edit$', editMosquitoNetsView),
    url(r'^hiv_aids_awareness_and_testing$', hivAwarenessView),
    url(r'^hiv_aids_awareness_and_testing_add$', addHivAwarenessView),
    url(r'^hiv_aids_awareness_and_testing_edit$', editHivAwarenessView),
    url(r'^registered_active_nhif_members_by_county$', nhifActiveMembersView),
    url(r'^registered_active_nhif_members_by_county_add$', addNhifActiveMembersView),
    url(r'^registered_active_nhif_members_by_county_edit$', editNhifActiveMembersView),
    url(r'^nhif_resources$', allNhifResourcesView),
    url(r'^nhif_members$', allMembersView),

    url(r'^education$', education),
    url(r'^total_secondary_school_enrollment_by_year_data$', viewSecSchoolEnrollment),
    url(r'^total_secondary_school_enrollment_by_year_data_add$', addSecSchoolEnrollment),
    url(r'^total_secondary_school_enrollment_by_year_data_edit$', editSecSchoolEnrollment),
    url(r'^primary_schools_by_category_and_subcounty$', primaryCategorySubCountyView),
    url(r'^primary_schools_by_category_and_subcounty_add$', addCategorySubCountyView),
    url(r'^primary_schools_by_category_and_subcounty_edit$', editCategorySubCountyView),
    url(r'^secondary_enrolment_and_access_indicators$', secondaryEnrollmentIndicatorsView),
    url(r'^secondary_enrolment_and_access_indicators_add$', addSecondaryEnrollmentIndicatorsView),
    url(r'^secondary_enrolment_and_access_indicators_edit$', editSecondaryEnrollmentIndicatorsView),
    url(r'^primary_enrollment_class_sex_and_subcounty$', primaryEnrollmentSexCountyView),
    url(r'^primary_enrollment_class_sex_and_subcounty_add$', addPrimaryEnrollmentSexCountyView),
    url(r'^primary_enrollment_class_sex_and_subcounty_edit$', editPrimaryEnrollmentSexCountyView),
    url(r'^primary_enrollment_class_sex_and_subcounty_view$', morePrimaryEnrollmentSexCounty),
    url(r'^student_enrolment_in_youth_polytechnics$', studentEnrollmentPolytechnicView),
    url(r'^student_enrolment_in_youth_polytechnics_add$', addStudentEnrollmentPolytechnicView),
    url(r'^student_enrolment_in_youth_polytechnics_edit$', editStudentEnrollmentPolytechnicView),
    url(r'^youth_polytechnics_category_and_subcounty$', polytechnicCategorySubcountyView),
    url(r'^youth_polytechnics_category_and_subcounty_add$', addPolytechnicCategorySubcountyView),
    url(r'^youth_polytechnics_category_and_subcounty_edit$', editPolytechnicCategorySubcountyView),
    url(r'^teacher_training_colleges$', teacherTrainingCollegesView),
    url(r'^teacher_training_colleges_add$', addTeacherTrainingCollegesView),
    url(r'^teacher_training_colleges_edit$', editTeacherTrainingCollegesView),
    url(r'^ecde_centres_by_category_and_subcounty$', ecdeCategorySubCountyView),
    url(r'^ecde_centres_by_category_and_subcounty_add$', addEcdeCategorySubCountyView),
    url(r'^ecde_centres_by_category_and_subcounty_edit$', editEcdeCategorySubCountyView),
    url(r'^primary_enrolment_and_access_indicators$', primaryEnrollmentIndicatorsView),
    url(r'^primary_enrolment_and_access_indicators_add$', addPrimaryEnrollmentIndicatorsView),
    url(r'^primary_enrolment_and_access_indicators_edit$', editPrimaryEnrollmentIndicatorsView),
    url(r'^adult_education_centres_by_subcounty$', adultEducationCentresView),
    url(r'^adult_education_centres_by_subcounty_add$', addAdultEducationCentresView),
    url(r'^adult_education_centres_by_subcounty_edit$', editAdultEducationCentresView),
    url(r'^adult_education_enrolment_by_sex_and_subcounty$', adultEducationEnrolmentView),
    url(r'^adult_education_enrolment_by_sex_and_subcounty_add$', addAdultEducationEnrolmentView),
    url(r'^adult_education_enrolment_by_sex_and_subcounty_edit$', editAdultEducationEnrolmentView),
    url(r'^adult_education_proficiency_test_results$', adultEducationProficiencyView),
    url(r'^adult_education_proficiency_test_results_add$', addAdultEducationProficiencyView),
    url(r'^adult_education_proficiency_test_results_edit$', editAdultEducationProficiencyView),
    url(r'^secondary_enrollment_class_sex_subcounty$', secondaryEnrollmentSexCountyView),
    url(r'^secondary_enrollment_class_sex_subcounty_add$', addSecondaryEnrollmentSexCountyView),
    url(r'^secondary_enrollment_class_sex_subcounty_edit$', editSecondaryEnrollmentSexCountyView),
    url(r'^approved_degree_diploma_programs$', diplomaDegreeView),
    url(r'^approved_degree_diploma_programs_add$', addDiplomaDegreeView),
    url(r'^approved_degree_diploma_programs_edit$', editDiplomaDegreeView),
    url(r'^student_enrollment_public_universities$', studentEnrollmentPublicView),
    url(r'^student_enrollment_public_universities_add$', addStudentEnrollmentPublicView),
    url(r'^student_enrollment_public_universities_edit$', editStudentEnrollmentPublicView),
    url(r'^student_enrollment_sex_technical_institutions$', studentEnrollmentView),
    url(r'^student_enrollment_sex_technical_institutions_add$', addStudentEnrollmentView),
    url(r'^student_enrollment_sex_technical_institutions_edit$', editStudentEnrollmentView),
    url(r'^edstat_ecde_enrollment_and_enrollment_rates_by_county$', ecdeEnrollmentView),
    url(r'^edstat_ecde_enrollment_and_enrollment_rates_by_county_add$', addEcdeEnrollmentView),
    url(r'^edstat_ecde_enrollment_and_enrollment_rates_by_county_edit$', editEcdeEnrollmentView),
    url(r'^edstat_primary_enrollment_and_enrollment_rates_by_county$', primaryEnrollmentView),
    url(r'^edstat_primary_enrollment_and_enrollment_rates_by_county_add$', addPrimaryEnrollmentView),
    url(r'^edstat_primary_enrollment_and_enrollment_rates_by_county_edit$', editPrimaryEnrollmentView),
    url(r'^edstat_secondary_enrollment_and_enrollment_rates_by_county$', secondaryEnrollmentView),
    url(r'^edstat_secondary_enrollment_and_enrollment_rates_by_county_add$', addSecondaryEnrollmentView),
    url(r'^edstat_secondary_enrollment_and_enrollment_rates_by_county_edit$', editSecondaryEnrollmentView),
    url(r'^edstat_kcpe_examination_candidature$', kcpeCandidatureView),
    url(r'^edstat_kcpe_examination_candidature_add$', addKcpeCandidatureView),
    url(r'^edstat_kcpe_examination_candidature_edit$', editKcpeCandidatureView),
    url(r'^edstat_kcpe_examination_results_by_subject$', kcpeResultsView),
    url(r'^edstat_kcpe_examination_results_by_subject_add$', addKcpeResultsView),
    url(r'^edstat_kcpe_examination_results_by_subject_edit$', editKcpeResultsView),
    url(r'^edstat_kcse_examination_results$', kcseResults),
    url(r'^edstat_kcse_examination_results_add$', addKcseResultsView),
    url(r'^edstat_kcse_examination_results_edit$', editKcseResultsView),


    url(r'^finance$', finance),
    url(r'^county_revenue_history$', viewCountyRevenue),
    url(r'^county_revenue_add$', addCountyRevenueView),
    url(r'^county_revenue_edit$', editCountyRevenueView),
    url(r'^county_budget_allocation$', viewCountyAllocation),
    url(r'^county_budget_allocation_add$', addCountyAllocationView),
    url(r'^county_budget_allocation_edit$', editCountyAllocationView),
    url(r'^cdf_allocation$', viewCdfAllocation),
    url(r'^cdf_allocation_add$', addCdfAllocationView),
    url(r'^cdf_allocation_edit$', editCdfAllocationView),
    # url(r'^money_and_banking$', viewBankingInstitution),
    # url(r'^money_and_banking_add$', addBankingInstitutionView),
    # url(r'^money_and_banking_edit$', editBankingInstitutionView),
    url(r'^county_expenditure$', allCountyExpenditureView),
    url(r'^county_expenditure_add$', addCountyExpenditureView),
    url(r'^county_expenditure_edit$', editCountyExpenditureView),
    url(r'^county_expenditure_view$', viewExpenditure),
    url(r'^excise_revenue_commodity$', allExciseRevenueView),
    url(r'^excise_revenue_commodity_add$', addExciseRevenueView),
    url(r'^excise_revenue_commodity_edit$', editExciseRevenueView),
    url(r'^outstanding_debt_lending_country$', allDebtLendingView),
    url(r'^outstanding_debt_lending_country_add$', addDebtLendingView),
    url(r'^outstanding_debt_lending_country_edit$', editDebtLendingView),
    url(r'^outstanding_debt_international_organization$', allDebtInternationalView),
    url(r'^outstanding_debt_international_organization_add$', addDebtInternationalView),
    url(r'^outstanding_debt_international_organization_edit$', editDebtInternationalView),
    url(r'^economic_classification_revenue$', allEconomicRevenueView),
    url(r'^economic_classification_revenue_add$', addEconomicRevenueView),
    url(r'^economic_classification_revenue_edit$', editEconomicRevenueView),
    url(r'^economic_classification_revenue_view$', viewEconomicRevenue),
    url(r'^national_government_expenditure_purpose$', allNationalPurposeView),
    url(r'^national_government_expenditure_purpose_add$', addNationalPurposeView),
    url(r'^national_government_expenditure_purpose_edit$', editNationalPurposeView),
    url(r'^national_government_expenditure_purpose_view$', viewNationalPurpose),
    url(r'^national_government_expenditure$', allNationalExpenditureView),
    url(r'^national_government_expenditure_add$', addNationalExpenditureView),
    url(r'^national_government_expenditure_edit$', editNationalExpenditureView),
    url(r'^national_government_expenditure_view$', viewNationalExpenditure),

    url(r'^agriculture$', agriculture),
    url(r'^price_to_producers_for_meat_milk$', viewPriceMeatMilk),
    url(r'^price_to_producers_for_meat_milk_add$', addPriceMeatMilkView),
    url(r'^price_to_producers_for_meat_milk_edit$', editPriceMeatMilkView),
    url(r'^land_potential$', viewLandPotential),
    url(r'^land_potential_add$', addLandPotentialView),
    url(r'^land_potential_edit$', editLandPotentialView),
    url(r'^chemical_med_feed_input$', chemicalFeedView),
    url(r'^chemical_med_feed_input_add$', addChemicalFeedView),
    url(r'^chemical_med_feed_input_edit$', editChemicalFeedView),
    url(r'^chemical_med_feed_input_view$', viewChemFeed),
    url(r'^cooperatives$', cooperativesView),
    url(r'^cooperatives_add$', addCooperativesView),
    url(r'^cooperatives_edit$', editCooperativesView),
    url(r'^cooperatives_view$', viewCooperatives),
    url(r'^gross_market_production$', marketProductionView),
    url(r'^gross_market_production_add$', addMarketProductionView),
    url(r'^gross_market_production_edit$', editMarketProductionView),
    url(r'^gross_market_production_view$', viewMarketProduction),
    url(r'^irrigation_schemes$', irrigationSchemesView),
    url(r'^irrigation_schemes_add$', addIrrigationSchemesView),
    url(r'^irrigation_schemes_edit$', editIrrigationSchemesView),
    url(r'^irrigation_schemes_view$', viewIrrigationSchemes),
    url(r'^total_share_capital$', shareCapitalView),
    url(r'^total_share_capital_add$', addShareCapitalView),
    url(r'^total_share_capital_edit$', editShareCapitalView),
    url(r'^total_share_capital_view$', viewShareCapital),
    url(r'^value_of_agricultural_inputs$', agriculturalInputsView),
    url(r'^value_of_agricultural_inputs_add$', addAgriculturalInputsView),
    url(r'^value_of_agricultural_inputs_edit$', editAgriculturalInputsView),
    url(r'^value_of_agricultural_inputs_view$', viewAgriculturalInputs),
    url(r'^area_under_sugarcane_harvested_production_avg_yield$', viewAreaSugarcane),
    url(r'^area_under_sugarcane_harvested_production_avg_yield_add$', addAreaSugarcaneView),
    url(r'^area_under_sugarcane_harvested_production_avg_yield_edit$', editAreaSugarcaneView),
    url(r'^categories_of_agricultural_land$', viewAgriculturalLand),
    url(r'^categories_of_agricultural_land_add$', addAgriculturalLandView),
    url(r'^categories_of_agricultural_land_edit$', editAgriculturalLandView),
    url(r'^production_area_average_yield_coffee_type_of_grower$', areaCoffeeView),
    url(r'^production_area_average_yield_coffee_type_of_grower_add$', addAreaCoffeeView),
    url(r'^production_area_average_yield_coffee_type_of_grower_edit$', editAreaCoffeeView),
    url(r'^production_area_average_yield_tea_type_grower$', areaTeaView),
    url(r'^production_area_average_yield_tea_type_grower_add$', addAreaTeaView),
    url(r'^production_area_average_yield_tea_type_grower_edit$', editAreaTeaView),
    url(r'^production_of_livestock_and_dairy_products$', livestockProductsView),
    url(r'^production_of_livestock_and_dairy_products_add$', addLivestockProductsView),
    url(r'^production_of_livestock_and_dairy_products_edit$', editLivestockProductsView),

    url(r'^labour$', labour),
    url(r'^labour_employment_public_sector$', allPublicSectorView),
    url(r'^labour_employment_public_sector_add$', addPublicSectorView),
    url(r'^labour_employment_public_sector_edit$', editPublicSectorView),


    url(r'^administrative$', administrative),
    url(r'^administrative_unit$', allUnitView),
    url(r'^administrative_unit_add$', addUnitView),
    url(r'^administrative_unit_edit$', editUniView),

    url(r'^political$', political),
    url(r'^political_unit$', allUnitsView),
    url(r'^political_unit_add$', addUnitsView),
    url(r'^political_unit_edit$', editUnitsView),

    url(r'^trade_and_commerce$', trade_and_commerce),
    url(r'^trade_and_commerce_amount$', tradeAmountView),
    url(r'^trade_and_commerce_amount_add$', addTradeAmountView),
    url(r'^trade_and_commerce_amount_edit$', editTradeAmountView),

    url(r'^governance$', governance),
    url(r'^crimes_reported_to_police_by_command_stations$', crimesReportedView),
    url(r'^crimes_reported_to_police_by_command_stations_add$', addCrimesReportedView),
    url(r'^crimes_reported_to_police_by_command_stations_edit$', editCrimesReportedView),
    url(r'^offence_by_sex_and_command_stations$', offenceSexView),
    url(r'^offence_by_sex_and_command_stations_add$', addOffenceSexView),
    url(r'^offence_by_sex_and_command_stations_edit$', editOffenceSexView),
    url(r'^registered_voters_by_county_and_by_sex$', registeredVotersCountyView),
    url(r'^registered_voters_by_county_and_by_sex_add$', addRegisteredVotersCountyView),
    url(r'^registered_voters_by_county_and_by_sex_edit$', editRegisteredVotersCountyView),

    url(r'^vital_statistics$', vital_statistics),
    url(r'^births_and_deaths_by_sex$', sexBirthsDeathsView),
    url(r'^births_and_deaths_by_sex_add$', addSexBirthsDeathsView),
    url(r'^births_and_deaths_by_sex_edit$', editSexBirthsDeathsView),
    url(r'^expected_and_registered_births_and_deaths$', expectedBirthsDeathsView),
    url(r'^expected_and_registered_births_and_deaths_add$', addExpectedBirthsDeathsView),
    url(r'^expected_and_registered_births_and_deaths_edit$', editExpectedBirthsDeathsView),
    url(r'^top_ten_death_causes_2014$', topTenDeathCausesView),
    url(r'^top_ten_death_causes_2014_add$', addTopTenDeathCausesView),
    url(r'^top_ten_death_causes_2014_edit$', editTopTenDeathCausesView),
    url(r'^cases_handled_by_various_courts$', casesVariousCourtsView),
    url(r'^convicted_prisoners_by_type_of_offence_and_sex$', prisonersOffencesexView),
    url(r'^environmental_crimes_reported_to_nema$', environmentalCrimesView),
    url(r'^cases_handled_by_ethics_commision$', casesEACCView),
    url(r'^cases_forwarded_and_action_taken$', casesForwardedActediew),
    url(r'^convicted_prison_population_by_age_and_sex$', convictedPrisonAgeSexView),
    url(r'^number_of_police_prisons_and_probation_officers$', policePrisonsProbationView),
    url(r'^offences_committed_against_morality$', offenceMoralityView),
    url(r'^persons_reported_to_have_committed_homicide_by_sex$', homicideSexView),
    url(r'^persons_reported_to_have_committed_robbery_and_theft$', robberyTheftView),
    url(r'^population_projections_by_selected_age_group$', populationSelectedAgeGroupView),
    url(r'^population_projections_by_selected_age_group_add$', addPopulationSelectedAgeGroupView),
    url(r'^population_projections_by_selected_age_group_edit$', editPopulationSelectedAgeGroupView),
    url(r'^population_projections_by_selected_age_group_view$', viewPopulationSelectedAgeGroup),
    url(r'^population_projections_by_special_age_groups$', populationSpecialAgeGroupView),
    url(r'^population_projections_by_special_age_groups_add$', addPopulationSpecialAgeGroupView),
    url(r'^population_projections_by_special_age_groups_edit$', editPopulationSpecialAgeGroupView),
    url(r'^population_projections_by_special_age_groups_view$', viewPopulationSpecialAgeGroup),

    url(r'^land_and_climate$', land_and_climate),
    url(r'^surface_area_by_category$', viewSurfaceArea),
    url(r'^surface_area_by_category_add$', addSurfaceAreaView),
    url(r'^surface_area_by_category_edit$', editSurfaceAreaView),
    url(r'^temperature$', viewTemperature),
    url(r'^temperature_add$', addTemperatureView),
    url(r'^temperature_edit$', editTemperatureView),
    url(r'^rainfall$', viewRainfall),
    url(r'^rainfall_add$', addRainfallView),
    url(r'^rainfall_edit$', editRainfallView),
    url(r'^topography_altitude$', viewTopograhyAltitude),
    url(r'^topography_altitude_add$', addTopograhyAltitudeView),
    url(r'^topography_altitude_edit$', editTopograhyAltitudeView),

    url(r'^transport_and_communication$', transport_and_communication),
    url(r'^road_coverage_by_type_and_distance$', viewTransportCommunication),
    url(r'^road_coverage_by_type_and_distance_add$', addTransportCommunicationView),
    url(r'^road_coverage_by_type_and_distance_edit$', editTransportCommunicationView),

    url(r'^building_and_construction$', building_and_construction),
    url(r'^amount$', viewAmountBuilding),
    url(r'^amount_add$', addAmountBuildingView),
    url(r'^amount_edit$', editAmountBuildingView),
    url(r'^quarterly_civil_engineering_cost_index$', quarterlyCivilView),
    url(r'^quarterly_civil_engineering_cost_index_add$', addQuarterlyCivilView),
    url(r'^quarterly_civil_engineering_cost_index_edit$', editQuarterlyCivilView),
    url(r'^quarterly_non_residential_build_cost$', quarterlyNonResidentialView),
    url(r'^quarterly_non_residential_build_cost_add$', addQuarterlyNonResidentialView),
    url(r'^quarterly_non_residential_build_cost_edit$', editQuarterlyNonResidentialView),
    url(r'^quarterly_overal_construction_cost$', quarterlyOverallView),
    url(r'^quarterly_overal_construction_cost_add$', addQuarterlyOverallView),
    url(r'^quarterly_overal_construction_cost_edit$', editQuarterlyOverallView),
    url(r'^quarterly_residential_bulding_cost$', quarterlyResidentialView),
    url(r'^quarterly_residential_bulding_cost_add$', addQuarterlyResidentialView),
    url(r'^quarterly_residential_bulding_cost_edit$', editQuarterlyResidentialView),

    url(r'^manufacturing$', manufacturing),
    url(r'^per_change_in_quantum_indices_of_man_production$', percentageChangeView),
    url(r'^per_change_in_quantum_indices_of_man_production_add$', addPercentageChangeView),
    url(r'^per_change_in_quantum_indices_of_man_production_edit$', editPercentageChangeView),
    url(r'^quantum_indices_of_manufacturing_production$', quantumIndicesView),
    url(r'^quantum_indices_of_manufacturing_production_add$', addQuantumIndicesView),
    url(r'^quantum_indices_of_manufacturing_production_edit$', editQuantumIndicesView),

    url(r'^energy$', energy),
    url(r'^average_retail_prices_of_selected_petroleum_products$', averagePricesView),
    url(r'^average_retail_prices_of_selected_petroleum_products_add$', addAveragePricesView),
    url(r'^average_retail_prices_of_selected_petroleum_products_edit$', editAveragePricesView),
    url(r'^net_domestic_sale_of_petroleum_fuels_by_consumer_category$', domesticSaleView),
    url(r'^net_domestic_sale_of_petroleum_fuels_by_consumer_category_add$', addDomesticSaleView),
    url(r'^net_domestic_sale_of_petroleum_fuels_by_consumer_category_edit$', editDomesticSaleView),
    url(r'^value_and_quantity_of_imports_exports$', valueQuantityView),
    url(r'^value_and_quantity_of_imports_exports_add$', addValueQuantityView),
    url(r'^value_and_quantity_of_imports_exports_edit$', editValueQuantityView),
    url(r'^petroleum_supply_and_demand$', petroleumSupplyView),
    url(r'^petroleum_supply_and_demand_add$', addPetroleumSupplyView),
    url(r'^petroleum_supply_and_demand_edit$', editPetroleumSupplyView),
    url(r'^installed_and_effective_capacity_of_electricity$', installedCapacityView),
    url(r'^installed_and_effective_capacity_of_electricity_add$', addInstalledCapacityView),
    url(r'^installed_and_effective_capacity_of_electricity_edit$', editInstalledCapacityView),
    url(r'^generation_and_imports_of_electricity$', generalImportsView),
    url(r'^generation_and_imports_of_electricity_add$', addGeneralImportsView),
    url(r'^generation_and_imports_of_electricity_edit$', editGeneralImportsView),
    url(r'^electricity_demand_and_supply$', electricityDemandView),
    url(r'^electricity_demand_and_supply_add$', addElectricityDemandView),
    url(r'^electricity_demand_and_supply_edit$', editElectricityDemandView),

    url(r'^cpi$', cpi),
    url(r'^annual_avg_retail_prices_of_certain_consumer_goods_in_kenya$', averageRetailView),
    url(r'^annual_avg_retail_prices_of_certain_consumer_goods_in_kenya_add$', addAverageRetailView),
    url(r'^annual_avg_retail_prices_of_certain_consumer_goods_in_kenya_edit$', editAverageRetailView),
    url(r'^consumer_price_index$', consumerPriceView),
    url(r'^consumer_price_index_add$', addConsumerPriceView),
    url(r'^consumer_price_index_edit$', editConsumerPriceView),
    url(r'^consumer_price_index_view$', viewConsumerPrice),
    url(r'^elementary_aggregates_weights_in_the_cpi_baskets$', elementaryWeightsView),
    url(r'^elementary_aggregates_weights_in_the_cpi_baskets_add$', addElementaryWeightsView),
    url(r'^elementary_aggregates_weights_in_the_cpi_baskets_edit$', editElementaryWeightsView),
    url(r'^group_weights_for_kenya_cpi_febuary_base_2009$', groupWeightsView),
    url(r'^group_weights_for_kenya_cpi_febuary_base_2009_add$', addGroupWeightsView),
    url(r'^group_weights_for_kenya_cpi_febuary_base_2009_edit$', editGroupWeightsView),
    url(r'^group_weights_for_kenya_cpi_october_base_1997$', groupWeightsKenyaView),
    url(r'^group_weights_for_kenya_cpi_october_base_1997_add$', addGroupWeightsKenyaView),
    url(r'^group_weights_for_kenya_cpi_october_base_1997_edit$', editGroupWeightsKenyaView),

    url(r'^money_and_banking$', money_and_banking),
    url(r'^commercial_banks_bills_loans_advances$', commercialBanksView),
    url(r'^commercial_banks_bills_loans_advances_add$', addCommercialBanksView),
    url(r'^commercial_banks_bills_loans_advances_edit$', editCommercialBanksView),
    url(r'^inflation_rates$', inflationRatesView),
    url(r'^inflation_rates_add$', addInflationRatesView),
    url(r'^inflation_rates_edit$', editInflationRatesView),
    url(r'^interest_rates$', interestRatesView),
    url(r'^interest_rates_add$', addInterestRatesView),
    url(r'^interest_rates_edit$', editInterestRatesView),
    url(r'^monetary_indicators_broad_money_supply$', monetaryIndicatorsView),
    url(r'^monetary_indicators_broad_money_supply_add$', addMonetaryIndicatorsView),
    url(r'^monetary_indicators_broad_money_supply_edit$', editMonetaryIndicatorsView),
    url(r'^monetary_indicators_domestic_credit$', monetaryIndicatorsDomesticView),
    url(r'^monetary_indicators_domestic_credit_add$', addMonetaryIndicatorsDomesticView),
    url(r'^monetary_indicators_domestic_credit_edit$', editMonetaryIndicatorsDomesticView),
    url(r'^nairobi_securities_exchange$', securitiesExchangeView),
    url(r'^nairobi_securities_exchange_add$', addSecuritiesExchangeView),
    url(r'^nairobi_securities_exchange_edit$', editSecuritiesExchangeView),
    url(r'^institutions$', viewBankingInstitution),
    url(r'^institutions_add$', addBankingInstitutionView),
    url(r'^institutions_edit$', editBankingInstitutionView),



    # url(r'^health/health_life_expectancy$', health_life_expectancy),
    # url(r'^registered_births/', registered_births),
    # url(r'^registered_births_add/', registered_births_add),
    # url(r'^registered_births_edit/', registered_births_update),
    # url(r'^registered_deaths/', registered_deaths),
    # url(r'^health/deaths', allDeaths),
    # url(r'^registered_deaths_add/', addDeathsView),
    # url(r'^registered_deaths_edit/', editDeathsView),

    # url(r'^county_revenue/', CountyRevenue),
    # url(r'^county_revenue_add/', addCountyRevenue),
    # url(r'^county_revenue_edit/', editCountyRevenue),
    url(r'^getYear$', getYear),
    url(r'^getSectorCount$', getCount),
    url(r'^requestDataset$', requestDataSet),

]

urlpatterns = format_suffix_patterns(urlpatterns)
