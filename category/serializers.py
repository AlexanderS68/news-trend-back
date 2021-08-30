from django.db.models import fields
from rest_framework import serializers
from .models import Category
from builtins import object

class Category_serializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__" 