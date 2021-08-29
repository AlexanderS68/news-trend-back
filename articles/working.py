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

# params = {
#   'language': ['en'],
#   'title': 'startup',
#   'published_at_start': 'NOW-1HOUR',
#   'published_at_end': 'NOW',
#   'cursor': '*',
#   'sort_by': 'published_at'
# }

opts = { 
    'categories_taxonomy':'iptc-subjectcode',
    'categories_id':['04005000', '04005001', '04005001','06003000','06001000','06006009'],
    'published_at_start':'NOW-7DAYS/DAY',
    'published_at_end':'NOW',
}


def fetchPayload():
    try: 
        # List time series
        api_response = api_instance.list_time_series(**opts)
        #pprint(api_response)
    except ApiException as e:
        pprint("Exception when calling DefaultApi->list_time_series: %s\n" % e)


    for idx, categoryDateSeries in enumerate(api_response.time_series):

        Category.objects.create(
            category_name = "Energy",
            count =  categoryDateSeries.count,
            published_at = categoryDateSeries.published_at,
        )
    
class Category_view_set(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = Article_serializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        fetchPayload()
        return Category.objects.all()

    def post(self, request,  format='json'):
        serializer = Category_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Article_view_set(viewsets.ModelViewSet):

    serializer_class = Article_serializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        fetchPayload()
        return Article.objects.all()

    def post(self, request,  format='json'):
        serializer = Article_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)