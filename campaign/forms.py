from django.contrib.gis.forms import ModelForm
from .models import Entry


class EntryForm(ModelForm):

    class Meta:
        model = Entry
        fields = ['name', 'pos']
