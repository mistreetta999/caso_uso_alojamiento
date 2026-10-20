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