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
from . import forms
from . import models
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
import datetime
from django.views.generic.base import TemplateView


class Home(TemplateView):
    template_name = 'home.html'


class WorldBorderMapView(TemplateView):
    """Markers map view."""

    template_name = "map.html"


class AddMarkerWorldBorderMapView(TemplateView):
    """Markers map view."""

    template_name = "addmapmarker.html"


def add_marker_world_border_map_view(request):
    # world_instance = get_object_or_404(models.WorldBorder)
    world_instance = models.WorldBorder()
    form = forms.AddMarkerForm(request.POST)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            world_instance.name = form.cleaned_data['name']
            world_instance.save()

            # redirect to a new URL:
            return redirect('/map')
            return HttpResponseRedirect(reverse('map/'))

    # If this is a GET (or any other method) create the default form.
    else:
        form = forms.AddMarkerForm()

    return render(request, 'addmapmarker.html', {'form': form, "world_instance": world_instance, })
