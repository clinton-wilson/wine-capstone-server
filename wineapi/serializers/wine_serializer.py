from rest_framework import serializers
from wineapi.models import Wine

class WineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wine
        fields = ('id', 'title', 'description', 'varietal', 'favorite', 'submitted_by', 'photo', 'price', 'score', 'main_ingredient')
        depth = 2