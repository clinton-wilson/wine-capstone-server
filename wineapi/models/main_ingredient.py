from django.db import models

class MainIngredient(models.Model):
    ingredient = models.CharField(max_length=100)
    
    def __str__(self):
        return self.label
    
    