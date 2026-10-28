from pathlib import Path


HTML = r"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Lista de Alojamientos</title>

    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
        rel="stylesheet"
    >
</head>

<body class="bg-light">

<nav class="navbar navbar-dark bg-dark">
    <div class="container">
        <a
            href="/"
            class="navbar-brand"
        >
            Sistema de Alojamientos
        </a>

        <a
            href="/"
            class="btn btn-outline-light"
        >
            Inicio
        </a>
    </div>
</nav>

<main class="container py-5">

    <div class="d-flex justify-content-between align-items-center mb-4">
        <div>
            <h1 class="fw-bold mb-1">
                Alojamientos
            </h1>

            <p class="text-muted mb-0">
                Lista de alojamientos registrados.
            </p>
        </div>

        <a
            href="/alojamientos/nuevo/"
            class="btn btn-primary"
        >
            Nuevo alojamiento
        </a>
    </div>

    <div class="card shadow-sm">
        <div class="card-body">

            {% if alojamientos %}

                <div class="table-responsive">
                    <table class="table table-hover align-middle mb-0">

                        <thead class="table-dark">
                            <tr>
                                <th>ID</th>
                                <th>Alojamiento</th>
                                <th>Descripción</th>
                                <th class="text-end">
                                    Acciones
                                </th>
                            </tr>
                        </thead>

                        <tbody>
                            {% for alojamiento in alojamientos %}
                                <tr>
                                    <td>
                                        {{ alojamiento.id }}
                                    </td>

                                    <td>
                                        {{ alojamiento }}
                                    </td>

                                    <td>
                                        {{ alojamiento.descripcion|default:"Sin descripción" }}
                                    </td>

                                    <td class="text-end">
                                        <div class="btn-group">

                                            <a
                                                href="/alojamientos/{{ alojamiento.id }}/"
                                                class="btn btn-sm btn-outline-primary"
                                            >
                                                Ver
                                            </a>

                                            <a
                                                href="/alojamientos/{{ alojamiento.id }}/editar/"
                                                class="btn btn-sm btn-outline-warning"
                                            >
                                                Editar
                                            </a>

                                            <a
                                                href="/alojamientos/{{ alojamiento.id }}/eliminar/"
                                                class="btn btn-sm btn-outline-danger"
                                            >
                                                Eliminar
                                            </a>

                                        </div>
                                    </td>
                                </tr>
                            {% endfor %}
                        </tbody>

                    </table>
                </div>

            {% else %}

                <div class="text-center py-5">
                    <h2 class="h4">
                        No hay alojamientos registrados
                    </h2>

                    <p class="text-muted">
                        Todavía no existen alojamientos para mostrar.
                    </p>

                    <a
                        href="/alojamientos/nuevo/"
                        class="btn btn-primary"
                    >
                        Crear alojamiento
                    </a>
                </div>

            {% endif %}

        </div>
    </div>

</main>

</body>
</html>
"""


BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_DIR = BASE_DIR / "templates" / "alojamientos_app" / "alojamientos_app"
TEMPLATE_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT = TEMPLATE_DIR / "lista_alojamientos.html"
OUTPUT.write_text(HTML, encoding="utf-8")

print(f"Archivo creado: {OUTPUT}")
