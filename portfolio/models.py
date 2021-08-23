from django.contrib.auth.models import User
from django.db import models
from stocks.models import Stock
from django.contrib.auth.models import User
from articles.models import Article

# Create your models here.

class Stock_watchlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ManyToManyField(User)
    stock = models.ManyToManyField(Stock)

    def __str__(self):
        return f"{self.name}"

class Article_watchlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ManyToManyField(User)
    article = models.ManyToManyField(Article)

    def __str__(self):
        return f"{self.name}"