import os

class Config:
    """
    General configuration parent class
    """
    NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey=bec8b1a4243742489712773bc99914a7'
    ALL_NEWS_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey=bec8b1a4243742489712773bc99914a7'

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