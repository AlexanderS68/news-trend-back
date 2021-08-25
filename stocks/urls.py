from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from .views import Stock_view_set

app_name = 'stocks'

stock_router = DefaultRouter()
stock_router.register('', Stock_view_set, basename='stocks')

urlpatterns = [
    url('', include(stock_router.urls))
]
