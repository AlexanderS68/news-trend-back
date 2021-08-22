from stocks.models import Stock
from rest_framework.routers import DefaultRouter
from .views import StockViewSet

app_name = "stocks"


stockRouter = DefaultRouter()
stockRouter.register('', StockViewSet.as_view())
