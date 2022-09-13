from unicodedata import name
from django.db import models

class Wine(models.Model):
    vintner = models.CharField(max_length=150)
    varietal = models.ForeignKey("Varietal", on_delete=models.CASCADE, related_name="wines")
    vintage = models.IntegerField()
    favorite = models.ManyToManyField("WineUser", through="WineFavorite", related_name="favorite_wines")
    submitted_by = models.ForeignKey("WineUser", on_delete=models.CASCADE, related_name="submitted_by_wines")
    photo = models.TextField(null=True)
    main_ingredient = models.ForeignKey("MainIngredient", on_delete=models.CASCADE, related_name="wines")