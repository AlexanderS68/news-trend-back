from django.conf.urls import include, url

from .views import Stock_watchlist_view_set, Article_watchlist_view_set
from rest_framework.routers import DefaultRouter


app_name = 'portfolio'

stock_watchlist_router = DefaultRouter()
stock_watchlist_router.register('', Stock_watchlist_view_set, basename='portfolio')


article_watchlist_router = DefaultRouter()
article_watchlist_router.register('', Article_watchlist_view_set, basename='portfolio')

urlpatterns = [
    url('',include(stock_watchlist_router.urls)),
    url('',include(article_watchlist_router.urls)),
]

