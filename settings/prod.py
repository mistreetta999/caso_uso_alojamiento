import os
from pathlib import Path
from .base import *
DEBUG = True



BASE_DIR = Path(__file__).resolve().parent.parent
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.path.join(BASE_DIR, os.getenv('DB_NAME', 'db.sqlite3')),
    }
}