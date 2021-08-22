from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('users/portfolio/', include('portfolio.urls', namespace='portfolio')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framwork')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
