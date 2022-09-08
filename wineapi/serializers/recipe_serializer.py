from pyexpat import model
from rest_framework import serializers
from wineapi.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields =('id', 'instructions', 'ingredients', 'prep_time', 'cook_time', 'photo', 'name', 'main_ingredient_id', 'serves' )
