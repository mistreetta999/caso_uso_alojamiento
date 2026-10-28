import os
from pathlib import Path
from dotenv import load_dotenv
import django

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Cargar variables de entorno desde .env
env_path = BASE_DIR / ".env"
load_dotenv(dotenv_path=env_path)

# Configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sistema_alojamientos.settings")

# Inicializar Django
django.setup()

# Ejemplo: acceder a una variable de entorno
SECRET_KEY = os.getenv("SECRET_KEY")

# Ejemplo: imprimir para verificar
if __name__ == "__main__":
    print("Bootstrap cargado correctamente")
    print("SECRET_KEY:", SECRET_KEY)
