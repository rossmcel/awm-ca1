from django.contrib.gis import admin
from .models import WorldBorder

#admin.site.register(WorldBorder, admin.OSMGeoAdmin)


@admin.register(WorldBorder)
class WorldBorderAdmin(admin.OSMGeoAdmin):
    """Marker admin."""

    list_display = ("name", "location")
