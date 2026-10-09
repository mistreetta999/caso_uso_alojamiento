"""
Módulo de conexión y gestión de base de datos para el sistema de alojamientos.
"""
import sqlite3
from pathlib import Path

# Ruta base del proyecto y archivo de la base de datos SQLite
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / 'db.sqlite3'


def obtener_conexion():
    """Establece y retorna una conexión directa con la base de datos SQLite."""
    conexion = sqlite3.connect(DB_PATH)
    # Permite acceder a las columnas por nombre (tipo diccionario)
    conexion.row_factory = sqlite3.Row
    return conexion


def ejecutar_consulta(query, parametros=()):
    """Ejecuta una consulta SQL de lectura o escritura de forma segura."""
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    try:
        cursor.execute(query, parametros)
        conexion.commit()
        return cursor
    except Exception as e:
        conexion.rollback()
        print(f"Error en la base de datos: {e}")
        raise e
    finally:
        conexion.close()
        
