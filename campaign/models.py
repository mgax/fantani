from django.contrib.gis.db import models


class Entry(models.Model):
    name = models.CharField('name', max_length=200)
    lnglat = models.PointField()

    objects = models.GeoManager()
