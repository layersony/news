import os

class Config:
  BASE_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'
  NEWS_API = os.environ.get('NEWS_API')

class ProdConfig(Config):
  pass

class DevConfig(Config):
  DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
