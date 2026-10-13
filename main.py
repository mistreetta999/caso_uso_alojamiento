import os
import sys
from django.core.management import execute_from_command_line

def main():
    """Configura y ejecuta el servidor Django en modo desarrollo."""
    # Configuración por defecto: entorno de desarrollo
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'sistema_alojamientos.settings.dev'
    )
    # Ejecuta el servidor Django
    execute_from_command_line(['manage.py', 'runserver'])

if __name__ == "__main__":
    main()
