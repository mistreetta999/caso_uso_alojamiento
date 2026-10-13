import os
from pathlib import Path
from dotenv import load_dotenv
import psycopg2

# Base directory del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Cargar variables desde .env
load_dotenv(BASE_DIR / ".env", override=True)

def get_connection():
    """
    Devuelve una conexión psycopg2 a la base Postgres usando las variables del .env
    """
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME", "sistema_alojamientos"),
        user=os.getenv("DB_USER", "carolinam"),
        password=os.getenv("DB_PASSWORD", "superseguro"),
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=os.getenv("DB_PORT", "5432"),
    )

def test_connection():
    """
    Prueba rápida: abre conexión y ejecuta SELECT version()
    """
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT version();")
        print("Conectado a:", cur.fetchone())
        cur.close()
        conn.close()
    except Exception as e:
        print("Error de conexión:", e)
