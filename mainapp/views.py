from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet


def index(request):
    return render(request, "mainapp/index.html")


def room(request, room_name):
    return render(request, "mainapp/room.html", {"room_name": room_name})