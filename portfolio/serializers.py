from django.db.models import fields
from rest_framework import serializers
from .models import StockWatchlist, ArticleWatchlist

class StockWatchlistSerializer:

    class Meta:
        model = StockWatchlist
        fields = "__all__"


class StockWatchlistSerializer:

    class Meta:
        model = ArticleWatchlist
        fields = "__all__"