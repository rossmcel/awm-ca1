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
    #queryset = models.WorldBorder.objects.all()
    queryset = models.WorldBorder.objects.get_queryset()
    serializer_class = serializers.WorldBorderSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return models.WorldBorder.objects.filter(adderuser=user)


# class WorldBorderViewSet(generics.ListAPIView):
#     """Marker view set."""

#     # bbox_filter_field = "location"
#     # filter_backends = (filters.InBBoxFilter,)
#     # queryset = models.WorldBorder.objects.all()
#     # serializer_class = serializers.WorldBorderSerializer

#     serializer_class = serializers.WorldBorderSerializer

#     def get_queryset(self):
#         """
#         This view should return a list of all the purchases
#         for the currently authenticated user.
#         """
#         user = self.request.user
#         return models.WorldBorder.objects.filter(user=user)
