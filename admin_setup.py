import importlib
from django.contrib import admin
from django.apps import apps

def auto_register_admin():
    """
    Recorre todas las apps del proyecto y registra automáticamente
    todos los modelos en el admin si no están registrados.
    """
    for app_config in apps.get_app_configs():
        try:
            # Importa el módulo admin de cada app si existe
            importlib.import_module(f"{app_config.name}.admin")
        except ModuleNotFoundError:
            pass  # Si la app no tiene admin.py, lo ignora

        # Registra todos los modelos de la app
        for model in app_config.get_models():
            try:
                admin.site.register(model)
            except admin.sites.AlreadyRegistered:
                pass  # Si ya está registrado, lo ignora
