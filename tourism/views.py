from django.shortcuts import render

#Create your views here.

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from tourism.models import Arrivals, Conferences, Departures, Earnings, Hotel_Occupancy_By_Residence, \
    Hotel_Occupancy_By_Zone, Visitor_To_Parks, Visitors_To_Museums, Population_Proportion_That_Took_Trip


#all tourist arrivals
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def TouristArrivals(request):
    touristarrivals = Arrivals.objects.all()

    arrivals = []

    if touristarrivals:
        for arrival in touristarrivals:
            c = {'quarter': arrival.quarter,
                 'holiday':arrival.holiday,
                 'business':arrival.business,
                 'transit':arrival.transit,
                 'other':arrival.other,
                 'year':arrival.year}
            arrivals.append(c)
    else:
        pass
    return Response(arrivals)
#all conferences
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def ConferencesHeld(request):
    conferences =Conferences.objects.all()
    allconferences =[]

    if conferences:
          for conference in conferences:
              c ={'category':conference.category,
                  'number_of_conferences':conference.category,
                  'number_of_delegates':conference.number_of_delegates,
                  'year':conference.year
                  }
              allconferences.append(c)
    else:
        pass
    return Response(allconferences)


#all departures

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def TouristDepartures(request):
    departures =Departures.objects.all()
    alldepartures =[]

    if departures:
          for depart in departures:
              c ={'quarter':depart.quarter,
                  'holiday':depart.holiday,
                  'business':depart.business,
                  'transit': depart.transit,
                  'other':depart.other,
                  'year':depart.year
                  }
              alldepartures.append(c)
    else:
        pass
    return Response(alldepartures)

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def TourismEarnings(request):
    earnings =Earnings.objects.all()
    allearnings=[]

    if earnings:
        for earning in earnings:
            c ={'tourism_earnings_billions':earning.tourism_earnings_billions,
                'year':earning.year}
            allearnings.append(c)
    else:
        pass
    return Response(allearnings)

#hotel occupancies
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def Hotel_Occupancy_By_Residences(request):
    hotel_occupancies =Hotel_Occupancy_By_Residence.objects.all()

    hotel_occupancies_residencies =[]

    if hotel_occupancies:
         for hotel_occupancies_by_residencies in hotel_occupancies:
             c={'year':hotel_occupancies_by_residencies.year,
                'permanent_occupants':hotel_occupancies_by_residencies.permanent_occupants,
                'germany': hotel_occupancies_by_residencies.germany,
                'switzerland': hotel_occupancies_by_residencies.germany,
                'america': hotel_occupancies_by_residencies.america,
                'asia': hotel_occupancies_by_residencies.asia,
                'united_kingdom': hotel_occupancies_by_residencies.united_kingdom,
                'france': hotel_occupancies_by_residencies.france,
                'scandinavia': hotel_occupancies_by_residencies.scandinavia,
                'other_europe': hotel_occupancies_by_residencies.other_europe,
                'other_america': hotel_occupancies_by_residencies.other_america,
                'other_asia': hotel_occupancies_by_residencies.other_asia,
                'all_other_countries': hotel_occupancies_by_residencies.all_other_countries,
                'tanzania': hotel_occupancies_by_residencies.tanzania,
                'uganda': hotel_occupancies_by_residencies.uganda,
                'kenya': hotel_occupancies_by_residencies.kenya_residents,
                'east_and_central_africa': hotel_occupancies_by_residencies.east_and_central_africa,
                'west_africa': hotel_occupancies_by_residencies.west_africa,
                'north_america': hotel_occupancies_by_residencies.north_africa,
                'south_africa': hotel_occupancies_by_residencies.south_africa,
                'africa': hotel_occupancies_by_residencies.africa,
                'usa': hotel_occupancies_by_residencies.usa,
                'japan': hotel_occupancies_by_residencies.japan,
                'india': hotel_occupancies_by_residencies.india,
                'middle_east': hotel_occupancies_by_residencies.middle_east,
                'other_africa ': hotel_occupancies_by_residencies.other_africa,
                'europe': hotel_occupancies_by_residencies.europe,
                'italy': hotel_occupancies_by_residencies.italy,
                'east_and _central_africa': hotel_occupancies_by_residencies.east_and_central_africa,
                'other_africa': hotel_occupancies_by_residencies.other_africa,
                'canada': hotel_occupancies_by_residencies.canada,
                'australia_and_new_Zealand': hotel_occupancies_by_residencies.australia_and_new_zealand,

                'total_occupied': hotel_occupancies_by_residencies.total_occupied,
                'total_available': hotel_occupancies_by_residencies.total_available,
                'occupancy_percetage_rate': hotel_occupancies_by_residencies.occupancy_percentage_rate

                }

             hotel_occupancies_residencies.append(c)
    else:
        pass
    return Response(hotel_occupancies_residencies)


