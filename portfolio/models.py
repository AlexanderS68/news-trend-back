from django.contrib.auth.models import User
from django.db import models
from django.db.models.aggregates import Max
from stocks.models import Stock



# Create your models here.


# class Stock_watchlist(models.Model):
#     name = models.CharField(max_length=100)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     stocks = models.ManyToManyField(Stock)

#     def __str__(self):
#         return f"{self.name}"


class Article_watchlist(models.Model):
    user = models.ManyToManyField(User)
    publishedAt = models.CharField(max_length=300, null=True)
    author = models.CharField(max_length=300, null=True)
    url = models.CharField(max_length=300, null=True)
    title = models.CharField(max_length=300, null=True)
    urlToImage = models.CharField(max_length=300, null=True)

    def __str__(self):
        return f"{self.title}"
