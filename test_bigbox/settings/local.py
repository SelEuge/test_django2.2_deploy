from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bigbox',
        'USER': 'postgres',
        'PASSWORD': 'bigbox',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
