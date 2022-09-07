from django.db import models

class PairingFavorite(models.Model):
    wine = models.ForeignKey("Wine", on_delete=models.CASCADE, related_name="pairing_favorites")
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE, related_name="pairing_favorites")
    wine_user = models.ForeignKey("WineUser", on_delete=models.CASCADE, related_name="pairing_favorites")