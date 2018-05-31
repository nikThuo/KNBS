# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404, render, render_to_response
# from django.template.defaultfilters import register
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import renderer_classes, api_view
# from rest_framework.renderers import JSONRenderer
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.template import loader
# import json
# from rest_framework import status, permissions
# #from .models import Counties, RegisteredBirthsOccurrence, RegisteredDeathsOccurrence, ProjectedLifeExpectancy, Death, \
#    # Diseases
#     # , HealthFacilities, MedicalPersonnel, NhifMembers, NhifResources
# from .serializers import CountiesSerializer
#
# # List all Counties or creates a new one
# # counties/
# # class CountiesList(APIView):
# #
# #     def get(self, request):
# #         county = Counties.objects.all()
# #         serializer = CountiesSerializer(county, many=True)
# #         return Response(serializer.data)
# #
# #     def post(self):
# #         pass
#
# #permission_classes = (permissions.AllowAny,)
#
# def index(request):
#     return render(request, template_name='knbs_bi/index.html')
#
# def health(request):
#     return render(request, template_name='knbs_bi/health.html')
#
# def registered_births(request):
#     all_births = RegisteredBirthsOccurrence.objects.all()
#     context = {'reg_births': all_births}
#     return render(request, 'knbs_bi/registered_births.html', context)
#
# from .forms import KnbsForm
# def registered_births_add(request):
#     #if request.method == 'POST':
#     form = KnbsForm(request.POST)
#     if form.is_valid():
#         #data = form.cleaned_data
#         instance = form.save()
#         #county = form.cleaned_data['county']
#         #instance.year = form.cleaned_data('year')
#         instance.county = request.POST.get('county')
#         instance.year = request.POST.get('year')
#         instance.health_facility = request.POST.get('health_facility')
#         instance.home= request.POST.get('home')
#         form.save()
#         #return HttpResponse('Done')
#     context = {'add_births':form}
#
#     # add_births.county = '001'
#     # add_births.year = '1900'
#     #getattr(county = add_births.county)
#     #add_births.county = request.__getattribute__('county')
#     #add_births.save()
#         #context = {'add_births': add_births}
#     return render(request, 'knbs_bi/registered_births_add.html', context)
#
# @csrf_exempt
# def registered_births_update(request):
#     #all_births = RegisteredBirthsOccurrence.objects.all()
#     #context = {'reg_births': all_births}
#     return render(request, 'knbs_bi/registered_births_edit.html')
#
# @register.filter(name = 'range')
# def filter_year(start, end):
#     return range(start, end)
#
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def health_birth_all(request):
#     reg_births = RegisteredBirthsOccurrence.objects.all()
#     #template = loader.get_template('knbs_bi/base.html')
#
#
#     births = []
#
#     if reg_births:
#         for birth in reg_births:
#             #print(reg_births[birth].county)
#             c = {'county': birth.county, 'year':birth.year, 'facility':birth.health_facility, 'home':birth.home}
#             births.append(c)
#     else:
#         pass
#
#     return Response(births)
#
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def health_birth_add(request):
#     if request.method == 'POST':
#         births_add = RegisteredBirthsOccurrence(county = request.data['county'], year = request.data['year'], health_facility = request.data['facility'], home = request.data['home'])
#
#         if births_add:
#             births_add.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def health_birth_update_load(request):
#     births_update = RegisteredBirthsOccurrence.objects.get(birth_id=request.data['birth'])
#
#     birth_load = []
#
#     if births_update:
#         c = {'id': births_update.birth_id,'county': births_update.county, 'year':births_update.year, 'facility':births_update.health_facility, 'home':births_update.home}
#         birth_load.append(c)
#     else:
#         pass
#
#     return Response(birth_load)
#
#
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def health_birth_update(request):
#
#     births_update = RegisteredBirthsOccurrence.objects.get(birth_id = request.data['birth'])
#
#     if 'county' in request.data:
#        births_update.county = request.data['county']
#     if 'year' in request.data:
#        births_update.year = request.data['year']
#     if 'facility' in request.data:
#         births_update.health_facility = request.data['facility']
#     if 'home' in request.data:
#         births_update.home = request.data['home']
#
#     births_update.save()
#     response = {'county': births_update.county, 'year': births_update.year, 'facility': births_update.health_facility, 'home': births_update.home}
#     return Response(response)
#
#
#
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def health_birth_delete(request):
#     birth_delete = RegisteredBirthsOccurrence.objects.filter(county = request.data['county_id']).delete()
#
#     if birth_delete:
#         return Response(status=status.HTTP_201_CREATED)
#     return Response(status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def health_births(request):
#     reg_births = RegisteredBirthsOccurrence.objects.filter(county = request.data['county_id'])
#     #reg_deaths = RegisteredDeathsOccurrence.objects.filter(county = request.data['county_id'])
#
#
#     births = []
#
#
#     if reg_births:
#         for birth in reg_births:
#             #print(reg_births[birth].county)
#             c = {'county': birth.county, 'year':birth.year, 'facility':birth.health_facility, 'home':birth.home}
#             births.append(c)
#     else:
#         pass
#
#     deaths = []
#
#     # if reg_deaths:
#     #     for death in reg_deaths:
#     #         d = {'county':death.county, 'year':death.year, 'facility':death.health_facility, 'home': death.home}
#     #         deaths.append(d)
#     # else:
#     #     pass
#
#
#
#     response = {'birth': births}
#     return Response(response)
#     #return Response("$$$$TRUE")
#
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def health_death_all(request):
#     reg_deaths = RegisteredDeathsOccurrence.objects.all()
#
#     deaths = []
#
#     if reg_deaths:
#         for death in reg_deaths:
#             d = {'county': death.county, 'year': death.year, 'facility': death.health_facility, 'home': death.home}
#             deaths.append(d)
#     else:
#         pass
#
#     return Response(deaths)
#
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def health_life_expectancy(request):
#     life_expectancy = ProjectedLifeExpectancy.objects.filter(year_range=request.data['range'])
#
#     expectancies = []
#
#     if life_expectancy:
#         for expectancy in life_expectancy:
#             l = {'status': expectancy.hiv_status, 'gender': expectancy.gender, 'range': expectancy.year_range,
#                  'index': expectancy.expectancy_index}
#             expectancies.append(l)
#     else:
#         pass
#
#     response = {'year range': expectancies}
#     return Response(response)
#
# #===============================REGISTERED DEATHS===============================
# #Launch Page
# def registered_deaths(request):
#     all_births = RegisteredDeathsOccurrence.objects.all()
#     context = {'reg_deaths': all_births}
#     return render(request, 'knbs_bi/registered_deaths.html', context)
#
# #All Deaths
# @csrf_exempt
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def allDeaths(request):
#     reg_deaths = RegisteredDeathsOccurrence.objects.all()
#
#     deaths = []
#
#     if reg_deaths:
#         for death in reg_deaths:
#             #print(reg_births[birth].county)
#             c = {'county': death.county, 'year':death.year, 'facility':death.health_facility, 'home':death.home}
#             deaths.append(c)
#     else:
#         pass
#
#     return Response(deaths)
#
# #Add Deaths
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def addDeaths(request):
#     if request.method == 'POST':
#         deaths_add = RegisteredDeathsOccurrence(county = request.data['county'], year = request.data['year'], health_facility = request.data['facility'], home = request.data['home'])
#
#         if deaths_add:
#             deaths_add.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
# #Edit Deaths
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def updateDeaths(request):
#
#     deaths_update = RegisteredDeathsOccurrence.objects.get(death_id = request.data['death'])
#
#     if 'county' in request.data:
#         deaths_update.county = request.data['county']
#     if 'year' in request.data:
#         deaths_update.year = request.data['year']
#     if 'facility' in request.data:
#         deaths_update.health_facility = request.data['facility']
#     if 'home' in request.data:
#         deaths_update.home = request.data['home']
#
#     deaths_update.save()
#     response = {'county': deaths_update.county, 'year': deaths_update.year, 'facility': deaths_update.health_facility, 'home': deaths_update.home}
#     return Response(response)
#
# #Deaths Add View
# def addDeathsView(request):
#     return render(request, 'knbs_bi/registered_deaths_add.html')
#
# #Deaths Edit View
# def editDeathsView(request):
#     return render(request, 'knbs_bi/registered_deaths_edit.html')
#
# #===============================DEATHS===============================
# #All Death
# # @api_view(http_method_names=['POST'])
# # @renderer_classes((JSONRenderer,))
# # def Deaths(request):
# #     all_deaths = Death.objects.all()
# #
# #     deaths = []
# #
# #     if all_deaths:
# #         for death in all_deaths:
# #             #print(reg_births[birth].county)
# #             c = {'year': death.year, 'anaemia':death.anaemia, 'cancer':death.cancer, 'heart':death.heart_disease,'hiv':death.hiv_aids,
# #                  'malaria':death.malaria, 'menengitis':death.menengitis, 'accidents':death.other_accidents, 'causes':death.other_causes,
# #                  'pneumonia':death.pneumonia, 'traffic':death.road_traffic, 'tuberculosis':death.tuberclosis}
# #             deaths.append(c)
# #     else:
# #         pass
# #
# #     return Response(deaths)
#
# #Add Deaths
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def plusDeaths(request):
#     if request.method == 'POST':
#         deaths_add = Death(year = request.data['year'], anaemia = request.data['anaemia'], cancer = request.data['cancer'], heart_disease = request.data['heart'],
#                                                 hiv_aids=request.data['hiv'], malaria = request.data['malaria'], menengitis = request.data['menengitis'],
#                                                 other_accidents=request.data['accidents'], other_causes=request.data['causes'], pneumonia=request.data['pneumonia'],
#                                                 road_traffic=request.data['traffic'], tuberclosis=request.data['tuberculosis'],)
#
#         if deaths_add:
#             deaths_add.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
# #Edit Deaths
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def alterDeaths(request):
#
#     deaths_update = Death.objects.get(death_id = request.data['death'])
#
#     if 'year' in request.data:
#         deaths_update.year = request.data['year']
#     if 'anaemia' in request.data:
#         deaths_update.anaemia = request.data['anaemia']
#     if 'cancer' in request.data:
#         deaths_update.cancer = request.data['cancer']
#     if 'heart' in request.data:
#         deaths_update.heart_disease = request.data['heart']
#     if 'hiv' in request.data:
#         deaths_update.hiv_aids = request.data['hiv']
#     if 'malaria' in request.data:
#         deaths_update.malaria = request.data['malaria']
#     if 'menengitis' in request.data:
#         deaths_update.menengitis = request.data['menengitis']
#     if 'accidents' in request.data:
#         deaths_update.other_accidents = request.data['accidents']
#     if 'causes' in request.data:
#         deaths_update.other_causes = request.data['causes']
#     if 'pneumonia' in request.data:
#         deaths_update.pneumonia = request.data['pneumonia']
#     if 'traffic' in request.data:
#         deaths_update.road_traffic = request.data['traffic']
#     if 'tuberculosis' in request.data:
#         deaths_update.tuberclosis = request.data['tuberculosis']
#
#
#     deaths_update.save()
#     response = {'year': deaths_update.year, 'anaemia': deaths_update.anaemia, 'cancer': deaths_update.cancer, 'heart': deaths_update.heart_disease,
#                 'hiv':deaths_update.hiv_aids, 'malaria':deaths_update.malaria, 'menengitis':deaths_update.menengitis , 'accidents':deaths_update.other_accidents,
#                 'causes': deaths_update.other_causes,'pneumonia':deaths_update.pneumonia,'traffic':deaths_update.road_traffic,
#                 'tuberclosis': deaths_update.tuberclosis}
#     return Response(response)
#
# #===============================DISEASES===============================
# #All Diseases
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# # def allDiseases(request):
# #     all_diseases = Diseases.objects.all()
# #
# #     diseases = []
# #
# #     if all_diseases:
# #         for disease in all_diseases:
# #             #print(reg_births[birth].county)
# #             c = {'year': disease.year, 'accidents':disease.accidents, 'disease':disease.other_diseases, 'diarrhoea':disease.diarrhoea,'respiratory':disease.respiratory,
# #                  'skin':disease.skin, 'eye_infection':disease.eye_infection,  'worms':disease.intestinal_worms, 'malaria':disease.malaria,
# #                  'pneumonia':disease.pneumonia, 'joints':disease.joint_pains, 'uti':disease.uti}
# #             diseases.append(c)
# #     else:
# #         pass
# #
# #     return Response(diseases)
#
# #Add Disease
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def addDisease(request):
#     if request.method == 'POST':
#         disease_add = Diseases(year = request.data['year'], accidents = request.data['accidents'], other_diseases = request.data['diseases'], diarrhoea = request.data['diarrhoea'],
#                               respiratory=request.data['respiratory'], skin = request.data['skin'], eye_infection = request.data['infection'],
#                               intestinal_worms=request.data['worms'], malaria=request.data['malaria'], pneumonia=request.data['pneumonia'],
#                               joint_pains=request.data['joints'], uti=request.data['uti'],)
#
#         if disease_add:
#             disease_add.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
# #Edit Disease
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def editDisease(request):
#
#     disease_update = Diseases.objects.get(disease_id = request.data['disease'])
#
#     if 'year' in request.data:
#         disease_update.year = request.data['year']
#     if 'accidents' in request.data:
#         disease_update.anaemia = request.data['accidents']
#     if 'diseases' in request.data:
#         disease_update.other_diseases = request.data['diseases']
#     if 'diarrhoea' in request.data:
#         disease_update.diarrhoea = request.data['diarrhoea']
#     if 'respiratory' in request.data:
#         disease_update.respiratory = request.data['respiratory']
#     if 'skin' in request.data:
#         disease_update.skin = request.data['skin']
#     if 'infection' in request.data:
#         disease_update.eye_infection = request.data['infection']
#     if 'worms' in request.data:
#         disease_update.intestinal_worms = request.data['worms']
#     if 'malaria' in request.data:
#         disease_update.malaria = request.data['malaria']
#     if 'pneumonia' in request.data:
#         disease_update.pneumonia = request.data['pneumonia']
#     if 'joints' in request.data:
#         disease_update.joint_pains = request.data['joints']
#     if 'uti' in request.data:
#         disease_update.uti = request.data['uti']
#
#     disease_update.save()
#     response = {'year': disease_update.year, 'accidents': disease_update.accidents, 'disease': disease_update.other_diseases, 'diarrhoea': disease_update.diarrhoea,
#                 'respiratory':disease_update.respiratory, 'skin':disease_update.skin, 'infection':disease_update.eye_infection , 'worms':disease_update.intestinal_worms,
#                 'malaria': disease_update.malaria,'pneumonia':disease_update.pneumonia,'joints':disease_update.joint_pains,
#                 'uti': disease_update.uti}
#     return Response(response)
#
# #===============================HEALTH FACILITIES===============================
# # #All Health Facilities
# # @api_view(http_method_names=['POST'])
# # @renderer_classes((JSONRenderer,))
# # def allHealthFacilities(request):
# #     all_facilities = HealthFacilities.objects.all()
# #
# #     facilities = []
# #
# #     if all_facilities:
# #         for facility in all_facilities:
# #             #print(reg_births[birth].county)
# #             c = {'county': facility.county_id, 'facility':facility.facilities, 'year':facility.year}
# #             facilities.append(c)
# #     else:
# #         pass
# #
# #     return Response(facilities)
#
# #Add Health Facility
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def addFacility(request):
#     if request.method == 'POST':
#         facility_add = HealthFacilities(county_id = request.data['county'], facilities = request.data['facility'], year = request.data['year'])
#
#         if facility_add:
#             facility_add.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
# #Edit Health Facility
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def editFacility(request):
#
#     facility_update = HealthFacilities.objects.get(facility_id = request.data['facility_id'])
#
#     if 'county' in request.data:
#         facility_update.county_id = request.data['county']
#     if 'facility' in request.data:
#         facility_update.facilities = request.data['facility']
#     if 'year' in request.data:
#         facility_update.year = request.data['year']
#
#     facility_update.save()
#     response = {'county': facility_update.county_id, 'facility': facility_update.facilities, 'year': facility_update.year}
#     return Response(response)
#
# #===============================MEDICAL PERSONNEL===============================
# #All Personnel
# # @api_view(http_method_names=['POST'])
# # @renderer_classes((JSONRenderer,))
# # def allPersonnel(request):
# #     all_personnel = MedicalPersonnel.objects.all()
# #
# #     personnel = []
# #
# #     if all_personnel:
# #         for person in all_personnel:
# #             #print(reg_births[birth].county)
# #             c = {'year': person.year, 'nursing':person.bsc_nursing, 'officers':person.clinical_officers, 'dentists':person.dentists,'doctors':person.doctors,
# #                  'nurses':person.enrolled_nurses, 'pharmacists':person.pharmacists,  'pharmtech':person.pharmtech, 'health_officer':person.health_officer,
# #                  'tech':person.health_tech, 'reg_nurse':person.registered_nurse, 'total':person.total}
# #             personnel.append(c)
# #     else:
# #         pass
# #
# #     return Response(personnel)
#
# #Add Personnel
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def addPersonnel(request):
#     if request.method == 'POST':
#         personnel_add = MedicalPersonnel(year = request.data['year'], bsc_nursing = request.data['nursing'], clinical_officers = request.data['clinical_officer'], dentists = request.data['dentists'],
#                                          doctors=request.data['doctors'], enrolled_nurses = request.data['nurses'], pharmacists = request.data['pharmacists'],
#                                          pharmtech=request.data['pharmtech'], health_officer=request.data['health_officer'], health_tech=request.data['tech'],
#                                          registered_nurse=request.data['reg_nurse'], total=request.data['total'],)
#
#         if personnel_add:
#             personnel_add.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
# #Edit Personnel
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def editPersonnel(request):
#
#     personnel_update = MedicalPersonnel.objects.get(medical_personnel_id = request.data['medical'])
#
#     if 'year' in request.data:
#         personnel_update.year = request.data['year']
#     if 'nursing' in request.data:
#         personnel_update.bsc_nursing = request.data['nursing']
#     if 'clinical_officers' in request.data:
#         personnel_update.clinical_officers = request.data['clinical_officers']
#     if 'dentists' in request.data:
#         personnel_update.dentists = request.data['dentists']
#     if 'doctors' in request.data:
#         personnel_update.doctors = request.data['doctors']
#     if 'nurses' in request.data:
#         personnel_update.enrolled_nurses = request.data['nurses']
#     if 'pharmacists' in request.data:
#         personnel_update.pharmacists = request.data['pharmacists']
#     if 'pharmtech' in request.data:
#         personnel_update.pharmtech = request.data['pharmtech']
#     if 'health_officer' in request.data:
#         personnel_update.health_officer = request.data['health_officer']
#     if 'health_tech' in request.data:
#         personnel_update.health_tech = request.data['health_tech']
#     if 'reg_nurse' in request.data:
#         personnel_update.registered_nurse = request.data['reg_nurse']
#     if 'total' in request.data:
#         personnel_update.total = request.data['total']
#
#     personnel_update.save()
#     response = {'year': personnel_update.year, 'nursing': personnel_update.bsc_nursing, 'clinical_officers': personnel_update.clinical_officers, 'dentists': personnel_update.dentists,
#                 'doctors':personnel_update.doctors, 'nurses':personnel_update.enrolled_nurses, 'pharmacists':personnel_update.pharmacists , 'phartech':personnel_update.pharmtech,
#                 'health_officer': personnel_update.health_officer,'tech':personnel_update.health_tech,'reg_nurse':personnel_update.registered_nurse,
#                 'total': personnel_update.total}
#     return Response(response)
#
# #===============================NHIF MEMBERS===============================
# #All Members
# # @api_view(http_method_names=['POST'])
# # @renderer_classes((JSONRenderer,))
# # def allMembers(request):
# #     all_members = NhifMembers.objects.all()
# #
# #     members = []
# #
# #     if all_members:
# #         for member in all_members:
# #             c = {'formal': member.formal_sector, 'informal':member.informal_sector, 'total':member.total, 'year':member.year}
# #             members.append(c)
# #     else:
# #         pass
# #
# #     return Response(members)
#
# #Add Members
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def addMember(request):
#     if request.method == 'POST':
#         member_add = NhifMembers(formal_sector = request.data['formal'], informal_sector = request.data['informal'], total = request.data['total'], year = request.data['year'])
#
#         if member_add:
#             member_add.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
# #Edit Members
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def editMember(request):
#
#     member_update = NhifMembers.objects.get(nhif_member_id = request.data['member'])
#
#     if 'formal' in request.data:
#         member_update.formal_sector = request.data['formal']
#     if 'informal' in request.data:
#         member_update.informal_sector = request.data['informal']
#     if 'total' in request.data:
#         member_update.total = request.data['total']
#     if 'year' in request.data:
#         member_update.year = request.data['year']
#
#     member_update.save()
#     response = {'formal': member_update.formal_sector, 'informal': member_update.informal_sector, 'total': member_update.total, 'year': member_update.year}
#     return Response(response)
#
# #===============================NHIF MEMBERS===============================
# #All NHIF Resources
# # @api_view(http_method_names=['POST'])
# # @renderer_classes((JSONRenderer,))
# # def allNhifResources(request):
# #     all_resources = NhifResources.objects.all()
# #
# #     resources = []
# #
# #     if all_resources:
# #         for resource in all_resources:
# #             c = {'year': resource.year, 'benefits':resource.benefits, 'contributionss':resource.contributions_net_benefits, 'receipts':resource.receipts}
# #             resources.append(c)
# #     else:
# #         pass
# #
# #     return Response(resources)
#
# #Add NHIF Resources
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def addNhifResource(request):
#     if request.method == 'POST':
#         resource_add = NhifResources(year = request.data['year'], benefits = request.data['benefits'], contributions_net_benefits = request.data['contributions'], receipts = request.data['receipts'])
#
#         if resource_add:
#             resource_add.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
# #Edit NHIF Resources
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def editNhifResource(request):
#
#     resource_update = NhifResources.objects.get(resource_id = request.data['resource'])
#
#     if 'year' in request.data:
#         resource_update.year = request.data['year']
#     if 'benefits' in request.data:
#         resource_update.benefits = request.data['benefits']
#     if 'contributions' in request.data:
#         resource_update.contributions_net_benefits = request.data['contributions']
#     if 'receipts' in request.data:
#         resource_update.receipts = request.data['receipts']
#
#     resource_update.save()
#     response = {'year': resource_update.year, 'benefits': resource_update.benefits, 'contributions': resource_update.contributions_net_benefits, 'receipts': resource_update.receipts}
#     return Response(response)
#
#
# # #===============================PUBLIC FINANCE===============================
# # #Launch Page
# # def CountyRevenue(request):
# #     return render(request, 'knbs_bi/finance_county_revenue_history.html')
# #
# # #County Revenue Add View
# # def addCountyRevenue(request):
# #     return render(request, 'knbs_bi/finance_county_revenue_add.html')
# #
# # #County Revenue Edit View
# # def editCountyRevenue(request):
# #     return render(request, 'knbs_bi/finance_county_revenue_edit.html')
#
#
#
#
#
#
