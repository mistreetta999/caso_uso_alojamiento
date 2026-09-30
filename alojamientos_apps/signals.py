from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Reserva

# Cuando se guarda una reserva nueva
@receiver(post_save, sender=Reserva)
def crear_log_reserva(sender, instance, created, **kwargs):
    if created:
        print(f"Reserva creada: {instance.id}")

# Cuando se elimina una reserva
@receiver(pre_delete, sender=Reserva)
def borrar_log_reserva(sender, instance, **kwargs):
    print(f"Reserva eliminada: {instance.id}")
