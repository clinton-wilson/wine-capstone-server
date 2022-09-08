from django.core.management.base import BaseCommand
import requests
from wineapi.models.recipe import Recipe

class Command(BaseCommand):
    def handle(self, *args, **options):
        recipe_request = requests.get('https://api.spoonacular.com/recipes/random?apiKey=632689716d184289ba940f30a19e4cf6&number=10')
        for r in recipe_request.json()["recipes"]:
            ingredients = ""
            for i in r["extendedIngredients"]:
                ingredients += i["original"]
            recipe = Recipe.objects.create(
                instructions=r["instructions"],
                ingredients=ingredients,
                ready_in_minutes=r["readyInMinutes"],
                image=r["image"],
                name=r["title"],
                serves=r["servings"],
                summary=r["summary"],
                more_info=r["sourceUrl"]
                )
