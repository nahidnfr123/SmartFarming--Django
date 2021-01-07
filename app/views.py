from django.shortcuts import render
from django.http import HttpResponse


def home(request, template_name='index.html'):
    return render(request, template_name)


def about(request, template_name='about.html'):
    return render(request, template_name)


def contact(request, template_name='contact.html'):
    return render(request, template_name)
