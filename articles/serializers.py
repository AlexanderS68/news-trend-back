from django.db.models import fields
from rest_framework import serializers
from .models import Article
from builtins import object


# class Article_serializer(serializers.ModelSerializer):

#     class Meta:
#         model = Article
#         fields = "__all__"

class ArticleSerializer(object):
    def __init__(self, title):
        self.title = title

    @property
    def articles(self):
        output = {'article':[]}

        for articles in self.body:
            articleAttributes = {
                'title': articles.title, 
                'description': articles.description, 
                'content':articles.content,
                'url': articles.url,
                'image': articles.image,
                'publishedAt': articles.publishedAt,
                'sourceName': articles.sourceName,
                'sentiment': articles.sentiment
            }
            output['product'].append(articleAttributes)
        return output

    @property
    def article_detail(self):
        return {
            'title': self.body.id,
            'description': self.body.description,
            'content': self.body.content,
            'url': self.body.url,
            'image': self.body.image,
            'publishedAt': self.body.publishedAt,
            'sourceName': self.body.sourceName,
            'sentiment': self.body.sentiment
        }