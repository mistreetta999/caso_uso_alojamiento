from django.apps import apps
from django.contrib import messages
from django.forms import modelform_factory
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

TPL = "sitema_alojamientos/crud/"

APPS = {
    "alojamientos": ["alojamientos_app", "alojamientos"],
    "cabanas": ["cabanas"],
    "clientes": ["clientes_app"],
    "reservas": ["reservas_app"],
}


def modelos_de(app):
    if app not in APPS:
        raise Http404("Aplicación inexistente")
    lista = []
    for label in APPS[app]:
        try:
            lista.extend(apps.get_app_config(label).get_models())
        except LookupError:
            continue
    return lista


def obtener_modelo(app, modelo):
    if app not in APPS:
        raise Http404("Aplicación inexistente")
    candidatos = [modelo, modelo.rstrip("s"), modelo[:-2]]
    for label in APPS[app]:
        for nombre in candidatos:
            try:
                return apps.get_model(label, nombre)
            except LookupError:
                continue
    raise Http404("Modelo inexistente: " + modelo)


def formulario_de(modelo_cls, *args, **kwargs):
    FormClase = modelform_factory(modelo_cls, fields="__all__")
    form = FormClase(*args, **kwargs)
    for campo in form.fields.values():
        if campo.widget.input_type != "checkbox":
            campo.widget.attrs.setdefault("class", "form-control")
    return form


def sistema_unificado(request):
    secciones = []
    for app in APPS:
        secciones.append({
            "app": app,
            "modelos": [
                {
                    "nombre": m._meta.model_name,
                    "plural": m._meta.verbose_name_plural,
                    "total": m.objects.count(),
                }
                for m in modelos_de(app)
            ],
        })
    return render(
        request,
        "sitema_alojamientos/sistema_alojamiento/sistema_unificado.html",
        {"secciones": secciones},
    )


def ayuda(request):
    return render(request, TPL + "pagina.html", {"titulo": "Ayuda"})


def contacto(request):
    return render(request, TPL + "pagina.html", {"titulo": "Contacto"})


def inicio(request, app):
    modelos = [
        {
            "nombre": m._meta.model_name,
            "plural": m._meta.verbose_name_plural,
            "total": m.objects.count(),
        }
        for m in modelos_de(app)
    ]
    return render(request, TPL + "inicio.html", {"app": app, "modelos": modelos})


def listar(request, app, modelo):
    Modelo = obtener_modelo(app, modelo)
    campos = Modelo._meta.fields
    filas = [
        {"obj": o, "valores": [getattr(o, f.name) for f in campos]}
        for o in Modelo.objects.all()
    ]
    return render(request, TPL + "listar.html", {
        "app": app,
        "modelo": modelo,
        "titulo": Modelo._meta.verbose_name_plural,
        "columnas": [f.verbose_name for f in campos],
        "filas": filas,
    })


def crear(request, app, modelo):
    Modelo = obtener_modelo(app, modelo)
    if request.method == "POST":
        form = formulario_de(Modelo, request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro creado.")
            return redirect(app + ":listar", modelo=modelo)
    else:
        form = formulario_de(Modelo)
    return render(request, TPL + "form.html", {
        "app": app, "modelo": modelo, "form": form,
        "titulo": "Nuevo " + str(Modelo._meta.verbose_name),
    })


def editar(request, app, modelo, pk):
    Modelo = obtener_modelo(app, modelo)
    obj = get_object_or_404(Modelo, pk=pk)
    if request.method == "POST":
        form = formulario_de(Modelo, request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro actualizado.")
            return redirect(app + ":listar", modelo=modelo)
    else:
        form = formulario_de(Modelo, instance=obj)
    return render(request, TPL + "form.html", {
        "app": app, "modelo": modelo, "form": form,
        "titulo": "Editar " + str(Modelo._meta.verbose_name),
    })


def eliminar(request, app, modelo, pk):
    Modelo = obtener_modelo(app, modelo)
    obj = get_object_or_404(Modelo, pk=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Registro eliminado.")
        return redirect(app + ":listar", modelo=modelo)
    return render(request, TPL + "eliminar.html", {
        "app": app, "modelo": modelo, "obj": obj,
    })