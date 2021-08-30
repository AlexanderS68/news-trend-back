from django.shortcuts import render
from rest_framework import viewsets
from .models import Blog
from rest_framework.permissions import AllowAny
from .serializers import Blog_serializer
# Create your views here.
class Blog_view_set(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = Blog_serializer
    permission_classes = [AllowAny]
