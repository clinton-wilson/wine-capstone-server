from unicodedata import name
from django.db import models

from wineapi.models import main_ingredient

class Recipe(models.Model):
    instructions = models.TextField()
    ingredients = models.TextField()
    ready_in_minutes = models.IntegerField()
    serves = models.IntegerField()
    image = models.URLField()
    name = models.CharField(max_length=150)
    main_ingredient = models.ForeignKey("MainIngredient", on_delete=models.CASCADE, related_name="recipes", null=True)
    favorite = models.ManyToManyField("WineUser", through="RecipeFavorite", related_name="recipes")
    summary=models.TextField()
    more_info=models.URLField()