from django.conf.urls import url, include
from rest_framework import views
from rest_framework.routers import DefaultRouter
from .views import Article_view_set
from django.urls import path
from . import views

app_name = 'articles'

articles_router = DefaultRouter()
articles_router.register('', Article_view_set, basename='articles')


urlpatterns = [
    url('', include(articles_router.urls)),
    
]


