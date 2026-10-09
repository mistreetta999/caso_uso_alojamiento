"""
Módulo de configuración de Bootstrap para alojamientos_apps
"""

from django.conf import settings

def bootstrap_context():
    """
    Devuelve las rutas de Bootstrap para usarlas en plantillas.
    Se puede registrar como context processor en settings.py.
    """
    return {
        "BOOTSTRAP_CSS": settings.STATIC_URL + "bootstrap/css/bootstrap.min.css",
        "BOOTSTRAP_JS": settings.STATIC_URL + "bootstrap/js/bootstrap.bundle.min.js",
    }
