from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Stock(models.Model):
    ticker = models.TextField()
    bid_price = models.IntegerField()
    ask_price = models.IntegerField()
    week_high_52 = models.IntegerField()
    week_low_52 = models.IntegerField()
    market_cap = models.IntegerField()
    volume = models.IntegerField()

    def __str__(self) -> str:
        return (f'{self.ticker}: {self.bid_price}')