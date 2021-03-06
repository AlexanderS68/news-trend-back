from django.conf.urls import include, url
from .views import Article_watchlist_view_set
from rest_framework.routers import DefaultRouter

# app_name = 'profolio'

# stock_watchlist_router = DefaultRouter()
# stock_watchlist_router.register(
#     '', Stock_watchlist_view_set, basename='stockwatchlist')


article_watchlist_router = DefaultRouter()
article_watchlist_router.register(
    '', Article_watchlist_view_set)

urlpatterns = [
    # url('stockwatchlist/', include(stock_watchlist_router.urls)),
    url('', include(article_watchlist_router.urls)),
]
