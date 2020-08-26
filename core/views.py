from os import environ

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse(f'<h1>{environ.get("TEST", "Nope")}</h1>')