#hotel occupancy by zone


@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def Hotels_By_Zone(request):
    hotels_by_zone =Hotel_Occupancy_By_Zone.objects.all()
    allhotels_by_zone =[]

    if hotels_by_zone:
          for hotels in hotels_by_zone:
              c ={'year':hotels.year,
                  'coastal_beach':hotels.coastal_beach,
                  'coastal_other':hotels.coastal_other,
                  'coastal_hinterland ': hotels.coastal_hinterland,
                  'nairobi_high_class ':hotels.nairobi_high_class,
                  'nairobi_other ':hotels.nairobi_other,
                  'central ':hotels.central,
                  'masailand':hotels.masailand,
                  'nyanza_basin':hotels.nyanza_basin,
                  'western':hotels.western,
                  'nothern':hotels.northern,
                  'total_occupied':hotels.total_occupied,
                  'total_available':hotels.total_available
                  }
              allhotels_by_zone.append(c)
    else:
        pass
    return Response(allhotels_by_zone)


#visitors by park
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def All_Visitor_To_Parks(request):
    visitor_to_park=Visitor_To_Parks.objects.all()
    all_visitor_to_parks =[]

    if visitor_to_park:
          for visitortoparks in visitor_to_park:
              c ={'year':visitortoparks.year,
                  'nairobi':visitortoparks.nairobi,
                  'nairobi_safari_Walk':visitortoparks.nairobi_safari_walk,
                  'nairobi_mini_orphanage  ': visitortoparks.nairobi_mini_orphanage ,
                  'amboseli  ':visitortoparks.amboseli ,
                  'tsavo_west  ':visitortoparks.tsavo_west ,
                  'tsavo_east  ':visitortoparks.tsavo_east ,
                  'aberdare ':visitortoparks.aberdare ,
                  'lake_nakuru ':visitortoparks.lake_nakuru ,
                  'masai_mara ':visitortoparks.masai_mara ,
                  'hallers_park ':visitortoparks.hallers_park ,
                  'malindi_marine ':visitortoparks.malindi_marine ,
                  'lake_bogoria ':visitortoparks.lake_bogoria,
                  'meru  ':visitortoparks.meru,
                  'shimba_hills   ':visitortoparks.shimba_hills,
                  'mt_kenya  ':visitortoparks.mt_kenya,
                  'samburu  ':visitortoparks.samburu ,
                  'kisite_mpunguti  ':visitortoparks.kisite_mpunguti,
                  'mombasa_marine  ':visitortoparks.mombasa_marine,
                  'watamu_marine ':visitortoparks.watamu_marine,
                  'hells_gate  ': visitortoparks.hells_gate ,
                  'impala_sanctuary_kisumu  ': visitortoparks.impala_sanctuary_kisumu ,
                  'mt_longonot  ': visitortoparks.mt_longonot ,
                  'other   ': visitortoparks.other
                  }
              all_visitor_to_parks.append(c)
    else:
        pass
    return Response(all_visitor_to_parks)


