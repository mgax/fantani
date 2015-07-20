from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.serializers import serialize
from django.middleware import csrf
from django.contrib.auth.decorators import login_required
from .models import Entry
from .forms import EntryForm


@login_required
def crashme(request):
    if request.method == 'POST':
        raise RuntimeError('Crashing as requested')
    return HttpResponse(
        '<form method=post>' +
        '<input type=hidden name=csrfmiddlewaretoken ' +
        'value=' + csrf.get_token(request) + '>' +
        '<button type=submit>crash'
    )


def index(request):
    return render(request, 'index.html')


def submit(request):
    if request.method == 'POST':
        entry_form = EntryForm(request.POST)
        if entry_form.is_valid():
            entry_form.save()
            return render(request, 'thanks.html')

    return HttpResponseBadRequest()


def overview(request):
    points_json = serialize(
        'geojson',
        Entry.objects.all(),
        geometry_field='pos',
        fields=['pos'],
    )
    return render(request, 'overview.html', {'points_json': points_json})
