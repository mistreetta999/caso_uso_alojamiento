import os
import django
from django.conf import settings
from django.db import connection

# Inicializar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sistema_alojamientos.settings.dev")
django.setup()

print("⚡ Settings cargados desde:", os.environ.get("DJANGO_SETTINGS_MODULE"))
print("⚡ Base de datos configurada:", settings.DATABASES['default'])

# Probar conexión a la base de datos vía Django
try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1;")
        print("✅ Django se conectó correctamente a Postgres")
except Exception as e:
    print("❌ Error de conexión desde Django:", e)

