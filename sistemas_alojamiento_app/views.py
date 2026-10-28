"""
Vistas unificadas generales del sistema.
Incluye los ViewSets de la API REST, las vistas basadas en clases
y las vistas basadas en funciones.
"""
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from rest_framework import viewsets



try:
    from alojamientos_app.forms import AlojamientoForm
    from alojamientos_app.models import Alojamiento
    from alojamientos_app.serializers import AlojamientoSerializer
except ImportError:
    Alojamiento = None
    AlojamientoForm = None
    AlojamientoSerializer = None


try:
    from cabanas_app.forms import CabanaForm
    from cabanas_app.models import Cabana
    from cabanas_app.serializers import CabanaSerializer
except ImportError:
    Cabana = None
    CabanaForm = None
    CabanaSerializer = None


try:
    from clientes_app.forms import ClienteForm
    from clientes_app.models import Cliente
    from clientes_app.serializers import ClienteSerializer
except ImportError:
    Cliente = None
    ClienteForm = None
    ClienteSerializer = None


try:
    from reservas_app.forms import ReservaForm
    from reservas_app.models import Reserva
    from reservas_app.serializers import ReservaSerializer
except ImportError:
    Reserva = None
    ReservaForm = None
    ReservaSerializer = None



if Alojamiento is not None and AlojamientoSerializer is not None:

    class AlojamientoViewSet(viewsets.ModelViewSet):
        queryset = Alojamiento.objects.all()
        serializer_class = AlojamientoSerializer


if Cabana is not None and CabanaSerializer is not None:

    class CabanaViewSet(viewsets.ModelViewSet):
        queryset = Cabana.objects.all()
        serializer_class = CabanaSerializer


if Cliente is not None and ClienteSerializer is not None:

    class ClienteViewSet(viewsets.ModelViewSet):
        queryset = Cliente.objects.all()
        serializer_class = ClienteSerializer


if Reserva is not None and ReservaSerializer is not None:

    class ReservaViewSet(viewsets.ModelViewSet):
        queryset = Reserva.objects.all()
        serializer_class = ReservaSerializer




class InicioView(TemplateView):
    template_name = "alojamientos_app/index.html"


class HomeView(TemplateView):
    template_name = "alojamientos_app/alojamientos_app.html"


class DashboardView(View):
    def get(
        self,
        request: HttpRequest,
    ) -> HttpResponse:
        return render(
            request,
            "global/global/dashboard.html",
        )


class SistemaUnificadoView(View):
    def get(
        self,
        request: HttpRequest,
    ) -> HttpResponse:
        return render(
            request,
            "sistema_unificado.html",
        )


if Alojamiento is not None:


    class AlojamientoDetailView(DetailView):
        model = Alojamiento
        template_name = "alojamientos_app/detalle_alojamiento.html"
        context_object_name = "alojamiento"
    
    class AlojamientoListView(ListView):
        model = Alojamiento
        template_name = (
            "alojamientos_app/alojamientos_app/"
            "lista_alojamientos.html"
        )
        context_object_name = "alojamientos"

    class AlojamientoCreateView(CreateView):
        model = Alojamiento
        form_class = AlojamientoForm
        template_name = "alojamientos_app/crear.html"
        success_url = reverse_lazy(
            "alojamientos_app:lista_alojamientos",
        )


    class AlojamientoUpdateView(UpdateView):
        model = Alojamiento
        form_class = AlojamientoForm
        template_name = "alojamientos_app/editar.html"
        success_url = reverse_lazy(
            "alojamientos_app:lista_alojamientos",
        )


    class AlojamientoDeleteView(DeleteView):
        model = Alojamiento
        template_name = "alojamientos_app/eliminar.html"
        success_url = reverse_lazy(
            "alojamientos_app:lista_alojamientos",
        )

