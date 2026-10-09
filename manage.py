#!/usr/bin/env python
"""Manage.py para sistema_alojamientos."""

import os
import sys

def main():
    """Punto de entrada para tareas administrativas de Django."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_alojamientos.settings')
    try:
        from django.core.management import execute_from_command_line  # pylint: disable=import-outside-toplevel
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. ¿Está instalado en este entorno?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
