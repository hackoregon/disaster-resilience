# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, NeighborhoodUnitsSerializer
from .preexisting_models import NeighborhoodUnits


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    

class NeighborhoodUnitsSet(viewsets.ModelViewSet):
    """
    API endpoint that allows NeighborhoodUnits to be viewed or edited.
    """
    queryset = NeighborhoodUnits.objects.all()
    serializer_class = NeighborhoodUnitsSerializer
