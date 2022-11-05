from rest_framework_gis import serializers

from . import models


class WorldBorderSerializer(serializers.GeoFeatureModelSerializer):
    """Marker GeoJSON serializer."""

    class Meta:
        """Marker serializer meta class."""

        fields = ("id", "name")
        geo_field = "location"
        model = models.WorldBorder
