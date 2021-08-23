from stocks.serializers import Stock_serializer
from django.shortcuts import render
from .models import Stock
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated



# Create your views here.

class Stock_view_set(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = Stock_serializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Stock.objects.all()

    def post(self, request,  format='json'):
        serializer = Stock_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)