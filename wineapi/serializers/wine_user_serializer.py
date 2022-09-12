from rest_framework import serializers
from django.contrib.auth.models import User
from wineapi.models import WineUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')

class WineUserSerializer(serializers.ModelSerializer):
    UserSerializer()
    class Meta:
        model = WineUser
        fields = ('id', 'photo', 'bio', 'admin', 'user')