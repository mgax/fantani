from django.contrib.gis import admin
from campaign.models import Entry


class EntryAdmin(admin.OSMGeoAdmin):
    default_lat = 5532000
    default_lon = 2905000
    default_zoom = 12

admin.site.register(Entry, EntryAdmin)
