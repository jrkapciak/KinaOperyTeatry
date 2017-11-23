from rest_framework import serializers
from map.models import Place

class PlacesSerializer(serializers.ModelSerializer):
    """Serializer for our user profile objects"""

    class Meta:
        model = Place
        fields = ('name','lat','long',)
