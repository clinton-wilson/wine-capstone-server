from django.db import models

class Varietal(models.Model):
    varietal = models.CharField(max_length=150)