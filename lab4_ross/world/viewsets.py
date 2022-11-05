"""Markers API views."""
from rest_framework import viewsets
from rest_framework_gis import filters

from . import models
from . import serializers
# from serializers import WorldBorderSerializer


class WorldBorderViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = models.WorldBorder.objects.all()
    serializer_class = serializers.WorldBorderSerializer
