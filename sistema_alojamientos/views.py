"""Vistas principales del sistema de alojamientos."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from sistemas_alojamiento_app.reservas_app.forms import ReservaForm
from sistemas_alojamiento_app.reservas_app.models import Reserva


# ============================================================
# VISTA PRINCIPAL DEL SISTEMA UNIFICADO
# ============================================================

def sistema_unificado(
    request: HttpRequest,
) -> HttpResponse:
    """Vista principal o unificada del sistema."""

    return render(
        request,
        "sistema_unificado.html",
    )


class SistemaUnificadoView(View):
    """Vista basada en clase para el sistema unificado."""

    def get(
        self,
        request: HttpRequest,
    ) -> HttpResponse:
        """Muestra el panel principal del sistema."""

        html_content = """
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta
                name="viewport"
                content="width=device-width, initial-scale=1"
            >
            <title>Sistema Unificado de Alojamientos</title>

            <link
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
                rel="stylesheet"
            >
        </head>

        <body class="bg-light">
            <div class="container mt-5">
                <h1 class="text-center mb-5">
                    Sistema Unificado de Alojamientos
                </h1>

                <h2 class="text-center mt-4">
                    Bienvenido al Sistema
                </h2>

                <p class="lead text-center">
                    Panel principal operativo en red local.
                </p>

                <hr>

                <div class="row g-4 mt-4">
                    <div class="col-md-3">
                        <a
                            href="/clientes/lista/"
                            class="btn btn-primary w-100 p-3"
                        >
                            Clientes
                        </a>
                    </div>

                    <div class="col-md-3">
                        <a
                            href="/reservas/lista/"
                            class="btn btn-success w-100 p-3"
                        >
                            Reservas
                        </a>
                    </div>

                    <div class="col-md-3">
                        <a
                            href="/cabanas/lista/"
                            class="btn btn-warning w-100 p-3 text-dark"
                        >
                            Cabañas
                        </a>
                    </div>

                    <div class="col-md-3">
                        <a
                            href="/alojamientos/lista/"
                            class="btn btn-danger w-100 p-3"
                        >
                            Alojamientos
                        </a>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """

        return HttpResponse(html_content)


# ============================================================
# RESERVAS
# ============================================================

class CrearReservaView(View):
    """Permite crear una nueva reserva."""

    def get(
        self,
        request: HttpRequest,
    ) -> HttpResponse:
        """Muestra el formulario vacío."""

        form = ReservaForm()

        return render(
            request,
            "reserva_form.html",
            {
                "form": form,
            },
        )

    def post(
        self,
        request: HttpRequest,
    ) -> HttpResponse:
        """Procesa el formulario de creación de reserva."""

        form = ReservaForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("home")

        return render(
            request,
            "reserva_form.html",
            {
                "form": form,
            },
        )


# ============================================================
# VISTAS GENERALES
# ============================================================

class RespuestaRootView(View):
    """Vista de respuesta para la ruta raíz."""

    def get(
        self,
        request: HttpRequest,
    ) -> HttpResponse:
        """Muestra la página de inicio."""

        return render(
            request,
            "inicio.html",
        )


class DashboardView(View):
    """Muestra el panel de control."""

    def get(
        self,
        request: HttpRequest,
    ) -> HttpResponse:
        """Renderiza el dashboard."""

        return render(
            request,
            "dashboard.html",
        )


class InicioView(View):
    """Muestra la página de inicio."""

    def get(
        self,
        request: HttpRequest,
    ) -> HttpResponse:
        """Renderiza la página de inicio."""

        return render(
            request,
            "inicio.html",
        )


class AyudaView(View):
    """Muestra la página de ayuda."""

    def get(
        self,
        request: HttpRequest,
    ) -> HttpResponse:
        """Renderiza la página de ayuda."""

        return render(
            request,
            "ayuda.html",
        )


class ContactoView(View):
    """Muestra la página de contacto."""

    def get(
        self,
        request: HttpRequest,
    ) -> HttpResponse:
        """Renderiza la página de contacto."""

        return render(
            request,
            "contacto.html",
        )

class RespuestaRootView(View):
    """
    Vista principal del sistema de alojamientos.
    """

    template_name = "respuesta_root.html"

    def get(self, request, *args, **kwargs):
        contexto = {
            "titulo": "Sistema de Alojamientos",
            "mensaje": "Bienvenido al sistema unificado de alojamientos.",
        }

        return render(
            request,
            self.template_name,
            contexto,
        )
