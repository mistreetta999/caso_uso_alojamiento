from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from . import crud_central as c

ALIAS_APP = {
    "clientes": ["menu_clientes", "clientes_lista", "clientes-list", "clientes"],
    "reservas": ["menu_reservas", "reservas_lista", "reservas"],
    "cabanas": ["menu_cabanas", "cabanas_lista", "cabanas-list", "cabanas"],
    "alojamientos": ["menu_alojamientos", "alojamientos_lista",
                     "lista_alojamientos", "alojamientos"],
}

ALIAS_UNIFICADO = ["home", "index", "dashboard", "panel_central"]


def rutas_app(app):
    k = {"app": app}
    patrones = []

    for nombre in ("inicio", "index"):
        patrones.append(path("", c.inicio, k, name=nombre))

    for nombre in ("listar", "lista"):
        patrones.append(path("<str:modelo>/", c.listar, k, name=nombre))
    patrones.append(path("", c.inicio, k, name="lista"))

    for nombre in ("crear", "create", "nuevo"):
        patrones.append(path("<str:modelo>/nuevo/", c.crear, k, name=nombre))

    for nombre in ("editar", "update"):
        patrones.append(path("<str:modelo>/<int:pk>/editar/", c.editar, k, name=nombre))

    for nombre in ("eliminar", "delete"):
        patrones.append(path("<str:modelo>/<int:pk>/eliminar/", c.eliminar, k, name=nombre))

    return (patrones, app)


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", TemplateView.as_view(
        template_name="sitema_alojamientos/respuesta_root.html"),
        name="respuesta_root.html"),
    path("inicio/", TemplateView.as_view(template_name="inicio.html"),
         name="inicio.html"),

    path("sistema_unificado/", c.sistema_unificado, name="sistema_unificado"),
    path("ayuda/", c.ayuda, name="ayuda"),
    path("contacto/", c.contacto, name="contacto"),

    path("alojamientos/", include(rutas_app("alojamientos"))),
    path("cabanas/", include(rutas_app("cabanas"))),
    path("clientes/", include(rutas_app("clientes"))),
    path("reservas/", include(rutas_app("reservas"))),
]

for _nombre in ALIAS_UNIFICADO:
    urlpatterns.append(path("sistema_unificado/", c.sistema_unificado, name=_nombre))

for _app, _nombres in ALIAS_APP.items():
    for _nombre in _nombres:
        urlpatterns.append(path(_app + "/", c.inicio, {"app": _app}, name=_nombre))