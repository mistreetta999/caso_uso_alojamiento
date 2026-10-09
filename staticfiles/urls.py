from django.contrib import admin
    # include eliminado (evita bucle)
from sistema_alojamientos.views import InicioView, SistemaUnificadoView
from alojamientos_apps.views import lista_alojamientos

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", lista_alojamientos, name="lista_alojamientos"),
    path("inicio/", InicioView.as_view(), name="inicio"),
    path("sistema/", SistemaUnificadoView.as_view(), name="sistema_unificado"),

    # include eliminado (evita bucle)
    # include eliminado (evita bucle)
    # include eliminado (evita bucle)
    # include eliminado (evita bucle)
]
