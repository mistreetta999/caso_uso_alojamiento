import sqlite3
import os

# Ruta predeterminada de tu base de datos SQLite en el proyecto
DB_PATH = os.path.join(os.path.dirname(__file__), 'db.sqlite3')

def obtener_conexion():
    """
    Establece y retorna una conexión a la base de datos SQLite.
    Permite el manejo de filas como diccionarios para facilitar el acceso a los datos.
    """
    conexion = sqlite3.connect(DB_PATH)
    conexion.row_factory = sqlite3.Row
    return conexion

def inicializar_base_datos():
    """
    Verifica o crea las tablas básicas si no se gestionan mediante Django ORM,
    o sirve de apoyo para consultas directas.
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    # Ejemplo de tabla de control o respaldo si se requiere consulta directa
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS control_sistema (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            clave TEXT UNIQUE NOT NULL,
            valor TEXT
        )
    ''')
    
    conexion.commit()
    conexion.close()

if __name__ == "__main__":
    # Si ejecutas este archivo directamente, verifica la conexión
    try:
        conn = obtener_conexion()
        print("[ÉXITO] Conexión a la base de datos establecida correctamente.")
        conn.close()
    except Exception as e:
        print(f"[ERROR] No se pudo conectar a la base de datos: {e}")
