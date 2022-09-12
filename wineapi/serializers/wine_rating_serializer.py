from rest_framework import serializers
from wineapi.models import WineRating

class WineRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WineRating
        fields = ('id', 'rating', 'wine_id', 'wine_user_id')
        depth = (2)