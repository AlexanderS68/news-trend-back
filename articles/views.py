from rest_framework.permissions import AllowAny
from .serializers import ArticleSerializer
from django.shortcuts import render
from .models import Article
from rest_framework import viewsets
# Create your views here.

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]