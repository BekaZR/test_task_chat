from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from django.shortcuts import render


def index(request):
    return render(request, "mainapp/index.html")