from django.db import models


class RecipeRating(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE, related_name="recipe_rating")
    wine_user = models.ForeignKey("WineUser", on_delete=models.CASCADE, related_name="recipe_rating")
    rating = models.IntegerField()