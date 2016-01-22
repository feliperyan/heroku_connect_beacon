import os


class Config(object):
    DEBUG = True
    TESTING = True
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class Development(Config):
	SQLALCHEMY_DATABASE_URI = 'localhost:5432'


class Production(Config):
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']