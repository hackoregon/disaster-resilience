from django.shortcuts import render
from rest_framework import viewsets

from api import models
from api import serializers


class NeighborhoodUnitsSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows NeighborhoodUnits to be viewed or edited.
    """
    queryset = models.preexisting_models.NeighborhoodUnits.objects.all()
    serializer_class = serializers.NeighborhoodUnitsSerializer