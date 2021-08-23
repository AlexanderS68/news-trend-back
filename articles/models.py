from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Article(models.Model):
    totalArticles = IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()
    url = models.URLField()
    image = models.ImageField()
    publishedAt = models.DateTimeField()
    sourceName = models.CharField(max_length=100)
    sentiment = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}"