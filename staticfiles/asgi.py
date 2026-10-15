"""
ASGI config para el módulo static.

Expone la aplicación ASGI como una variable llamada `application`.
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_alojamientos.settings')

application = get_asgi_application()
