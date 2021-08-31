from django.db import models
from django.contrib.auth.models import User

class Coin(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100, blank=True, default='N/A')
    volume = models.CharField(max_length=100, blank=True, default='N/A')
    max_supply = models.CharField(max_length=100, blank=True, default='N/A')
    market_cap = models.CharField(max_length=100, blank=True, default='N/A')


    def __str__(self):
        return (f'{self.name}')