from django.db.models import fields
from rest_framework import serializers
from .models import StockWatchlist

class StockWatchlistSerializer:

    class Meta:
        model = StockWatchlist
        fields = "__all__"