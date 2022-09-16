from django.db import models

class WineFavorite(models.Model):
    wine = models.ForeignKey("Wine", on_delete=models.CASCADE, related_name="wine_favorites")
    wine_user = models.ForeignKey("WineUser", on_delete=models.CASCADE, related_name="wine_favorites")
    
    def __str__(self) -> str:
        return f'{self.wine.vintner} {self.wine.vintage} {self.wine.varietal} favorited by {self.wine_user.user.first_name} {self.wine_user.user.last_name}'