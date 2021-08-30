from rest_framework.permissions import AllowAny
from .serializers import Article_serializer, Category_serializer
from django.shortcuts import render
from .models import Article, Category
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


def fetchPayload():
    
    #This is for the categories
    sectorName = ['Energy', 'Finance', 'Material', 'Industrial', 'Utility', 'Healthcare', 'Consumer Discretionary', 'IT', 'Communication services', 'Real Estate']

    sectorCategories = [['04005000', '04005001', '06003000', '06001000','06006009', '04005010', '04005004', '04005004'],['04008004', '04019000', '04016017', '04000000', '04006000', '04008023', '04016019'],['04011000', '04012005', '04012002'], ['04015001', '03006000', '04011002'], ['06001000',
    '06006000','04005008','06005002','06010000','04005006','04005003','04005004', '04005005'], ['07013000', '07000000', '04002006', '14008000', '04002001'],['04007000', '04016055', '04008014', '13020000', '01000000'], ['04003000', '13000000', '13010000', '13017000'], ['01026002', '04003007', '04007009', '04010010'], ['04008022', '11016002', '04004002', '04001003']]

    #Placeholder for when article search is fleshed out. Similar to above
    #

    
    payload = {
        'title':'energy',
        'published_at_start':'NOW-1DAY',
        'categories_confident': 'True',
    }
    
    api_response_articles = api_instance.list_stories(**payload)

    for ix, articleReturn in enumerate(api_response_articles.stories):
            Article.objects.create(
                title = articleReturn.title,
                description = articleReturn.categories[0].label,
                content = articleReturn.body,
                url = articleReturn.source.home_page_url,
                publishedAt = articleReturn.published_at,
                sourceName = articleReturn.source.name,
                sentiment = articleReturn.sentiment.body.polarity)


    for i in range(10):
        opts = { 
        'categories_taxonomy':'iptc-subjectcode',
        'categories_id': sectorCategories[i],
        'published_at_start':'NOW-7DAYS/DAY',
        'published_at_end':'NOW',
        'categories_confident': True
        }
  
        # List time series      
        api_response = api_instance.list_time_series(**opts)            
        
        for idx, categoryDateSeries in enumerate(api_response.time_series):

            Category.objects.create(
                category_name = sectorName[i],
                count =  categoryDateSeries.count,
                published_at = categoryDateSeries.published_at,
            )

       
        
    
class Category_view_set(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Category_serializer
    permission_classes = [AllowAny]

    def get_queryset(self):  
        #Everytime this ran, it was twice       
        #fetchPayload()
        return Category.objects.all()

    def post(self, request,  format='json'):
        serializer = Category_serializer(data=request.data)
        if serializer.is_valid():          
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Article_view_set(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = Article_serializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        Article.objects.all().delete()
        Category.objects.all().delete()
        fetchPayload()
        return Article.objects.all()

    def post(self, request,  format='json'):
        serializer = Article_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)