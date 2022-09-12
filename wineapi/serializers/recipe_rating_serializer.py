from rest_framework import serializers
from wineapi.models import RecipeRating

class RecipeRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeRating
        fields =('id', 'rating', 'recipe_id', 'wine_user_id')
        depth = 2