from rest_framework import serializers
from .models import Coin

class Coin_serializer(serializers.ModelSerializer):

    class Meta:
        model = Coin
        fields = '__all__'