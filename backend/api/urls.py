from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'neighborhoodunits', views.NeighborhoodUnitsSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    #path('', include('router.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]