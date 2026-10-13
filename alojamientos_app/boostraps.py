""" Bootstraps""" 
# alojamientos_apps/boostraps.py
import django

import os
import sys

# Agregamos la carpeta raíz del proyecto al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configuramos el settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sistema_alojamientos.settings.dev")

django.setup()

print("Django inicializado correctamente desde boostraps.py")

