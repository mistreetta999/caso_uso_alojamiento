"""
Configuración principal del proyecto de Django para el sistema de alojamientos.
"""
from pathlib import Path

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta (solo para desarrollo)
SECRET_KEY = 'django-insecure-clave-de-desarrollo-alquileres-cabanas'

# Modo debug (True en desarrollo, False en producción)
DEBUG = True

# Hosts permitidos
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Librerías externas
    'django_extensions',
    'crispy_forms',
    'crispy_bootstrap5',

    # Tus aplicaciones
    'alojamientos',
    'cabanas',
    'clientes',
    'alquileres',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de URLs y WSGI/ASGI
ROOT_URLCONF = 'alojamientos.urls'

WSGI_APPLICATION = 'alojamientos.wsgi.application'
ASGI_APPLICATION = 'alojamientos.asgi.application'

# Configuración de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # carpeta templates en la raíz
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Base de datos (SQLite por defecto)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validadores de contraseña
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Configuración regional
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/Argentina/Buenos_Aires'
USE_I18N = True
USE_TZ = True

# Archivos estáticos y media
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Configuración de crispy forms con Bootstrap 5
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Campo por defecto para IDs
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
