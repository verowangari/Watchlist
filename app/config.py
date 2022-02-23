from distutils.debug import DEBUG
from inspect import Arguments


class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
 
class prodConfig(Config):
    '''
    Production configuration child class
       Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass
class DevConfig(Config):
    '''
    Development configuration child class
    Args:
     Config: The parent configuration class with General configurations settings
    '''
    DEBUG=True
  