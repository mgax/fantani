from django.contrib.gis.db import models


class Entry(models.Model):
    name = models.CharField('name', max_length=200)
    pos = models.PointField()
    time = models.DateTimeField(auto_now_add=True)

    objects = models.GeoManager()

    def __unicode__(self):
        return (
            '<Entry name="{s.name}" time="{s.time:%Y-%m-%d %H:%M}">'
            .format(s=self)
        )
