from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages #import messages
from django.http import HttpResponse

# Create your views here.
