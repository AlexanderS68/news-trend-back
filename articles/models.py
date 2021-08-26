from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.


class Article(models.Model):
    
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    url = models.TextField(blank=True)
    publishedAt = models.TextField(blank=True)
    sourceName = models.CharField(max_length=100, blank=True)
    sentiment = models.CharField(max_length=50, blank=True)


    
    def create(self, title, description, content, url, publishedAt, sourceName, sentiment):
        self.title = title,
        self.description = description,
        self.content = content,
        self.url = url, 
        self.publishedAt = publishedAt, 
        self.sourceName = sourceName,
        self.sentiment = sentiment
       
        return Article

    
    def __str__(self):
        return f"{self.title}"
