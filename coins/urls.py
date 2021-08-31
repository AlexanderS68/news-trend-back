from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from .views import Coin_view_set

app_name = 'coins'

coin_router = DefaultRouter()
coin_router.register('', Coin_view_set, basename='coins')

urlpatterns = [
    url('', include(coin_router.urls))
]