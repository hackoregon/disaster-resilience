from django.shortcuts import render
from rest_framework import viewsets

from api.models import preexisting_models
from api import serializers


class NeighborhoodUnitsSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows NeighborhoodUnits to be viewed or listed.
    """
    queryset = preexisting_models.NeighborhoodUnits.objects.all()
    serializer_class = serializers.NeighborhoodUnitsSerializer


class BuildingFootprintsSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows NeighborhoodUnits to be viewed or listed.
    """
    queryset = preexisting_models.BuildingFootprints.objects.all()
    serializer_class = serializers.BuildingFootprintsSerializer


class ElectricalTransmissionStructuresSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows NeighborhoodUnits to be viewed or listed.
    """
    queryset = preexisting_models.ElectricalTransmissionStructures.objects.all()
    serializer_class = serializers.ElectricalTransmissionStructuresSerializer


class EmergencyTransportationRoutesSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows NeighborhoodUnits to be viewed or listed.
    """
    queryset = preexisting_models.EmergencyTransportationRoutes.objects.all()
    serializer_class = serializers.EmergencyTransportationRoutesSerializer

class HydrantsSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows NeighborhoodUnits to be viewed or listed.
    """
    queryset = preexisting_models.Hydrants.objects.all()
    serializer_class = serializers.HydrantsSerializer


class JurisdictionsSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows NeighborhoodUnits to be viewed or listed.
    """
    queryset = preexisting_models.Jurisdictions.objects.all()
    serializer_class = serializers.JurisdictionsSerializer


class LossJurisdictionCszM9P0DrySet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows NeighborhoodUnits to be viewed or listed.
    """
    queryset = preexisting_models.LossJurisdictionCszM9P0Dry.objects.all()
    serializer_class = serializers.LossJurisdictionCszM9P0DrySerializer


class LossJurisdictionCszM9P0WetSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows NeighborhoodUnits to be viewed or listed.
    """
    queryset = preexisting_models.LossJurisdictionCszM9P0Wet.objects.all()
    serializer_class = serializers.LossJurisdictionCszM9P0WetSerializer


class LossJurisdictionPhfM6P8DrySet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows NeighborhoodUnits to be viewed or listed.
    """
    queryset = preexisting_models.LossJurisdictionPhfM6P8Dry.objects.all()
    serializer_class = serializers.LossJurisdictionPhfM6P8DrySerializer


class LossJurisdictionPhfM6P8WetSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows NeighborhoodUnits to be viewed or listed.
    """
    queryset = preexisting_models.LossJurisdictionPhfM6P8Wet.objects.all()
    serializer_class = serializers.LossJurisdictionPhfM6P8WetSerializer


class LossNeighborhoodUnitCszM9P0DrySet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows NeighborhoodUnits to be viewed or listed.
    """
    queryset = preexisting_models.LossNeighborhoodUnitCszM9P0Dry.objects.all()
    serializer_class = serializers.LossNeighborhoodUnitCszM9P0DrySerializer


class LossNeighborhoodUnitCszM9P0WetSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows NeighborhoodUnits to be viewed or listed.
    """
    queryset = preexisting_models.LossNeighborhoodUnitCszM9P0Wet.objects.all()
    serializer_class = serializers.LossNeighborhoodUnitCszM9P0WetSerializer


class LossNeighborhoodUnitPhfM6P8DrySet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows NeighborhoodUnits to be viewed or listed.
    """
    queryset = preexisting_models.LossNeighborhoodUnitPhfM6P8Dry.objects.all()
    serializer_class = serializers.LossNeighborhoodUnitPhfM6P8DrySerializer


class LossNeighborhoodUnitPhfM6P8WetSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows NeighborhoodUnits to be viewed or listed.
    """
    queryset = preexisting_models.LossNeighborhoodUnitPhfM6P8Wet.objects.all()
    serializer_class = serializers.LossNeighborhoodUnitPhfM6P8WetSerializer


class PhfM6P8BedrockGroundmotionSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows NeighborhoodUnits to be viewed or listed.
    """
    queryset = preexisting_models.PhfM6P8BedrockGroundmotion.objects.all()
    serializer_class = serializers.PhfM6P8BedrockGroundmotionSerializer


class PointsOfServiceSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows NeighborhoodUnits to be viewed or listed.
    """
    queryset = preexisting_models.PointsOfService.objects.all()
    serializer_class = serializers.PointsOfServiceSerializer


class PopulationAndBuildingDensitySet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows NeighborhoodUnits to be viewed or listed.
    """
    queryset = preexisting_models.PopulationAndBuildingDensity.objects.all()
    serializer_class = serializers.PopulationAndBuildingDensitySerializer


class PressureZonesSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows NeighborhoodUnits to be viewed or listed.
    """
    queryset = preexisting_models.PressureZones.objects.all()
    serializer_class = serializers.PressureZonesSerializer


class PressurizedMainsSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows NeighborhoodUnits to be viewed or listed.
    """
    queryset = preexisting_models.PressurizedMains.objects.all()
    serializer_class = serializers.PressurizedMainsSerializer


class RegionalDrinkingWaterAdvisoryBoundarySet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows NeighborhoodUnits to be viewed or listed.
    """
    queryset = preexisting_models.RegionalDrinkingWaterAdvisoryBoundary.objects.all()
    serializer_class = serializers.RegionalDrinkingWaterAdvisoryBoundarySerializer


class RegionalWaterDistrictsSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows NeighborhoodUnits to be viewed or listed.
    """
    queryset = preexisting_models.RegionalWaterDistricts.objects.all()
    serializer_class = serializers.RegionalWaterDistrictsSerializer


class ServicesSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows NeighborhoodUnits to be viewed or listed.
    """
    queryset = preexisting_models.Services.objects.all()
    serializer_class = serializers.ServicesSerializer


# class SpatialRefSysSet(viewsets.ReadOnlyModelViewSet):
#     """
#     API endpoint that allows NeighborhoodUnits to be viewed or listed.
#     """
#     queryset = preexisting_models.SpatialRefSys.objects.all()
#     serializer_class = serializers.SpatialRefSysSerializer