from rest_framework import serializers
from wineapi.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields =('id', 'instructions', 'ingredients', 'ready_in_minutes', 'serves', 'image', 'name', 'main_ingredient', 'summary', 'more_info')
        depth = 1