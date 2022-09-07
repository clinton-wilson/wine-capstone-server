from django.db import models

class WineFavorite(models.Model):
    wine = models.ForeignKey("Wine", on_delete=models.CASCADE, related_name="wine_favorites")
    wine_user = models.ForeignKey("WineUser", on_delete=models.CASCADE, related_name="wine_favorites")