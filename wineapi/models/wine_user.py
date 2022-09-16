from django.db import models
from django.contrib.auth.models import User

class WineUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.TextField()
    bio = models.TextField()
    admin = models.BooleanField(False)