from django.contrib import admin
from .admin_setup import auto_register_admin

# Llama a la función que registra automáticamente todos los modelos
auto_register_admin()
