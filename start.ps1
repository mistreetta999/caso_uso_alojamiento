# start.ps1
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
& "$PSScriptRoot\venv312\Scripts\Activate.ps1"
python manage.py collectstatic --noinput
python manage.py runserver
