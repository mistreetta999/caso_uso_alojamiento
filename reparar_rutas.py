from pathlib import Path
import ast

BASE = Path.cwd()
APPS = {
    "clientes_app": "clientes",
    "reservas_app": "reservas",
    "cabanas_app": "cabanas",
    "alojamientos_app": "alojamientos",
}

def obtener_vista(app_dir, nombre):
    archivo = BASE / "sistemas_alojamiento_app" / app_dir / "views.py"

    if not archivo.exists():
        raise FileNotFoundError(str(archivo))

    texto = archivo.read_text(encoding="utf-8-sig")
    arbol = ast.parse(texto)

    funciones = [
        nodo.name
        for nodo in arbol.body
        if isinstance(nodo, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]

    if not funciones:
        raise RuntimeError(f"No hay funciones en {archivo}")

    preferencias = [
        f"{nombre}_views",
        f"{nombre}_view",
        f"{nombre}s_views",
        f"{nombre}s_view",
        f"{nombre}_app_view",
        f"{nombre}s_app_view",
    ]

    for funcion in preferencias:
        if funcion in funciones:
            return funcion

    coincidencias = [
        funcion
        for funcion in funciones
        if nombre in funcion.lower()
    ]

    if coincidencias:
        return coincidencias[0]

    return funciones[0]


for app_dir, nombre in APPS.items():
    vista = obtener_vista(app_dir, nombre)

    contenido = f'''from django.urls import path
from . import views

app_name = "{nombre}"

urlpatterns = [
    path("", views.{vista}, name="lista"),
]
'''

    destino = BASE / "sistemas_alojamiento_app" / app_dir / "urls.py"
    destino.write_text(contenido, encoding="utf-8")

    print(f"{destino}: views.{vista}")


urls_principal = '''from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "",
        TemplateView.as_view(
            template_name="sistema_alojamiento/sistema_unificado.html"
        ),
        name="inicio",
    ),

    path(
        "clientes/",
        include("sistemas_alojamiento_app.clientes_app.urls"),
    ),

    path(
        "reservas/",
        include("sistemas_alojamiento_app.reservas_app.urls"),
    ),

    path(
        "cabanas/",
        include("sistemas_alojamiento_app.cabanas_app.urls"),
    ),

    path(
        "alojamientos/",
        include("sistemas_alojamiento_app.alojamientos_app.urls"),
    ),
]
'''

destino_principal = BASE / "sistema_alojamientos" / "urls.py"
destino_principal.write_text(urls_principal, encoding="utf-8")

print(destino_principal)
