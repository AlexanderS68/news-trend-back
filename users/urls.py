from django.conf.urls import url, include
from .views import BlacklistTokenView, User_model_view_set
from rest_framework.routers import DefaultRouter



app_name = 'users'

user_router = DefaultRouter()
user_router.register('', User_model_view_set, basename='users')

urlpatterns = [
    url('',include(user_router.urls)),
    url('logout/blacklist/', BlacklistTokenView.as_view(), name='blacklist')
]
