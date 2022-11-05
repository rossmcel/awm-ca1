# from django.views import generic  # django generic view

# # to get our longitude and latitude
# from django.contrib.gis.geos import fromstr, Point

# # distance between us and fav places
# from django.contrib.gis.db.models.functions import Distance

# from .models import Myplaces

# from django.http import HttpResponse

# from django.core.serializers import serialize


# longitude = -80.191788

# latitude = 25.761681


# # default location we will use gps geolocation in future totorials.
# my_location = Point(longitude, latitude, srid=4326)


# class Home(generic.ListView):
#     model = Myplaces
#     context_object_name = 'places'
#     queryset = Myplaces.objects.annotate(distance=Distance(
#         'location', my_location)).order_by('distance')[0:6]

#     template_name = 'home.html'

#     def places_dataset(request):
#         place = serialize('geojson', Myplaces.objects.all())
#         return HttpResponse(place, content_type='json')
from django.views.generic.base import TemplateView


class Home(TemplateView):
    template_name = 'home.html'


class WorldBorderMapView(TemplateView):
    """Markers map view."""

    template_name = "map.html"