if Cabana is not None:

    class CabanaListView(ListView):
        model = Cabana
        template_name = "cabanas_app/listar_cabanas.html"
        context_object_name = "cabanas"


    class CabanaDetailView(DetailView):
        model = Cabana
        template_name = "cabanas_app/detalle_cabana.html"
        context_object_name = "cabana"


    class CabanaCreateView(CreateView):
        model = Cabana
        form_class = CabanaForm
        template_name = "cabanas_app/crear_cabanas.html"
        success_url = reverse_lazy(
            "cabanas_app:lista_cabanas",
        )


    class CabanaUpdateView(UpdateView):
        model = Cabana
        form_class = CabanaForm
        template_name = "cabanas_app/editar_cabanas.html"
        success_url = reverse_lazy(
            "cabanas_app:lista_cabanas",
        )


    class CabanaDeleteView(DeleteView):
        model = Cabana
        template_name = "cabanas_app/eliminar_cabana.html"
        success_url = reverse_lazy(
            "cabanas_app:lista_cabanas",
        )




if Cliente is not None:

    class ClienteListView(ListView):
        model = Cliente
        template_name = "clientes_app/clientes_list.html"
        context_object_name = "clientes"


    class ClienteCreateView(CreateView):
        model = Cliente
        form_class = ClienteForm
        template_name = "clientes_app/crear_cliente.html"
        success_url = reverse_lazy(
            "clientes_app:lista",
        )


    
if Reserva is not None:

    class ReservaListView(ListView):
        model = Reserva
        template_name = "reservas_app/reservas_list.html"
        context_object_name = "reservas"


    class ReservaCreateView(CreateView):
        model = Reserva
        form_class = ReservaForm
        template_name = "reservas_app/crear.html"
        success_url = reverse_lazy(
            "reservas_app:lista",
        )

def sistema_unificado(
    request: HttpRequest,
) -> HttpResponse:
    return render(
        request,
        "sitema_unificado/sitema_unificado.html",
    )




def inicio(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "index.html",
    )


def crear_alojamiento(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        return redirect("dashboard")

    return render(
        request,
        "alojamientos_app/crear_alojamiento.html",
    )


def lista_alojamientos(request: HttpRequest) -> HttpResponse:
    alojamientos = []

    if Alojamiento is not None:
        alojamientos = Alojamiento.objects.all()

    return render(
        request,
        "alojamientos_app/lista_alojamientos.html",
        {
            "alojamientos": alojamientos,
        },
    )


def cabana_views_set(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "cabanas.html",
    )


def respuesta_root(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "clientes_app/base.html",
    )


def cliente_detalles(
    
    request: HttpRequest,
    cliente_id: int,
) -> HttpResponse:
    cliente = None

    if Cliente is not None:
        cliente = get_object_or_404(
            Cliente,
            pk=cliente_id,
        )

    return render(
        request,
        "clientes_app/detalle.html",
        {
            "cliente": cliente,
        },
    )


def ClienteUpdateView(
    request: HttpRequest,
    pk: int,
) -> HttpResponse:
    cliente = None

    if Cliente is not None:
        cliente = get_object_or_404(
            Cliente,
            pk=pk,
        )

    if request.method == "POST" and ClienteForm is not None:
        form = ClienteForm(
            request.POST,
            instance=cliente,
        )

        if form.is_valid():
            form.save()
            return redirect("clientes_app:lista")
    else:
        if ClienteForm is not None:
            form = ClienteForm(
                instance=cliente,
            )
        else:
            form = None

    return render(
        request,
        "clientes_app/editar.html",
        {
            "form": form,
            "cliente": cliente,
        },
    )


def ClienteDeleteView(
    request: HttpRequest,
    pk: int,
) -> HttpResponse:
    cliente = None

    if Cliente is not None:
        cliente = get_object_or_404(
            Cliente,
            pk=pk,
        )

    if request.method == "POST" and cliente is not None:
        cliente.delete()
        return redirect("clientes_app:lista")

    return render(
        request,
        "clientes_app/eliminar.html",
        {
            "cliente": cliente,
        },
    )
    
class RespuestaRootView(View):
    """
    Vista principal del sistema de alojamientos.
    """

    template_name = "respuesta_root.html"

    def get(self, request, *args, **kwargs):
        """Renderiza la página principal del sistema de alojamientos."""
        contexto = {
            "titulo": "Sistema de Alojamientos",
            "mensaje": "Bienvenido al sistema unificado de alojamientos.",
        }

        return render(
            request,
            self.template_name,
            contexto,
        )
