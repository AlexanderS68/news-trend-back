from django.conf.urls import url, include
from rest_framework import views
from rest_framework.routers import DefaultRouter
from .views import Category_view_set
from django.urls import path
from . import views

app_name = 'category'

category_router = DefaultRouter()
category_router.register('', Category_view_set, basename='category')

urlpatterns = [
    url('', include(category_router.urls)),
]