from django.db import models

class RecipeFavorite(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE, related_name="recipe_favorites")
    wine_user = models.ForeignKey("WineUser", on_delete=models.CASCADE, related_name="recipe_favorites")