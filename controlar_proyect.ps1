# Ruta base del proyecto
$basePath = "C:\Users\carol\OneDrive\Desktop\sistema_alojamientos"

# Carpetas a revisar
$folders = @("alojamientos", "cabanas", "clientes", "alquileres", "templates")

foreach ($folder in $folders) {
    Write-Host "=== Revisando carpeta: $folder ===" -ForegroundColor Cyan
    $path = Join-Path $basePath $folder
    
    if (Test-Path $path) {
        # Mostrar archivos y subcarpetas
        Get-ChildItem -Path $path -Recurse | Select-Object FullName
    } else {
        Write-Host "⚠️ La carpeta $folder NO existe en $basePath" -ForegroundColor Red
    }
    Write-Host ""
}
# Ruta base del proyecto
$basePath = "C:\Users\carol\OneDrive\Desktop\sistema_alojamientos"

# Carpetas de apps a revisar
$apps = @("alojamientos", "cabanas", "clientes", "alquileres")

foreach ($app in $apps) {
    Write-Host "=== Revisando app: $app ===" -ForegroundColor Cyan
    $path = Join-Path $basePath $app
    
    if (Test-Path $path) {
        $requiredFiles = @("apps.py", "models.py", "views.py", "urls.py")
        foreach ($file in $requiredFiles) {
            $filePath = Join-Path $path $file
            if (Test-Path $filePath) {
                Write-Host "✔️ $file encontrado" -ForegroundColor Green
            } else {
                Write-Host "❌ Falta $file en $app" -ForegroundColor Red
            }
        }
    } else {
        Write-Host "⚠️ La carpeta $app NO existe" -ForegroundColor Red
    }
    Write-Host ""
}
