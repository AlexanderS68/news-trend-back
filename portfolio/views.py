from articles.models import Article
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import Stock_watchlist_serializer
from .models import Stock_watchlist
from rest_framework.decorators import action
# Create your views here.


class Stock_watchlist_view_set(viewsets.ModelViewSet):
    queryset = Stock_watchlist.objects.all()
    serializer_class = Stock_watchlist_serializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Stock_watchlist.objects.all()



class Article_watchlist_view_set(viewsets.ModelViewSet):
    queryset = Stock_watchlist.objects.all()
    serializer_class = Stock_watchlist_serializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Article.objects.all()