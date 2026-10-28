# Ruta absoluta al proyecto
$projectPath = "C:\Users\carol\OneDrive\Desktop\sistema_alojamientos"

Write-Host "🔎 Listado de vistas y rutas Django en $projectPath"

# Activar entorno virtual
& "$projectPath\venv\Scripts\Activate.ps1"

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
# 1. Correcciones de nombres de archivos
$correcciones = @{
    "bootsstrap.html"      = "bootstrap.html"
    "boostrap.html"        = "bootstrap.html"
    "deshabord.html"       = "dashboard.html"
    "deshboard.html"       = "dashboard.html"
    "aditar_cabanas.html"  = "editar_cabanas.html"
    "SistemaUnificado.html"= "sistema_unificado.html"
}

Get-ChildItem -Path $rutaBase -Recurse -File -Include *.html | ForEach-Object {
    if ($correcciones.ContainsKey($_.Name)) {
        $nuevoNombre = $correcciones[$_.Name]
        Rename-Item -Path $_.FullName -NewName $nuevoNombre -Force
        Write-Host "🔄 Archivo renombrado: $($_.Name) → $nuevoNombre" -ForegroundColor Cyan
    }
}

# 2. Reemplazo en código .py
Get-ChildItem -Path $rutaBase -Recurse -Include *.py | ForEach-Object {
    $contenido = Get-Content $_.FullName
    foreach ($clave in $correcciones.Keys) {
        $contenido = $contenido -replace $clave, $correcciones[$clave]
    }
    $contenido | Set-Content $_.FullName
    Write-Host "📝 Revisado: $($_.FullName)" -ForegroundColor Yellow
}

# 3. Validación final
$templatesCorrectos = $correcciones.Values | Select-Object -Unique
Get-ChildItem -Path $rutaBase -Recurse -Include *.py | ForEach-Object {
    foreach ($tpl in $templatesCorrectos) {
        if (Select-String -Path $_.FullName -Pattern $tpl -start) {
            Write-Host "✅ $tpl referenciado en: $($_.FullName)" -ForegroundColor Green
        }
    }
}
Get-ChildItem -Path $rutaBase -Recurse -Include *.html |
Group-Object Name | Where-Object { $_.Count -gt 1 } |
ForEach-Object {
    Write-Host "📂 Template duplicado: $($_.Name)" -ForegroundColor Cyan
    $_.Group | ForEach-Object {
        Write-Host "   ↳ $($_.FullName)" -ForegroundColor Yellow
    }
}
