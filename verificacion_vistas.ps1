# Ruta absoluta al proyecto
$projectPath = "C:\Users\carol\OneDrive\Desktop\sistema_alojamientos"

Write-Host "🔎 Listado de vistas y rutas Django en $projectPath"

# Activar entorno virtual
& "$projectPath\venv312\Scripts\Activate.ps1"

# 1. Mostrar todas las rutas registradas en el proyecto
Write-Host "`n[1] Rutas registradas en urls.py:"
python "$projectPath\manage.py" show_urls

# 2. Buscar todas las funciones def en views.py de cada app
Write-Host "`n[2] Funciones en views.py de cada app:"
Get-ChildItem "$projectPath" -Recurse -Filter views.py | ForEach-Object {
    Write-Host "`nArchivo:" $_.FullName
    Select-String -Path $_.FullName -Pattern "def "
}

# 3. Buscar todas las clases basadas en vistas
Write-Host "`n[3] Clases en views.py de cada app:"
Get-ChildItem "$projectPath" -Recurse -Filter views.py | ForEach-Object {
    Write-Host "`nArchivo:" $_.FullName
    Select-String -Path $_.FullName -Pattern "class "
}
