from django.db import models

# Create your models here.


class Stock(models.Model):
    name = models.CharField(max_length=100)
    bidPrice = models.CharField(max_length=100)
    totalVolume = models.CharField(max_length=100, null=False)
    openPrice = models.CharField(max_length=100, null=True)
    closePrice = models.CharField(max_length=100, null=True)
    mark = models.CharField(max_length=100, null=True)
    volatility = models.CharField(max_length=100, null=True)
    peRatio = models.CharField(max_length=100, null=True)
    divAmount = models.CharField(max_length=100, null=True)
    divDate = models.CharField(max_length=100, null=True)
    markPercentChangeInDouble = models.CharField(max_length=100, null=True)

    def __str__(self):
        return (f'{self.name}')
