from django.db.models import fields
from rest_framework import serializers
from .models import Article
from builtins import object


class Article_serializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = "__all__"

      
