from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from wineapi.models import MainIngredient
from wineapi.serializers import MainIngredientSerializer
class MainIngredientView(ViewSet):
    """Viewset for handling main ingredient requests"""
    
    def list(self, request):
        """method to handle getting all main ingredients"""
        
        main_ingredients = MainIngredient.objects.all()
        serializer = MainIngredientSerializer(main_ingredients, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        """handles get request for single main ingredient"""
        
        try:
            main_ingredient = MainIngredient.objects.get(pk=pk)
            serializer = MainIngredientSerializer(main_ingredient)
            return Response(serializer.data)
        except MainIngredient.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """method to handle making a new main ingredient"""
        
        main_ingredient = MainIngredient.objects.create(
            ingredient=request.data['ingredient']
        )
        
        serializer=MainIngredientSerializer(main_ingredient)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """handles put requests for a main ingredient"""
        
        main_ingredient=MainIngredient.objects.get(pk=pk)
        main_ingredient.ingredient=request.data['ingredient']
        
        main_ingredient.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """handles delete requests for a main ingredient"""
        main_ingredient = MainIngredient.objects.get(pk=pk)
        main_ingredient.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)