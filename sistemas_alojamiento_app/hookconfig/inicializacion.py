# sistemas_alojamiento_app/hookconfig/inicializacion.py

import os
import sys
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent.parent

APP_DIR = BASE_DIR / "sistemas_alojamiento_app"

SETTINGS_MODULE = "sistema_alojamientos.settings"

APPS_REQUERIDAS = [
    "sistemas_alojamiento_app.clientes_app",
    "sistemas_alojamiento_app.reservas_app",
    "sistemas_alojamiento_app.cabanas_app",
    "sistemas_alojamiento_app.alojamientos_app",
]

CARPETAS_REQUERIDAS = [
    BASE_DIR / "static",
    BASE_DIR / "staticfiles",
    BASE_DIR / "media",
    APP_DIR / "templates",
    APP_DIR / "templates" / "sitema_unificado",
]


def cargar_entorno():
    if str(BASE_DIR) not in sys.path:
        sys.path.insert(0, str(BASE_DIR))

    load_dotenv(BASE_DIR / ".env")

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_MODULE)

    return True


def iniciar_django():
    import django

    django.setup()

    return True


def crear_carpetas():
    creadas = []

    for carpeta in CARPETAS_REQUERIDAS:
        if not carpeta.exists():
            carpeta.mkdir(parents=True, exist_ok=True)
            creadas.append(str(carpeta))

    return creadas


def verificar_apps():
    from django.apps import apps
    from django.conf import settings

    faltantes = []

    for app in APPS_REQUERIDAS:
        if app not in settings.INSTALLED_APPS:
            faltantes.append(app)

    registradas = [config.name for config in apps.get_app_configs()]

    return {
        "faltantes_en_settings": faltantes,
        "registradas": registradas,
    }


def verificar_templates():
    from django.template.loader import get_template
    from django.template import TemplateDoesNotExist

    nombres = [
        "sitema_unificado/sitema_unificado.html",
        "sitema_unificado.html",
    ]

    for nombre in nombres:
        try:
            get_template(nombre)
            return nombre
        except TemplateDoesNotExist:
            continue

    return None


def aplicar_migraciones():
    from django.core.management import call_command

    call_command("makemigrations", interactive=False)
    call_command("migrate", interactive=False)

    return True


def recolectar_estaticos():
    from django.core.management import call_command

    call_command("collectstatic", interactive=False, verbosity=0)

    return True


def crear_superusuario():
    from django.contrib.auth import get_user_model

    usuario = os.getenv("ADMIN_USER")
    email = os.getenv("ADMIN_EMAIL", "")
    clave = os.getenv("ADMIN_PASSWORD")

    if not usuario or not clave:
        return "omitido: faltan ADMIN_USER / ADMIN_PASSWORD en .env"

    Usuario = get_user_model()

    if Usuario.objects.filter(username=usuario).exists():
        return "ya existe"

    Usuario.objects.create_superuser(
        username=usuario,
        email=email,
        password=clave,
    )

    return "creado"


def inicializar_sistema(migrar=True, estaticos=False):
    resultado = {}

    cargar_entorno()

    resultado["carpetas_creadas"] = crear_carpetas()

    iniciar_django()

    resultado["apps"] = verificar_apps()

    resultado["template_unificado"] = verificar_templates()

    if migrar:
        resultado["migraciones"] = aplicar_migraciones()

    if estaticos:
        resultado["estaticos"] = recolectar_estaticos()

    resultado["superusuario"] = crear_superusuario()

    return resultado


def mostrar_resultado(resultado):
    print("=" * 50)
    print("INICIALIZACIÓN DEL SISTEMA DE ALOJAMIENTOS")
    print("=" * 50)

    for clave, valor in resultado.items():
        print(f"{clave}: {valor}")

    print("=" * 50)


if __name__ == "__main__":
    argumentos = sys.argv[1:]

    resultado = inicializar_sistema(
        migrar="--sin-migrar" not in argumentos,
        estaticos="--estaticos" in argumentos,
    )

    mostrar_resultado(resultado)