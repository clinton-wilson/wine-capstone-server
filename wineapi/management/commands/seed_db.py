from turtle import title
from django.core.management.base import BaseCommand
import requests
from wineapi.models.recipe import Recipe
from wineapi.models.wine import Wine

class Command(BaseCommand):
    def handle(self, *args, **options):
        # recipe_request = requests.get('https://api.spoonacular.com/recipes/random?apiKey=de0370b0aae443489712b13c4bfdcc22&number=10')
        # for r in recipe_request.json()["recipes"]:
        #     ingredients = ""
        #     for i in r["extendedIngredients"]:
        #         ingredients += i["original"]
        #     recipe = Recipe.objects.create(
        #         instructions=r["instructions"],
        #         ingredients=ingredients,
        #         ready_in_minutes=r["readyInMinutes"],
        #         image=r["image"],
        #         name=r["title"],
        #         serves=r["servings"],
        #         summary=r["summary"],
        #         more_info=r["sourceUrl"]
        #         )
            
        wine_request = requests.get('https://api.spoonacular.com/food/wine/recommendation?apiKey=de0370b0aae443489712b13c4bfdcc22&wine=pinot_noir&number=12')
        for w in wine_request.json()["recommendedWines"]:
            wine = Wine.objects.create(
                title=w['title'],
                description=w['description'],
                photo=w['imageUrl'],
                link=w['link'],
                price=w['price'],
                score=w['score']
            )
