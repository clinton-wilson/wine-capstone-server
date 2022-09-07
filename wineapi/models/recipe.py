from unicodedata import name
from django.db import models

from wineapi.models import main_ingredient

class Recipe(models.Model):
    instructions = models.TextField()
    ingredients = models.TextField()
    prep_time = models.IntegerField(null=True)
    cook_time = models.IntegerField(null=True)
    serves = models.IntegerField(null=True)
    photo = models.TextField()
    name = models.CharField(max_length=150)
    main_ingredient = models.ForeignKey("MainIngredient", on_delete=models.CASCADE, related_name="recipes")
    favorite = models.ManyToManyField("WineUser", through="RecipeFavorite", related_name="recipes")