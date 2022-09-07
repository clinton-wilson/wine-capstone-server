from django.db import models

class WineRating(models.Model):
    wine = models.ForeignKey("Wine", on_delete=models.CASCADE, related_name="wine_rating")
    wine_user = models.ForeignKey("WineUser", on_delete=models.CASCADE, related_name="wine_rating")
    rating = models.IntegerField()