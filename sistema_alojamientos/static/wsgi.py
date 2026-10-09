"""
WSGI config para el módulo static.

Expone la aplicación WSGI como una variable llamada `application`.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_alojamientos.settings')

application = get_wsgi_application()
