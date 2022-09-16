from rest_framework import serializers
from wineapi.models import Wine

class WineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wine
        fields = ('id', 'vintner', 'vintage', 'varietal', 'photo', 'submitted_by', 'main_ingredient', 'favorited')
        depth = 2