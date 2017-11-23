from rest_framework import serializers
from map.models import Place,Shows

class PlacesSerializer(serializers.ModelSerializer):
    """Serializer for our user profile objects"""

    class Meta:
        model = Place
        fields = ('name','lat','long',)


class ShowsSerializer(serializers.ModelSerializer):
    """Serializer for our user profile objects"""

    class Meta:
        model = Shows
        fields = ('id','lat','long',)
