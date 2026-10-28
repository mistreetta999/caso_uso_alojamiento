@echo off
REM Activar entorno virtual
call C:\Users\carol\OneDrive\Desktop\sistema_alojamientos\venv\Scripts\activate.bat

REM Ir al directorio del proyecto
cd C:\Users\carol\OneDrive\Desktop\sistema_alojamientos

REM Migraciones
python manage.py migrate

REM Levantar servidor Django en segundo plano
start "" python manage.py runserver 0.0.0.0:8000


REM Abrir navegador en la URL del servidor
start "" http://127.0.0.1:8000/

REM Abrir Visual Studio Code en el proyecto
start code .

pause
