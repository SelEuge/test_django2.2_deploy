"""
WSGI config for test_bigbox project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_bigbox.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_bigbox.settings.local')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_bigbox.settings.production')
# La sig línea sirve entorno local
#application = get_wsgi_application()

# Cambiamos la línea anterior para usar en produc, soluciona problema de archivos estáticos
from dj_static import Cling

application = Cling(get_wsgi_application())
