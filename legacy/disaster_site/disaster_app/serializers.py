from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .preexisting_models import NeighborhoodUnits

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class NeighborhoodUnitsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NeighborhoodUnits
        fields = '__all__'