from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('articles/', include('articles.urls', namespace='articles')),
    path('stocks/', include('stocks.urls', namespace='stocks')),
    path('portfolio/', include('portfolio.urls')),
    path('category/', include('category.urls')),
    path('blog/', include('blog.urls')),
    path('coin/', include('coins.urls')),
    

    path('api-auth/', include('rest_framework.urls', namespace='rest_framwork')),

]
