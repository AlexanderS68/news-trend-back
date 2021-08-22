from .serializers import ArticleSerializer
from django.shortcuts import render
from .models import Article
from rest_framework import viewsets
# Create your views here.

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer