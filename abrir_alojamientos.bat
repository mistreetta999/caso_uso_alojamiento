@echo off
REM Activar entorno virtual y levantar Django con panel admin

cd /d C:\Users\carol\OneDrive\Desktop\sistema_alojamientos

REM Activar entorno virtual
call venv312\Scripts\activate.bat

REM Levantar servidor Django
start "" python manage.py runserver

REM Abrir navegador en el panel de administración
start "" http://127.0.0.1:8000/admin/

pause
#abrir con user =carol y palabra =superseguro