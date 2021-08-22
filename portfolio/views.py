from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import StockWatchlistSerializer
from .models import StockWatchlist
from rest_framework.decorators import action
# Create your views here.


class StockWatchlistViewSet(viewsets.ModelViewSet):
    queryset = StockWatchlist.objects.all()
    serializer_class = StockWatchlistSerializer
    permission_classes = [AllowAny]