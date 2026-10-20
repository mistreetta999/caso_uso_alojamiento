"""Development settings for the project."""

# pylint: disable=wildcard-import
from .base import *
from .base import MIDDLEWARE
import os
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

SECRET_KEY = 'superseguro'
DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("POSTGRES_DB"),
        'USER': os.getenv("POSTGRES_USER"),
        'PASSWORD': os.getenv("POSTGRES_PASSWORD"),
        'HOST': os.getenv("POSTGRES_HOST", "localhost"),
        'PORT': os.getenv("POSTGRES_PORT", "5432"),
    }
}

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
