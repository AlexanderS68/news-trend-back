from django.contrib import admin
from .models import Stock_watchlist, Article_watchlist
# Register your models here.
admin.site.register(Stock_watchlist)
admin.site.register(Article_watchlist)
