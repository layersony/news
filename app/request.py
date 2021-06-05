import urllib.request, json
from app.models import Article, Source

api_key = None
base_url = None

def configure_request(app):
  global base_url, category_url, api_key
  api_key = app.config['NEWS_API']
  base_url = app.config['BASE_URL']

def get_sources(sources):
  get_source_url = base_url.format(sources, api_key)

  try:
    with urllib.request.urlopen(get_source_url) as url:
      get_catergory_data = url.read()
      get_catergory_response = json.loads(get_catergory_data)

      news_data = None

      if get_catergory_response['sources']:
        news_list = get_catergory_response['sources']
        news_data = extractData(news_list)
    return news_data

  except urllib.error.URLError:
    print('Connection Reset by peer')

def extractData(newsList):

  news_list = []

  for news in newsList:
    id = news.get('id')
    name = news.get('name')
    desc = news.get('description')
    catergory = news.get('catergory')
    url = news.get('url')

    source_list = Source(id, name, desc, catergory, url)
    news_list.append(source_list)

  return news_list