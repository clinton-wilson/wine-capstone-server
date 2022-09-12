from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from wineapi.models import MainIngredient

class MainIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainIngredient
        fields = ('id', 'ingredient')