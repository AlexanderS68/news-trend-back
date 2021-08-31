from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Stock(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=100)
    bidPrice = models.CharField(max_length=100, blank=True, default='N/A')
    totalVolume = models.CharField(max_length=100, blank=True, default='N/A')
    openPrice = models.CharField(max_length=100, blank=True, default='N/A')
    closePrice = models.CharField(max_length=100, blank=True, default='N/A')
    mark = models.CharField(max_length=100, blank=True, default='N/A')
    volatility = models.CharField(max_length=100, blank=True, default='N/A')
    peRatio = models.CharField(max_length=100, blank=True, default='N/A')
    divAmount = models.CharField(max_length=100, blank=True, default='N/A')
    divDate = models.CharField(max_length=100, blank=True, default='N/A')
    markPercentChangeInDouble = models.CharField(max_length=100, blank=True, default='N/A')

    def __str__(self):
        return (f'{self.name}')
