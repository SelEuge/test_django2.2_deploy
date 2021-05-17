from .base import *

DEBUG = True
# DEBUG = False

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*']

import dj_database_url
from decouple import config

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}
