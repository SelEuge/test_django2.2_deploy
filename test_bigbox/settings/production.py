from .base import *

DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ['bigboxselene.herokuapp.com']

import dj_database_url
from decouple import config

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

STATICFILES_DIRS = (BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')