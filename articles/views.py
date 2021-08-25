from rest_framework.permissions import AllowAny
from .serializers import Article_serializer
from django.shortcuts import render
from .models import Article
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
# Create your views here.


class Article_view_set(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = Article_serializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Article.objects.all()

    def post(self, request,  format='json'):
        serializer = Article_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
