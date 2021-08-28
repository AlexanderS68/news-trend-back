from portfolio.models import Article_watchlist
from articles.models import Article
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import Article_watchlist_serializer
from rest_framework.decorators import action
# Create your views here.


# class Stock_watchlist_view_set(viewsets.ModelViewSet):
#     queryset = Stock_watchlist.objects.all()
#     serializer_class = Stock_watchlist_serializer
#     permission_classes = [AllowAny]

#     def get_queryset(self):
#         return Stock_watchlist.objects.all()


class Article_watchlist_view_set(viewsets.ModelViewSet):
    queryset = Article_watchlist.objects.all()
    serializer_class = Article_watchlist_serializer
    permission_classes = [AllowAny]

        

