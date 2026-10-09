# Activar entorno virtual
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
& "$PSScriptRoot\venv314\Scripts\Activate.ps1"

# Migraciones
python manage.py migrate

# Colectar estáticos
python manage.py collectstatic --noinput

# Levantar servidor (modo desarrollo)
python manage.py runserver 127.0.0.1:8000
