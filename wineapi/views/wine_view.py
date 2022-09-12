from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from wineapi.models import Wine
from wineapi.models.varietal import Varietal
from wineapi.models.wine_user import WineUser
from wineapi.serializers import WineSerializer

class WineView(ViewSet):
    """viewset for handling wine requests"""

    def list(self, request):
        """method to handle getting all recipes"""
        varietal = request.query_params.get('varietal', None)
        wines = Wine.objects.all()
        if varietal is not None:
            wines = wines.filter(varietal_id=varietal)
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
        wine = Wine.objects.create(
            varietal=varietal,
            submitted_by=wine_user,
            vintner=request.data['vintner'],
            vintage=request.data['vintage'],
            photo=request.data['photo']
        )
        serializer=WineSerializer(wine)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """handle put requests for a wine"""
        
        wine=Wine.objects.get(pk=pk)
        wine.vintner=request.data['vintner']
        wine.vintage=request.data['vintage']
        wine.photo=request.data['photo']
        
        wine_user = WineUser.objects.get(user=request.auth.user)
        wine.submitted_by=wine_user
        varietal = Varietal.objects.get(pk=request.data['varietal'])
        wine.varietal=varietal
        
        wine.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """handles delete request for a wine"""
        wine = Wine.objects.get(pk=pk)
        wine.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)