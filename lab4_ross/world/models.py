from django.contrib.gis.db import models


class WorldBorder(models.Model):
    name = models.CharField(max_length=255)
    adderuser = models.CharField(max_length=255)
    location = models.PointField(null=True)

    # Returns the string representation of the model.
    def __str__(self):
        return self.name
