from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from wineapi import serializers

from wineapi.models.wine_user import WineUser
from wineapi.serializers.wine_user_serializer import WineUserSerializer

class WineUserView(ViewSet):
    """viewset for handling wine user requests"""
    def list(self, request):
        """method to handle getting all wine users"""
        wine_user= WineUser.objects.all()
        
        serializer = WineUserSerializer(wine_user, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        """handles get request for a single wine user"""
        
        try:
            wine_user = WineUser.objects.get(pk=pk)
            serializer = WineUserSerializer(wine_user)
            return Response(serializer.data)
        except WineUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]},
            status=status.HTTP_404_NOT_FOUND)