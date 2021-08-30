from .serializers import Coin_serializer
from django.shortcuts import render
from .models import Coin
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated


# Create your views here.

class Coin_view_set(viewsets.ModelViewSet):
    queryset = Coin.objects.all()
    serializer_class = Coin_serializer
    permission_classes = [AllowAny]

    def post(self, request,  format='json'):
        serializer = Coin_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)