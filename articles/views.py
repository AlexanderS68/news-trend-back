from rest_framework.permissions import AllowAny
from .serializers import Article_serializer
from django.shortcuts import render
from .models import Article
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
import time
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint
from rest_framework.decorators import api_view


configuration = aylien_news_api.Configuration()
configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = '4e174919'
configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = '047069c3a217672289a4954b85f4b848'

client = aylien_news_api.ApiClient(configuration)
api_instance = aylien_news_api.DefaultApi(client)


def fetchPayload(requestKeyWord):
    # payload = {
    # 'categories_taxonomy':'iab-qag'
    # 'body':f'{category}',
    # 'published_at_start':'NOW-1DAY',
    # 'categories_confident': 'True',
    # 'cursor': '*'
    # }
    # listOf = []
    # print(listOf, 'init')
    # if payload['body'] not in listOf:
    #     api_response = api_instance.list_stories(**payload)
    #     for idx, article in enumerate(api_response.stories):
    #         Article.objects.create(
    #             title = article.title,
    #             description = article.categories[0].label, 
    #             content = article.body,
    #             url = article.source.home_page_url,
    #             publishedAt = article.published_at,
    #             sourceName = article.source.name,
    #             sentiment = article.sentiment.body.polarity)  
    #         print(type(api_response.stories.body))
    #     #listOf.append(api_response.stories.body) 
    #     print(listOf, 'middle') 
    #     #fetchPayload(api_response.stories.body)
    try:
        #In my defense my brain hurts to do the math logic and period doesn't work
        # for i in range(7):
            api_response1 = api_instance.list_stories(
            #title=f'{requestKeyWord}',
            categories_taxonomy='iptc-subjectcode',
            categories_id=['04005000'],
            published_at_start=f'NOW-7DAYS',
            language=['en'],
            per_page=10,
            sort_by='published_at'
            )

            api_response2 = api_instance.list_stories(
            #title=f'{requestKeyWord}',
            categories_taxonomy='iptc-subjectcode',
            categories_id=['04000000'],
            published_at_start=f'NOW-7DAYS',
            language=['en'],
            per_page=10,
            sort_by='published_at'
            )
            
            #response 1 is energy 2 finance
            for idx, article in enumerate(api_response1.stories):
                Article.objects.create(
                    title = article.title,
                    description = article.categories[0].label, 
                    content = article.body,
                    url = article.source.home_page_url,
                    publishedAt = article.published_at,
                    sourceName = article.source.name,
                    sentiment = article.sentiment.body.polarity)

            for idx, article in enumerate(api_response2.stories):
                Article.objects.create(
                    title = article.title,
                    description = article.categories[0].label, 
                    content = article.body,
                    url = article.source.home_page_url,
                    publishedAt = article.published_at,
                    sourceName = article.source.name,
                    sentiment = article.sentiment.body.polarity)

    except ApiException as e:
        print("Exception when calling DefaultApi->list_stories: %s\n" % e)
    
class Article_view_set(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = Article_serializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        fetchPayload('energy')
        return Article.objects.all()

    def post(self, request,  format='json'):
        serializer = Article_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

