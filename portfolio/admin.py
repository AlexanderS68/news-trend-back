from django.contrib import admin
from .models import StockWatchlist, ArticleWatchlist
# Register your models here.
admin.site.register(StockWatchlist)
admin.site.register(ArticleWatchlist)
