from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Stock(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=100)
    bidPrice = models.CharField(max_length=100, blank=True)
    totalVolume = models.CharField(max_length=100, blank=True)
    openPrice = models.CharField(max_length=100, blank=True)
    closePrice = models.CharField(max_length=100, blank=True)
    mark = models.CharField(max_length=100, blank=True)
    volatility = models.CharField(max_length=100, blank=True)
    peRatio = models.CharField(max_length=100, blank=True)
    divAmount = models.CharField(max_length=100, blank=True)
    divDate = models.CharField(max_length=100, blank=True)
    markPercentChangeInDouble = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return (f'{self.name}')
