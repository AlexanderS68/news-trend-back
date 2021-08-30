from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from .views import Blog_view_set

app_name = 'blogs'

blog_router = DefaultRouter()
blog_router.register('', Blog_view_set, basename='blogs')

urlpatterns = [
    url('', include(blog_router.urls))
]