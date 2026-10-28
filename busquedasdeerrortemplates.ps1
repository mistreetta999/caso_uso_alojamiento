$codigo = @'
import os, re, traceback
from pathlib import Path
from django.conf import settings
from django.template import engines
from django.template.loader import get_template
from django.urls import reverse, NoReverseMatch
from django.contrib.staticfiles import finders

base = Path(settings.BASE_DIR)
excluir = {"venv", "staticfiles", ".git", "__pycache__", "node_modules"}
motor = engines["django"]

rx_url = re.compile(r"\{%\s*url\s+['\"]([^'\"]+)['\"]")
rx_static = re.compile(r"\{%\s*static\s+['\"]([^'\"]+)['\"]")
rx_ref = re.compile(r"\{%\s*(?:extends|include)\s+['\"]([^'\"]+)['\"]")

errores = []
revisados = 0

for raiz, dirs, archivos in os.walk(base):
    dirs[:] = [d for d in dirs if d not in excluir]
    for nombre in archivos:
        if not nombre.endswith(".html"):
            continue
        ruta = Path(raiz) / nombre
        rel = ruta.relative_to(base)
        revisados += 1
        try:
            texto = ruta.read_text(encoding="utf-8")
        except Exception as e:
            errores.append((rel, 0, "No se puede leer (codificacion): " + str(e)))
            continue

        # 1) Sintaxis de la plantilla
        try:
            motor.from_string(texto)
        except Exception as e:
            linea = 0
            try:
                linea = e.template_debug["line"]
            except Exception:
                pass
            errores.append((rel, linea, "SINTAXIS: " + str(e).splitlines()[0]))

        for n, linea_txt in enumerate(texto.splitlines(), start=1):
            # 2) extends / include
            for ref in rx_ref.findall(linea_txt):
                try:
                    get_template(ref)
                except Exception as e:
                    errores.append((rel, n, "PLANTILLA NO ENCONTRADA: " + ref))

            # 3) nombres de url
            for nombre_url in rx_url.findall(linea_txt):
                try:
                    reverse(nombre_url)
                except NoReverseMatch as e:
                    if "is not a valid view function or pattern name" in str(e):
                        errores.append((rel, n, "URL INEXISTENTE: " + nombre_url))
                except Exception as e:
                    errores.append((rel, n, "URL ERROR (" + nombre_url + "): " + str(e)))

            # 4) archivos estaticos
            for est in rx_static.findall(linea_txt):
                if not finders.find(est):
                    errores.append((rel, n, "STATIC NO ENCONTRADO: " + est))

print("Plantillas revisadas:", revisados)
print("Problemas encontrados:", len(errores))
print("-" * 70)
for rel, n, msg in sorted(errores, key=lambda x: (str(x[0]), x[1])):
    print(str(rel) + " | linea " + str(n) + " | " + msg)

print("-" * 70)
print("Prueba de la pagina principal /")
from django.test import Client
c = Client(raise_request_exception=True, SERVER_NAME="127.0.0.1")
try:
    r = c.get("/")
    print("Estado HTTP:", r.status_code)
except Exception:
    print(traceback.format_exc())
'@

python manage.py shell -c $codigo