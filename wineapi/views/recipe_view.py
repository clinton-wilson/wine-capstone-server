from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from wineapi.models.recipe import Recipe
from wineapi.serializers.recipe_serializer import RecipeSerializer

class RecipeView(ViewSet):
    """Viewset for handling recipe requests
    """
    
    def list(self, request):
        """method to handle getting all recipes"""

        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        """handles get request for a single recipe"""
        
        try:
            recipe = Recipe.objects.get(pk=pk)
            serializer = RecipeSerializer(recipe)
            return Response(serializer.data)
        except Recipe.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def create(self, request):
        """method to handle making a new recipe"""
        
        recipe = Recipe.objects.create(
            instructions=request.data['instructions'],
            ingredients=request.data['ingredients'],
            name=request.data['name'],
            main_ingredient=request.data['main_ingredient'],
            summary=request.data['summary'],
            image=request.data['image'],
            more_info=request.data['more_info'],
            ready_in_minutes=request.data['ready_in_minutes'],
            serves=request.data['serves']
        )
        serializer=RecipeSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """handle put requests for a recipe"""
        
        recipe=Recipe.objects.get(pk=pk)
        recipe.instructions=request.data['instructions']
        recipe.ingredients=request.data['ingredients']
        recipe.name=request.data['name']
        recipe.main_ingredient=request.data['main_ingredient']
        recipe.summary=request.data['summary']
        recipe.image=request.data['image']
        recipe.more_info=request.data['more_info']
        recipe.ready_in_minutes=request.data['ready_in_minutes']
        recipe.serves=request.data['serves']
        
        recipe.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """handles delete request for a recipe"""
        recipe = Recipe.objects.get(pk=pk)
        recipe.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)