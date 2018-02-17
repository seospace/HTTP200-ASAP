import os

SECRET_KEY = 'SECRET'
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False
STATIC_ROOT = None

SERVER_NAME = os.environ.get('DOMAIN', 'yourdomain.tld')
