# config.py
class Config:
    DEBUG = True
    TAG = 'default'
    SECRET_KEY = 'default_key'
    MONGO_HOST = None
    MONGO_PORT = 27017
    MONGO_USER = 'admin'
    MONGO_PWD = '123456'
    MONGO_DB = 'admin'

class CiweiConfig(Config):
    TAG = 'ciwei'
    SECRET_KEY = 'ciwei_key'
    MONGO_HOST = '172.16.2.249'


class HomeConfig(Config):
    TAG = 'home'
    SECRET_KEY = 'hoem_key'


config = CiweiConfig
