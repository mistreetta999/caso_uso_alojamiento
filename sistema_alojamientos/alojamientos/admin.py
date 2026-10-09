from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Alojamiento

@admin.register(Alojamiento)
class AlojamientoAdmin(admin.ModelAdmin):
    """Admin personalizado para el modelo Alojamiento, mostrando botones CRUD."""
    list_display = ('id', 'nombre', 'botones_crud_python')

    @admin.display(description="Acciones CRUD")
    def botones_crud_python(self, obj):
        """Genera los botones de acción CRUD (Editar y Borrar) para cada objeto."""
        url_editar = reverse('admin:alojamientos_alojamiento_change', args=[obj.pk])
        url_eliminar = reverse('admin:alojamientos_alojamiento_delete', args=[obj.pk])
        
        return format_html(
            '<a class="button" href="{}">Editar</a> '
            '<a class="button" style="background:red;" href="{}">Borrar</a>',
            url_editar, url_eliminar
        )
    
