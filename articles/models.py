from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.


class Article(models.Model):
    totalArticles = IntegerField()
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    url = models.URLField(blank=True)
    image = models.ImageField(blank=True)
    publishedAt = models.DateTimeField(blank=True)
    sourceName = models.CharField(max_length=100, blank=True)
    sentiment = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.title}"
