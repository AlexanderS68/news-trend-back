from django.db.models import fields
from rest_framework import serializers
from .models import Stock_watchlist, Article_watchlist

class Stock_watchlist_serializer(serializers.ModelSerializer):

    class Meta:
        model = Stock_watchlist
        fields = "__all__"


class Article_watchlist_serializer(serializers.ModelSerializer):

    class Meta:
        model = Article_watchlist
        fields = "__all__"