#visitors by park
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def All_Visitor_To_Parks(request):
    visitor_to_park=Visitor_To_Parks.objects.all()
    all_visitor_to_parks =[]

    if visitor_to_park:
          for visitortoparks in visitor_to_park:
              c ={'year':visitortoparks.year,
                  'nairobi':visitortoparks.nairobi,
                  'nairobi_safari_Walk':visitortoparks.nairobi_safari_walk,
                  'nairobi_mini_orphanage  ': visitortoparks.nairobi_mini_orphanage ,
                  'amboseli  ':visitortoparks.amboseli ,
                  'tsavo_west  ':visitortoparks.tsavo_west ,
                  'tsavo_east  ':visitortoparks.tsavo_east ,
                  'aberdare ':visitortoparks.aberdare ,
                  'lake_nakuru ':visitortoparks.lake_nakuru ,
                  'masai_mara ':visitortoparks.masai_mara ,
                  'hallers_park ':visitortoparks.hallers_park ,
                  'malindi_marine ':visitortoparks.malindi_marine ,
                  'lake_bogoria ':visitortoparks.lake_bogoria,
                  'meru  ':visitortoparks.meru,
                  'shimba_hills   ':visitortoparks.shimba_hills,
                  'mt_kenya  ':visitortoparks.mt_kenya,
                  'samburu  ':visitortoparks.samburu ,
                  'kisite_mpunguti  ':visitortoparks.kisite_mpunguti,
                  'mombasa_marine  ':visitortoparks.mombasa_marine,
                  'watamu_marine ':visitortoparks.watamu_marine,
                  'hells_gate  ': visitortoparks.hells_gate ,
                  'impala_sanctuary_kisumu  ': visitortoparks.impala_sanctuary_kisumu ,
                  'mt_longonot  ': visitortoparks.mt_longonot ,
                  'other   ': visitortoparks.other
                  }
              all_visitor_to_parks.append(c)
    else:
        pass
    return Response(all_visitor_to_parks)



#visitors by museums
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def All_Visitors_To_Museums(request):
    visitor_to_museum=Visitors_To_Museums.objects.all()
    all_visitor_to_museums =[]

    if visitor_to_museum:
          for visitor in visitor_to_museum:
              c ={'year':visitor.year,
                  'nairobi_snake_park':visitor.nairobi_snake_park,
                  'fort_jesus':visitor.fort_jesus,
                  'kisumu  ': visitor.kisumu ,
                  'kitale  ':visitor.kitale ,
                  'gede  ':visitor.gede ,
                  'meru  ':visitor.meru ,
                  'lamu ':visitor.lamu ,
                  'jumba_la_mtwana ':visitor.jumba_la_mtwana ,
                  'kariandusi ':visitor.kariandusi ,
                  'hyrax_hill ':visitor.hyrax_hill ,
                  'karen_blixen ':visitor.karen_blixen ,
                  'malindi ':visitor.malindi,
                  'kilifi_mnarani  ':visitor.kilifi_mnarani,
                  'kabarnet   ':visitor.kabarnet,
                  'kapenguria  ':visitor.kapenguria,
                  'swahili_house  ':visitor.swahili_house ,
                  'narok  ':visitor.narok,
                  'german_post  ':visitor.german_post,
                  'takwa_ruins ':visitor.takwa_ruins

                  }
              all_visitor_to_museums.append(c)
    else:
        pass
    return Response(all_visitor_to_museums)



#visitors by museums
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def All_Population_Proportion_That_Took_Trip(request):
    population=Population_Proportion_That_Took_Trip.objects.all()
    all_population =[]

    if population:
          for population_proportion in population:
              c ={'county_id':population_proportion.county_id,
                  'no_of_individuals':population_proportion.no_of_individuals,
                  'proportion':population_proportion.proportion,


                  }
              all_population.append(c)
    else:
        pass
    return Response(all_population)