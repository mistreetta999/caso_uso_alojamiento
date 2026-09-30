from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
# Cuando se guarda una reserva nueva
@receiver(post_save, sender="alojamientos.Reserva")
def crear_log_reserva(sender, instance, created, **kwargs):
    """Crea un log cuando se guarda una nueva reserva."""
    if created:
        print(f"Reserva creada: {instance.id}")

# Cuando se elimina una reserva
@receiver(pre_delete, sender="alojamientos.Reserva")
def borrar_log_reserva(sender, instance, **kwargs):
    """Crea un log cuando se elimina una reserva."""
    print(f"Reserva eliminada: {instance.id}")
