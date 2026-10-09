from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from sistema_alojamientos.alojamientos.models import Alojamiento
@admin.register(Alojamiento)
class AlojamientoAdmin(admin.ModelAdmin):
    """Admin personalizado para el modelo Alojamiento, mostrando botones CRUD."""
    # Añade el método a la lista de columnas visibles
    list_display = ('id', 'nombre', 'botones_crud_python')

    @admin.display(description="Acciones CRUD")
    def botones_crud_python(self, obj):
        # Python genera los enlaces de acción usando reversión de URLs de Django
        url_editar = reverse('admin:alojamientos_alojamiento_change', args=[obj.pk])
        url_eliminar = reverse('admin:alojamientos_alojamiento_delete', args=[obj.pk])
        
        return format_html(
            '<a class="button" href="{}">Editar</a> '
            '<a class="button" style="background:red;" href="{}">Borrar</a>',
            url_editar, url_eliminar
        )
    
