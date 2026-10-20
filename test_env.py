import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url  # <-- Nueva librería para leer URLs de bases de datos
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env", override=True)

print("DB_ENGINE:", os.getenv("DB_ENGINE"))
print("DB_NAME:", os.getenv("DB_NAME"))
print("DB_USER:", os.getenv("DB_USER"))
print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))
print("DB_HOST:", os.getenv("DB_HOST"))
print("DB_PORT:", os.getenv("DB_PORT"))
