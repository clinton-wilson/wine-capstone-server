from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from wineapi.models import Varietal
from wineapi.serializers import VarietalSerializer

class VarietalView(ViewSet):
    """viewset for handling varietal requests"""

    def list(self, request):
        """method to handle getting all varietals"""

        varietals = Varietal.objects.all()
        serializer = VarietalSerializer(varietals, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        """handles get request for a single varietal"""
        
        try:
            varietal = Varietal.objects.get(pk=pk)
            serializer = VarietalSerializer(varietal)
            return Response(serializer.data)
        except Varietal.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def create(self, request):
        """method to handle making a new varietal"""

        varietal = Varietal.objects.create(
            varietal=request.data['varietal']            
        )
        serializer=VarietalSerializer(varietal)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """handle put requests for a varietal"""
        
        varietal=Varietal.objects.get(pk=pk)
        varietal=request.data['varietal']            

        
        varietal.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """handles delete request for a varietal"""
        varietal = Varietal.objects.get(pk=pk)
        varietal.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)