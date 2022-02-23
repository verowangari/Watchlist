from distutils.debug import DEBUG
from inspect import Arguments


class Config:
    '''
    General configuration parent class
    '''
    pass
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
  