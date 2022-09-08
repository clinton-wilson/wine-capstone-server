from rest_framework import serializers
from wineapi.models import Wine

class WineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wine
        fields = ('id', 'vintner', 'vintage', 'varietal_id', 'photo', 'submitted_by_id')
        depth = 1