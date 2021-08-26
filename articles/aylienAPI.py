from __future__ import print_function
import time
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint
from rest_framework.decorators import api_view
from .models import Article

configuration = aylien_news_api.Configuration()
configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = '4e174919'
configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = '047069c3a217672289a4954b85f4b848'

client = aylien_news_api.ApiClient(configuration)
api_instance = aylien_news_api.DefaultApi(client)

def caching():
  pass

#look up cursor to get max 100+/pagination

def fetchPayload(requestKeyWord, requestStartDate, requestEndDate):
  try:
      api_response = api_instance.list_stories(
          title=f'{requestKeyWord}',
          published_at_start=f'{requestStartDate}',
          published_at_end=f'{requestEndDate}',
          per_page=10,
          sort_by='published_at'
      )
      for idx, article in enumerate(api_response.stories):
        Article.objects.create(
          title = article.title,
          description = article.categories[0].label, 
          content = article.body,
          url = article.source.home_page_url,
          publishedAt = article.published_at,
          sourceName = article.source.name,
          sentiment = article.sentiment.body.polarity)
          
        print(idx)
      
      
  except ApiException as e:
      print("Exception when calling DefaultApi->list_stories: %s\n" % e)

fetchPayload('energy','NOW-7DAYS','NOW-6DAYS')