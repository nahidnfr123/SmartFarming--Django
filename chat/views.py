# chat/views.py
from django.shortcuts import render

app_name = 'chat'


def index(request):
    return render(request, 'chat.html')


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })
