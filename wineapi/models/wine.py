from django.db import models

class Wine(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    varietal = models.ForeignKey("Varietal", on_delete=models.CASCADE, related_name="wines", null=True)
    favorite = models.ManyToManyField("WineUser", through="WineFavorite", related_name="favorite_wines")
    submitted_by = models.ForeignKey("WineUser", on_delete=models.CASCADE, related_name="submitted_by_wines", null=True)
    link = models.URLField()
    photo = models.URLField()
    price = models.CharField(max_length=100)
    score = models.IntegerField()
    main_ingredient = models.ForeignKey("MainIngredient", on_delete=models.CASCADE, related_name="wines", null=True)
    
    def __str__(self):
        return self.name
    
    @property
    def favorited(self):
        return self.__favorited
    
    @favorited.setter
    def favorited(self, value):
        self.__favorited = value