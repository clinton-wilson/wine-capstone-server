from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from wineapi.models import PairingFavorite
from wineapi.models.recipe import Recipe
from wineapi.models.wine import Wine
from wineapi.models.wine_user import WineUser
from wineapi.serializers import PairingFavoriteSerializer

class PairingFavoriteView(ViewSet):
    """viewset for handling pairing favorite requests"""

    def list(self, request):
        """method to handle getting all recipes"""

        pairing_favorite = PairingFavorite.objects.all()
        serializer = PairingFavoriteSerializer(pairing_favorite, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        """handles get request for a single recipe"""
        
        try:
            pairing_favorite = PairingFavorite.objects.get(pk=pk)
            serializer = PairingFavoriteSerializer(pairing_favorite)
            return Response(serializer.data)
        except PairingFavorite.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def create(self, request):
        """method to handle making a new pairing_favorite"""
        
        wine_user = WineUser.objects.get(user=request.auth.user)
        wine = Wine.objects.get(pk=request.data["wine"])
        recipe = Recipe.objects.get(pk=request.data['recipe'])

        pairing_favorite = PairingFavorite.objects.create(
            recipe=recipe,
            wine=wine,
            wine_user=wine_user
            
        )
        serializer=PairingFavoriteSerializer(pairing_favorite)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """handle put requests for a pairing_favorite"""
        
        pairing_favorite=PairingFavorite.objects.get(pk=pk)
        recipe = Recipe.objects.get(pk=request.data['recipe'])
        pairing_favorite.recipe=recipe
        wine_user = WineUser.objects.get(user=request.auth.user)
        pairing_favorite.wine_user=wine_user
        wine = Wine.objects.get(pk=request.data["wine"])
        pairing_favorite.wine=wine
        
        pairing_favorite.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """handles delete request for a pairing_favorite"""
        pairing_favorite = PairingFavorite.objects.get(pk=pk)
        pairing_favorite.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)