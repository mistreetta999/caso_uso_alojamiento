"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    # Ajusta esta línea según la ubicación real de tu settings.py
    # Si tu settings.py está dentro de la carpeta del proyecto llamada "sistema_alojamientos"
    # entonces debe ser 'sistema_alojamientos.settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alojamientos.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. ¿Está instalado en tu entorno virtual?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
