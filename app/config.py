from distutils.debug import DEBUG
from inspect import Arguments


class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'


class prodConfig(Config):
    '''
    Production configuration child class
       Args:
        Config: The parent configuration class with General configuration settings
    '''
    MOVIE_API_KEY = '088521cf5d91eb31d4bb90e4d992ac9d'


class DevConfig(Config):
    '''
    Development configuration child class
    Args:
     Config: The parent configuration class with General configurations settings
    '''
    DEBUG = True
