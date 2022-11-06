from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view()),
    path("map/", views.WorldBorderMapView.as_view()),
    #path("map/add/", views.AddMarkerWorldBorderMapView.as_view()),
    # path('book/<uuid:pk>/renew/', views.AddMarkerWorldBorderMapView,
    #      name='add-marker-world-border-map-view'),
    path('map/add/', views.add_marker_world_border_map_view,
         name='add-marker-world-border-map-view'),
]
