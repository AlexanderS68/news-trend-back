from django.db import models

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
