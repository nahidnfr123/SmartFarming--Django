from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.

def index(request, template_name='weather.html'):
    return render(request, template_name)
