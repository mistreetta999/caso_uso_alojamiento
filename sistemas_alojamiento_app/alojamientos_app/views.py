# views.py (idéntico en clientes_app, reservas_app, cabanas_app, alojamientos_app)

from django.apps import apps
from django.contrib import messages
from django.db.models import Model
from django.forms import modelform_factory
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse


APP_NAME = __package__


def _modelos() -> dict[str, type[Model]]:
    for config in apps.get_app_configs():
        if config.name == APP_NAME:
            return {
                modelo.__name__.lower(): modelo
                for modelo in config.get_models()
            }
    return {}


def _modelo(nombre):
    modelo = _modelos().get(nombre)
    if modelo is None:
        raise Http404("Modelo no encontrado")
    return modelo


def _url(request, nombre, *args):
    namespace = request.resolver_match.namespace
    return reverse(f"{namespace}:{nombre}", args=args)


def inicio(request):
    modelos = [
        {
            "nombre": modelo.__name__.lower(),
            "titulo": modelo._meta.verbose_name_plural.capitalize(),
            "url": _url(request, "listar", modelo._meta.model_name),
            "url_crear": _url(request, "crear", modelo._meta.model_name),
        }
        for modelo in _modelos().values()
    ]
    return render(
        request,
        "sitema_unificado/crud_inicio.html",
        {"titulo": APP_NAME.split(".")[-1], "modelos": modelos},
    )


def listar(request, modelo):
    clase = _modelo(modelo)
    campos = list(getattr(clase, "_meta").concrete_fields)

    filas = [
        {
            "pk": objeto.pk,
            "valores": [getattr(objeto, campo.name) for campo in campos],
            "url_editar": _url(request, "editar", modelo, objeto.pk),
            "url_eliminar": _url(request, "eliminar", modelo, objeto.pk),
        }
        for objeto in clase.objects.all()
    ]

    return render(
        request,
        "sitema_unificado/crud_lista.html",
        {
            "titulo": getattr(clase, "_meta").verbose_name_plural.capitalize(),
            "columnas": [campo.verbose_name.capitalize() for campo in campos],
            "filas": filas,
            "url_crear": _url(request, "crear", modelo),
            "url_inicio": _url(request, "inicio"),
        },
    )


def crear(request, modelo):
    clase = _modelo(modelo)
    Formulario = modelform_factory(clase, fields="__all__")

    if request.method == "POST":
        formulario = Formulario(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro creado correctamente.")
            return redirect(_url(request, "listar", modelo))
    else:
        formulario = Formulario()

    return render(
        request,
        "sitema_unificado/crud_form.html",
        {
            "titulo": f"Nuevo - {clase._meta.verbose_name.capitalize()}",
            "formulario": formulario,
            "url_volver": _url(request, "listar", modelo),
        },
    )


def editar(request, modelo, pk):
    clase = _modelo(modelo)
    objeto = get_object_or_404(clase, pk=pk)
    Formulario = modelform_factory(clase, fields="__all__")

    if request.method == "POST":
        formulario = Formulario(request.POST, request.FILES, instance=objeto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro actualizado correctamente.")
            return redirect(_url(request, "listar", modelo))
    else:
        formulario = Formulario(instance=objeto)

    return render(
        request,
        "sitema_unificado/crud_form.html",
        {
            "titulo": f"Editar - {clase._meta.verbose_name.capitalize()}",
            "formulario": formulario,
            "url_volver": _url(request, "listar", modelo),
        },
    )


def eliminar(request, modelo, pk):
    clase = _modelo(modelo)
    objeto = get_object_or_404(clase, pk=pk)

    if request.method == "POST":
        objeto.delete()
        messages.success(request, "Registro eliminado correctamente.")
        return redirect(_url(request, "listar", modelo))

    return render(
        request,
        "sitema_unificado/crud_confirmar.html",
        {
            "titulo": f"Eliminar - {clase._meta.verbose_name.capitalize()}",
            "objeto": objeto,
            "url_volver": _url(request, "listar", modelo),
        },
    )