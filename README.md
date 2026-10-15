# Sistema de Alojamientos

Proyecto Django para gestionar alojamientos, cabañas, clientes y reservas.

---

## 🚀 Creación del proyecto

```powershell
# Crear entorno virtual
python -m venv venv312
(Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& .\venv312\Scripts\Activate.ps1)

# Instalar dependencias
pip install django psycopg[binary]

# Crear proyecto base
django-admin startproject sistema_alojamientos .

# Crear aplicaciones
python manage.py startapp alojamientos_app
python manage.py startapp cabanas_app
python manage.py startapp clientes_app
python manage.py startapp reservas_app
