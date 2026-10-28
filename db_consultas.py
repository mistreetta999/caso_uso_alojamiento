"""
Módulo centralizado para todas las consultas SQL del Sistema de Alojamientos.
"""
from db import ejecutar_consulta

# ==========================================
# 1. CONSULTAS DE CLIENTES
# ==========================================

def obtener_todos_los_clientes():
    """Retorna una lista con todos los clientes registrados."""
    cursor = ejecutar_consulta("SELECT * FROM clientes_cliente ORDER BY apellido, nombre;")
    return cursor.fetchall()


def insertar_cliente(nombre, apellido, dni, direccion, telefono):
    """Inserta un nuevo cliente en la base de datos."""
    query = """
        INSERT INTO clientes_cliente (nombre, apellido, dni, direccion, telefono) 
        VALUES (?, ?, ?, ?, ?);
    """
    ejecutar_consulta(query, (nombre, apellido, dni, direccion, telefono))


def buscar_cliente_por_dni(dni):
    """Busca un cliente específico por su número de DNI."""
    cursor = ejecutar_consulta("SELECT * FROM clientes_cliente WHERE dni = ?;", (dni,))
    return cursor.fetchone()


def eliminar_cliente(cliente_id):
    """Elimina un cliente según su ID."""
    ejecutar_consulta("DELETE FROM clientes_cliente WHERE id = ?;", (cliente_id,))


# ==========================================
# 2. CONSULTAS DE CABAÑAS
# ==========================================

def obtener_todas_las_cabanas():
    """Retorna todas las cabañas disponibles en el sistema."""
    cursor = ejecutar_consulta("SELECT * FROM cabanas_cabana;")
    return cursor.fetchall()


def insertar_cabana(nombre, capacidad, precio_por_noche, descripcion):
    """Registra una nueva cabaña."""
    query = """
        INSERT INTO cabanas_cabana (nombre, capacidad, precio_por_noche, descripcion) 
        VALUES (?, ?, ?, ?);
    """
    ejecutar_consulta(query, (nombre, capacidad, precio_por_noche, descripcion))


# ==========================================
# 3. CONSULTAS DE ALOJAMIENTOS
# ==========================================

def obtener_todos_los_alojamientos():
    """Retorna la lista general de alojamientos."""
    cursor = ejecutar_consulta("SELECT * FROM alojamientos_alojamiento;")
    return cursor.fetchall()


# ==========================================
# 4. CONSULTAS DE ALQUILERES (RESERVAS)
# ==========================================

def obtener_todos_los_alquileres():
    """Retorna todos los alquileres o reservas registradas."""
    cursor = ejecutar_consulta("SELECT * FROM alquileres_alquiler;")
    return cursor.fetchall()


def insertar_alquiler(cliente_id, cabana_id, fecha_inicio, fecha_fin, total):
    """Registra un nuevo alquiler vinculando cliente y cabaña."""
    query = """
        INSERT INTO alquileres_alquiler (cliente_id, cabana_id, fecha_inicio, fecha_fin, total) 
        VALUES (?, ?, ?, ?, ?);
    """
    ejecutar_consulta(query, (cliente_id, cabana_id, fecha_inicio, fecha_fin, total))
