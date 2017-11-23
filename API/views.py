from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import PlacesSerializer
from map.models import Place


# Create your views here.

class PlacesViewSet(viewsets.ModelViewSet):

    serializer_class = PlacesSerializer
    queryset = Place.objects.all()






