import os
from datetime import datetime, date
from functools import partial
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
dbdir = basedir.replace('api/config', 'db')

load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    DEBUG = False


class DevelopmentConfig(Config):
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DB_URL')
    # SQLALCHEMY_BINDS = = 'sqlite:///' + os.path.join(dbdir,  "docdb_"+str(datetime.date(datetime.now()))+'.db')
    DEBUG = True


class TestingConfig(Config):
    ENV = 'testing'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(dbdir,  "testdb_" +
                     str(datetime.date(datetime.now()))+'.db')
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DB_URL')
    DEBUG = False
    TESTING = False
    # SQLALCHEMY_BINDS = {'docdb':'sqlite:///' + os.path.join(dbdir,  "docdb_"+str(datetime.date(datetime.now()))+'.db')}
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(dbdir,  "docdb_"+str(datetime.date(datetime.now()))+'.db')

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
