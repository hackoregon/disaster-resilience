from rest_framework import serializers

from api import preexisting_models


class NeighborhoodUnitsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.NeighborhoodUnits
        fields = '__all__'

class BuildingFootprintsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.BuildingFootprints 
        fields = '__all__'

class ElectricalTransmissionStructuresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.ElectricalTransmissionStructures
        fields = '__all__'

class HydrantsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.Hydrants
        fields = '__all__'

class JurisdictionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.Jurisdictions
        fields = '__all__'

class LossJurisdictionCszM9P0DrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.LossJurisdictionCszM9P0Dry
        fields = '__all__'

class LossJurisdictionCszM9P0WetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.LossJurisdictionCszM9P0Wet
        fields = '__all__'

class LossJurisdictionPhfM6P8DrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.LossJurisdictionPhfM6P8Dry
        fields = '__all__'

class LossJurisdictionPhfM6P8WetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.LossJurisdictionPhfM6P8Wet
        fields = '__all__'

class LossNeighborhoodUnitCszM9P0DrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.LossNeighborhoodUnitCszM9P0Dry
        fields = '__all__'

class LossNeighborhoodUnitCszM9P0WetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.LossNeighborhoodUnitCszM9P0Wet
        fields = '__all__'

class LossNeighborhoodUnitPhfM6P8DrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.LossNeighborhoodUnitPhfM6P8Dry
        fields = '__all__'

class LossNeighborhoodUnitPhfM6P8WetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.LossNeighborhoodUnitPhfM6P8Wet
        fields = '__all__'

class PhfM6P8BedrockGroundmotionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.PhfM6P8BedrockGroundmotion
        fields = '__all__'

class PointsOfServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.PointsOfService
        fields = '__all__'

class PopulationAndBuildingDensitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.PopulationAndBuildingDensity
        fields = '__all__'

class PressureZonesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.PressureZones
        fields = '__all__'

class PressurizedMainsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.PressurizedMains
        fields = '__all__'

class RegionalDrinkingWaterAdvisoryBoundarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.RegionalDrinkingWaterAdvisoryBoundary
        fields = '__all__'

class RegionalWaterDistrictsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.RegionalWaterDistricts
        fields = '__all__'

class ServicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.Services
        fields = '__all__'

class SpatialRefSysSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.SpatialRefSys
        fields = '__all__'