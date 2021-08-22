from stocks.serializers import StockSerializer
from django.shortcuts import render
from .models import Stock
from rest_framework import viewsets
# Create your views here.

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
