# start.ps1
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
& "$PSScriptRoot\venv312\Scripts\Activate.ps1"
python manage.py collectstatic --noinput
python manage.py runserver
Set-Content -Path "templates\sistema_unificado.html" -Value "<!DOCTYPE html><html><head><title>Sistema</title></head><body><h1>¡Funcionando!</h1></body></html>" -Encoding utf8