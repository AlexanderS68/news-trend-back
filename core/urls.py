from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('sector.urls', namespace='sectors')),
    path('api/stock/', include('stocks.urls', namespace='stocks')),
    path('api/articles/', include('articles.urls', namespace='articles')),
    path('api/watchlist/', include('watchlist.urls', namespace='watchlist')),
    path('api/portfolio/', include('portfolio.urls', namespace='portfolio')),
    path('api/users/', include('users.urls', namespace='users')),
    path('api-auth/', include('rest_Framework.urls', namespace='rest_framwork')),
    path('api/token', TokenObtainPairView.asview(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), namespace='token_refresh'),
]
