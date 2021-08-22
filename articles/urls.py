from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet

app_name = "articles"


articlesRouter = DefaultRouter()
articlesRouter.register('', ArticleViewSet.as_view())