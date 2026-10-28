from django.contrib import admin

@admin.register(Alojamiento)
class AlojamientoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "ubicacion", "precio", "disponible")
    search_fields = ("nombre", "ubicacion")
    list_filter = ("disponible",)

