import os

class Config:
    """
    General configuration parent class
    """
    NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey=72f6b6ddc8d045ba9d939d04e2679521'
    ALL_NEWS_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey=72f6b6ddc8d045ba9d939d04e2679521'

    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}