from dataclasses import field
from rest_framework import serializers
from wineapi.models import PairingFavorite

class PairingFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PairingFavorite
        fields = ('id', 'recipe_id', 'wine_id', 'wine_user_id')
        depth = 2