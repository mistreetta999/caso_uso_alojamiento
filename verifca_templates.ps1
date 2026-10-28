# Script para verificar templates de Django
$rutaBase = "C:\Users\carol\OneDrive\Desktop\sistema_alojamientos"
Write-Host "🔍 Verificando estructura de templates en: $rutaBase" -ForegroundColor Cyan

Get-ChildItem -Path $rutaBase -Directory | ForEach-Object {
    $appFolder = $_.FullName
    $templatesFolder = Join-Path $appFolder "templates"
    
    if (Test-Path $templatesFolder) {
        Write-Host " [OK] Carpeta templates encontrada en: $($_.Name)" -ForegroundColor Green
        Get-ChildItem -Path $templatesFolder -Recurse -File | ForEach-Object {
            Write-Host "      📄 Archivo: $($_.Name)" -ForegroundColor Yellow
        }
    }
}

# Verificar carpeta templates global por si acaso
$globalTemplates = Join-Path $rutaBase "templates"
if (Test-Path $globalTemplates) {
    Write-Host "`n📁 Carpeta templates global encontrada en la raíz:" -ForegroundColor Green
    Get-ChildItem -Path $globalTemplates -Recurse -File | ForEach-Object {
        Write-Host "      📄 Archivo global: $($_.Name)" -ForegroundColor Yellow
    }
}
Get-ChildItem -Path $rutaBase -Recurse -File -Include *.html |
Where-Object { $_.Name -match "boots|desh|Sistema" } |
ForEach-Object {
    Write-Host "⚠️ Posible typo: $($_.FullName)" -ForegroundColor Red
}
Get-ChildItem -Path $rutaBase -Recurse -File -Include *.html |
Where-Object { $_.Name -match "boots|desh|Sistema" } |
ForEach-Object {
    Write-Host "⚠️ Posible typo: $($_.FullName)" -ForegroundColor Red
}
# Lista de nombres correctos que deberían usarse
$templatesCorrectos = @(
    "bootstrap.html",
    "dashboard.html",
    "editar_cabanas.html",
    "sistema_unificado.html"
)

# Buscar en todos los .py si se usan los nombres correctos
Get-ChildItem -Path $rutaBase -Recurse -Include *.py | ForEach-Object {
    $archivo = $_.FullName
    foreach ($tpl in $templatesCorrectos) {
        $coincidencias = Select-String -Path $archivo -Pattern $tpl -start
        if ($coincidencias) {
            Write-Host "✅ $tpl referenciado en: $archivo" -ForegroundColor Green
        }
    }
}

# Buscar si todavía hay referencias a nombres viejos
$templatesErroneos = @(
    "bootsstrap.html",
    "boostrap.html",
    "deshabord.html",
    "deshboard.html",
    "aditar_cabanas.html",
    "SistemaUnificado.html"
)

Get-ChildItem -Path $rutaBase -Recurse -Include *.py | ForEach-Object {
    $archivo = $_.FullName
    foreach ($tpl in $templatesErroneos) {
        $coincidencias = Select-String -Path $archivo -Pattern $tpl -start
        if ($coincidencias) {
            Write-Host "⚠️ Referencia a nombre viejo: $tpl en $archivo" -ForegroundColor Red
        }
    }
}
$reemplazos = @{
    "bootsstrap.html"      = "bootstrap.html"
    "boostrap.html"        = "bootstrap.html"
    "deshabord.html"       = "dashboard.html"
    "deshboard.html"       = "dashboard.html"
    "aditar_cabanas.html"  = "editar_cabanas.html"
    "SistemaUnificado.html"= "sistema_unificado.html"
}

Get-ChildItem -Path $rutaBase -Recurse -Include *.py | ForEach-Object {
    $archivo = $_.FullName
    $contenido = Get-Content $archivo
    foreach ($clave in $reemplazos.Keys) {
        $contenido = $contenido -replace $clave, $reemplazos[$clave]
    }
    $contenido | Set-Content $archivo
    Write-Host "🔄 Revisado: $archivo" -ForegroundColor Cyan
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
