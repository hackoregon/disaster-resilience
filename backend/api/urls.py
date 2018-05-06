from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'NeighborhoodUnits', views.NeighborhoodUnitsSet)
router.register(r'BuildingFootprints', views.BuildingFootprintsSet)
router.register(r'CensusBgAoi', views.CensusBgAoiSet)
router.register(r'CommunityCenters', views.CommunityCentersSet)
router.register(r'CountiesAoi', views.CountiesAoiSet)
router.register(r'ElectricalTransmissionStructures', views.ElectricalTransmissionStructuresSet)
router.register(r'Hydrants', views.HydrantsSet)
router.register(r'Hospital', views.HospitalSet)
router.register(r'Jurisdictions', views.JurisdictionsSet)
router.register(r'LossJurisdictionCszM9P0Dry', views.LossJurisdictionCszM9P0DrySet)
router.register(r'LossJurisdictionCszM9P0Wet', views.LossJurisdictionCszM9P0WetSet)
router.register(r'LossJurisdictionPhfM6P8Dry', views.LossJurisdictionPhfM6P8DrySet)
router.register(r'LossJurisdictionPhfM6P8Wet', views.LossJurisdictionPhfM6P8WetSet)
router.register(r'LossNeighborhoodUnitCszM9P0Dry', views.LossNeighborhoodUnitCszM9P0DrySet)
router.register(r'LossNeighborhoodUnitCszM9P0Wet', views.LossNeighborhoodUnitCszM9P0WetSet)
router.register(r'LossNeighborhoodUnitPhfM6P8Dry', views.LossNeighborhoodUnitPhfM6P8DrySet)
router.register(r'LossNeighborhoodUnitPhfM6P8Wet', views.LossNeighborhoodUnitPhfM6P8WetSet)
router.register(r'PhfM6P8BedrockGroundmotion', views.PhfM6P8BedrockGroundmotionSet)
router.register(r'PointsOfService', views.PointsOfServiceSet)
router.register(r'PopulationAndBuildingDensity', views.PopulationAndBuildingDensitySet)
router.register(r'PressureZones', views.PressureZonesSet)
router.register(r'PressurizedMains', views.PressurizedMainsSet)
router.register(r'RegionalDrinkingWaterAdvisoryBoundary', views.RegionalDrinkingWaterAdvisoryBoundarySet)
router.register(r'RegionalWaterDistricts', views.RegionalWaterDistrictsSet)
router.register(r'Services', views.ServicesSet)
router.register(r'UnreinforcedMasonryBuildings', views.UnreinforcedMasonryBuildings)


urlpatterns = [
    url(r'^', include(router.urls)),
    #path('', include('router.urls')),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]