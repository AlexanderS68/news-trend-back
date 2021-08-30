from django.db.models import fields
from core.settings import REST_FRAMEWORK
from rest_framework import serializers
from .models import Blog

class Blog_serializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'