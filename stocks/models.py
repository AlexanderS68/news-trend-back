from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Stock(models.Model):
    ticker = models.CharField(max_length=6)
    bid_price = models.DecimalField(decimal_places=2, max_digits=100000000)
    ask_price = models.DecimalField(decimal_places=2, max_digits=100000000)
    week_high_52 = models.DecimalField(decimal_places=2, max_digits=100000000)
    week_low_52 = models.DecimalField(decimal_places=2, max_digits=100000000)
    market_cap = models.IntegerField()
    volume = models.IntegerField()

    def __str__(self):
        return (f'{self.ticker}: ${self.bid_price}')