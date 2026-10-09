"""ASGI configuration for cabanas project."""
import os
from django.core.asgi import get_asgi_application
from sistema_alojamientos.cabanas  import Cabana
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cabanas.settings')

application = get_asgi_application()
