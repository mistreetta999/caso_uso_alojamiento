@echo off
REM Activar entorno virtual
call "%~dp0venv314\Scripts\activate.bat"

REM Levantar servidor con Uvicorn en puerto 8000
start cmd /k "uvicorn sistema_alojamientos.asgi:application --host 0.0.0.0 --port 8000"

REM Abrir navegador en la URL
start http://127.0.0.1:8000
