from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from wineapi.models import Wine
from rest_framework.decorators import action
from wineapi.models import wine_user
from wineapi.models.varietal import Varietal
from wineapi.models.main_ingredient import MainIngredient
from wineapi.models.wine_user import WineUser
from wineapi.serializers import WineSerializer

class WineView(ViewSet):
    """viewset for handling wine requests"""
    
    @action(methods=['post'], detail=True)
    def favorite(self, request, pk):
        """post request for a user to favorite a wine"""
        
        wine = Wine.objects.get(pk=pk)
        wine_user = WineUser.objects.get(user=request.auth.user)
        wine.favorite.add(wine_user)
        return Response({'message': 'Wine favorited'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['delete'], detail=True)
    def unfavorite(self, request, pk):
        """delete request for a user to favorite a wine"""
        wine = Wine.objects.get(pk=pk)
        wine_user = WineUser.objects.get(user=request.auth.user)
        wine.favorite.remove(wine_user)
        return Response({'message': 'Wine unfavorited'}, status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        """method to handle getting all wines"""
        varietal = request.query_params.get('varietal', None)
        search_term = request.query_params.get('search_term', None)
        wine_user = WineUser.objects.get(user=request.auth.user)
        wines = Wine.objects.all()
        if search_term is not None:
            wines = wines.filter(title__icontains = search_term) | wines.filter(varietal__varietal__icontains = search_term) | wines.filter(main_ingredient__ingredient__icontains = search_term)
        if varietal is not None:
            wines = wines.filter(varietal_id=varietal)
        for wine in wines:
            wine.favorited = wine_user in wine.favorite.all()
            
        serializer = WineSerializer(wines, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        """handles get request for a single recipe"""
        
        try:
            wine = Wine.objects.get(pk=pk)
            serializer = WineSerializer(wine)
            return Response(serializer.data)
        except Wine.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def create(self, request):
        """method to handle making a new wine"""
        
        wine_user = WineUser.objects.get(user=request.auth.user)
        varietal = Varietal.objects.get(pk=request.data['varietal'])
        main_ingredient = MainIngredient.objects.get(pk=request.data['main_ingredient'])
        wine = Wine.objects.create(
            varietal=varietal,
            submitted_by=wine_user,
            main_ingredient=main_ingredient,
            vintner=request.data['vintner'],
            vintage=request.data['vintage'],
            photo=request.data['photo']
        )
        serializer=WineSerializer(wine)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """handle put requests for a wine"""
        
        wine=Wine.objects.get(pk=pk)
        wine.title=request.data['title']
        wine.price=request.data['price']
        wine.description=request.data['description']
        wine.photo=request.data['photo']
        
        wine_user = WineUser.objects.get(user=request.auth.user)
        wine.submitted_by=wine_user
        varietal = Varietal.objects.get(pk=request.data['varietal'])
        wine.varietal=varietal
        main_ingredient = MainIngredient.objects.get(pk=request.data['main_ingredient'])
        wine.main_ingredient=main_ingredient
        
        wine.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """handles delete request for a wine"""
        wine = Wine.objects.get(pk=pk)
        wine.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)