"""Admin configuration for the cabanas app."""
from django.contrib import admin
from .models import Cabana

# Register the Cabana model with the admin site for management through the Django admin interface.
admin.site.register(Cabana)
