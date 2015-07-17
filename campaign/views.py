from django.shortcuts import render
from django.http import HttpResponseBadRequest
from .forms import EntryForm


def index(request):
    return render(request, 'index.html')


def submit(request):
    if request.method == 'POST':
        entry_form = EntryForm(request.POST)
        if entry_form.is_valid():
            entry_form.save()
            return render(request, 'thanks.html')

    return HttpResponseBadRequest()
