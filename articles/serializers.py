from django.db.models import fields
from rest_framework import serializers
from .models import Article, Category
from builtins import object


class Article_serializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = "__all__"

class Category_serializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"        
