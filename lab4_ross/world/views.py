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
import os
import sys
from . import forms
from . import models
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
import datetime
from django.views.generic.base import TemplateView
from django.contrib.gis.geos import Point
import json
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class Home(TemplateView):
    template_name = 'home.html'


@method_decorator(login_required, name='dispatch')
class WorldBorderMapView(TemplateView):
    """Markers map view."""

    template_name = "map.html"


@method_decorator(login_required, name='dispatch')
class AddMarkerWorldBorderMapView(TemplateView):
    """Markers map view."""

    template_name = "addmapmarker.html"


@login_required
def add_marker_world_border_map_view(request):
    # world_instance = get_object_or_404(models.WorldBorder)
    world_instance = models.WorldBorder()
    form = forms.AddMarkerForm(request.POST)

    # If this is a POST request then process the Form data
    if request.method == 'POST':
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

        if is_ajax:
            # my_location = request.POST.get("point", None)
            # if not my_location:
            #     return JsonResponse({"message": "No location found."}, status=400)
            data = json.load(request)
            todo = data.get('payload')
            print(todo['lat'], os.getcwd())
            world_instance.name = "Current Location"
            pnt = Point(todo['lng'], todo['lat'])
            world_instance.location = pnt
            world_instance.adderuser = request.user
            world_instance.save()
            return JsonResponse({'status': 'Data added!'})

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            world_instance.name = form.cleaned_data['name']
            pnt = Point(form.cleaned_data['lng'], form.cleaned_data['lat'])
            world_instance.location = pnt
            world_instance.adderuser = request.user
            world_instance.save()

            # redirect to a new URL:
            return redirect('/map')

    # If this is a GET (or any other method) create the default form.
    else:
        form = forms.AddMarkerForm()

    return render(request, 'map.html', {'form': form, "world_instance": world_instance, })
