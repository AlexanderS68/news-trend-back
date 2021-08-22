from django.urls import path
from django.urls.conf import include
from .views import StockWatchlistViewSet

app_name = 'portfolio'

urlpatterns = [
    path('stockWatchlist', StockWatchlistViewSet.as_view({'get': 'list'}), name='stockWatchlist'),
]

