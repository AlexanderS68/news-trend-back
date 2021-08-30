from django.db import models
from django.db.models.fields import IntegerField

class Article(models.Model):
    
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    url = models.TextField(blank=True)
    publishedAt = models.TextField(blank=True)
    sourceName = models.CharField(max_length=500, blank=True)
    sentiment = models.CharField(max_length=500, blank=True)


    
    def createArticle(self, title, description, content, url, publishedAt, sourceName, sentiment):
        self.title = title,
        self.description = description,
        self.content = content,
        self.url = url, 
        self.publishedAt = publishedAt, 
        self.sourceName = sourceName,
        self.sentiment = sentiment
        
        return Article

    def deleteArticle(self, title, description, content, url, publishedAt, sourceName, sentiment):
        self.title = title,
        self.description = description,
        self.content = content,
        self.url = url, 
        self.publishedAt = publishedAt, 
        self.sourceName = sourceName,
        self.sentiment = sentiment
    
    def __str__(self):
        return f"{self.title}"

class Category(models.Model):
    
    category_name= models.CharField(max_length=100, blank=True)
    count = models.CharField(max_length=100, blank=True)
    published_at = models.CharField(max_length=100, blank=True)
    
    def create(self, category_name, count, published_at):

        self.category_name= category_name
        self.count = count,
        self.published_at = published_at,

        return Category

    def deleteCategory(self, category_name, count, published_at):
        self.category_name = category_name
        self.count = count
        self.published_at = published_at

    def __str__(self):
        return f"{self.category_name}"

