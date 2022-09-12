from rest_framework import serializers
from wineapi.models import Varietal

class VarietalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Varietal
        fields = ('id', 'varietal')