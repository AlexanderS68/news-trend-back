from django.db import models

# Create your models here.
class Article(models.Model):
    author = models.CharField(max_length=100)
    date_published = models.TextField()
    headline = models.TextField()