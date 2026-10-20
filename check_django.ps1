# Ruta absoluta al proyecto
$projectPath = "C:\Users\carol\OneDrive\Desktop\sistema_alojamientos"

Write-Host "🔎 Diagnóstico Django en $projectPath"

# 1. Verificar si el servidor Uvicorn está corriendo
Write-Host "`n[1] Procesos en puerto 8000/8001/8002:"
netstat -ano | findstr :8000
netstat -ano | findstr :8001
netstat -ano | findstr :8002

# 2. Verificar carpeta templates
Write-Host "`n[2] Archivos en carpeta templates:"
Get-ChildItem "$projectPath\sistema_alojamientos\templates" -ErrorAction SilentlyContinue

# 3. Buscar configuración TEMPLATES en settings.py
Write-Host "`n[3] Configuración TEMPLATES en settings.py:"
Select-String -Path "$projectPath\sistema_alojamientos\settings.py" -Pattern "TEMPLATES"

# 4. Mostrar BASE_DIR en settings.py
Write-Host "`n[4] BASE_DIR en settings.py:"
Select-String -Path "$projectPath\sistema_alojamientos\settings.py" -Pattern "BASE_DIR"

Write-Host "`n✅ Diagnóstico completo. Revisa arriba si falta templates o si el puerto está ocupado."
# Ruta absoluta al proyecto
$projectPath = "C:\Users\carol\OneDrive\Desktop\sistema_alojamientos"

Write-Host "🚀 Test de renderizado Django"

# Activar entorno virtual
& "$projectPath\venv312\Scripts\Activate.ps1"

# 1. Verificar migraciones y errores de configuración
python "$projectPath\manage.py" check
python "$projectPath\manage.py" showmigrations

# 2. Probar levantar el servidor en modo debug
python "$projectPath\manage.py" runserver 127.0.0.1:8000

# 3. Opcional: probar directamente la vista raíz con curl
Write-Host "`n[3] Probando respuesta en /"
curl http://127.0.0.1:8000/
# Ruta absoluta al proyecto
$projectPath = "C:\Users\carol\OneDrive\Desktop\sistema_alojamientos"

Write-Host "🚀 Test de respuesta en /"

# Activar entorno virtual
& "$projectPath\venv312\Scripts\Activate.ps1"

# Levantar servidor en segundo plano
Start-Process powershell -ArgumentList "python `"$projectPath\manage.py`" runserver 127.0.0.1:8000" -NoNewWindow

# Esperar unos segundos
Start-Sleep -Seconds 5
# Ruta del proyecto
$projectPath = "C:\Users\carol\OneDrive\Desktop\sistema_alojamientos"

Write-Host "🔎 Analizando includes en urls.py dentro de $projectPath"

# Buscar todos los archivos urls.py
$urlsFiles = Get-ChildItem -Path $projectPath -Recurse -Filter "urls.py"

foreach ($file in $urlsFiles) {
    Write-Host "`n📂 Archivo:" $file.FullName
    # Mostrar las líneas que tengan 'include('
    Select-String -Path $file.FullName -Pattern "include"
}

# Guardar la respuesta de la raíz en un archivo
Invoke-WebRequest http://127.0.0.1:8000/ | Select-Object -ExpandProperty Content | Out-File "$projectPath\respuesta_root.html"

Write-Host "`n✅ Se guardó la respuesta en respuesta_root.html. Abrilo para ver qué HTML está devolviendo Django."
# Ruta del proyecto
$projectPath = "C:\Users\carol\OneDrive\Desktop\sistema_alojamientos"

Write-Host "🔎 Grafo de includes en urls.py dentro de $projectPath"

# Buscar todos los urls.py
$urlsFiles = Get-ChildItem -Path $projectPath -Recurse -Filter "urls.py"

foreach ($file in $urlsFiles) {
    $lines = Select-String -Path $file.FullName -Pattern "include"
    foreach ($line in $lines) {
        # Extraer el destino del include
        if ($line.Line -match 'include\("([^"]+)"\)') {
            $target = $matches[1]
            Write-Host "$($file.Name) --> $target"
        }
    }
}
# Ruta del proyecto
$projectPath = "C:\Users\carol\OneDrive\Desktop\sistema_alojamientos"

Write-Host "🔎 Detectando ciclos de includes en urls.py dentro de $projectPath"

# Buscar todos los urls.py
$urlsFiles = Get-ChildItem -Path $projectPath -Recurse -Filter "urls.py"

$edges = @()

foreach ($file in $urlsFiles) {
    $lines = Select-String -Path $file.FullName -Pattern "include"
    foreach ($line in $lines) {
        if ($line.Line -match 'include\("([^"]+)"\)') {
            $target = $matches[1]
            $edges += [PSCustomObject]@{Source=$file.Name; Target=$target}
        }
    }
}

# Mostrar todas las relaciones
$edges | ForEach-Object { Write-Host "$($_.Source) --> $($_.Target)" }

# Detectar ciclos simples (cuando una app incluye a sí misma)
$edges | Where-Object { $_.Source -like "*urls.py" -and $_.Target -like "*$($_.Source.Replace('.py',''))*" } |
    ForEach-Object { Write-Host "⚠️ Ciclo detectado: $($_.Source) incluye a $($_.Target)" -ForegroundColor Red }
    # Ruta del proyecto
    $projectPath = "C:\Users\carol\OneDrive\Desktop\sistema_alojamientos"
    
    Write-Host "🔎 Detectando ciclos de includes en urls.py dentro de $projectPath"
    
    # Buscar todos los urls.py
    $urlsFiles = Get-ChildItem -Path $projectPath -Recurse -Filter "urls.py"
    
    $edges = @()
    
    foreach ($file in $urlsFiles) {
        $lines = Select-String -Path $file.FullName -Pattern "include"
        foreach ($line in $lines) {
            if ($line.Line -match 'include\("([^"]+)"\)') {
                $target = $matches[1]
                $edges += [PSCustomObject]@{Source=$file.Name; Target=$target}
            }
        }
    }
    
    # Mostrar todas las relaciones
    $edges | ForEach-Object { Write-Host "$($_.Source) --> $($_.Target)" }
    
    # Detectar ciclos simples (cuando una app incluye a sí misma)
    $edges | Where-Object { $_.Source -like "*urls.py" -and $_.Target -like "*$($_.Source.Replace('.py',''))*" } |
        ForEach-Object { Write-Host "⚠️ Ciclo detectado: $($_.Source) incluye a $($_.Target)" -ForegroundColor Red }
        # Ruta del proyecto
        $projectPath = "C:\Users\carol\OneDrive\Desktop\sistema_alojamientos"
        
        Write-Host "🔎 Diagnóstico de templates Django en $projectPath"
        
        # 1. Listar todos los templates disponibles
        Write-Host "`n[1] Archivos en carpeta templates:"
        Get-ChildItem "$projectPath\sistema_alojamientos\templates" -ErrorAction SilentlyContinue
        
        # 2. Buscar si existe sistema_unificado.html (nombre correcto)
        Write-Host "`n[2] Verificar existencia de sistema_unificado.html:"
        Get-ChildItem "$projectPath\sistema_alojamientos\templates" -Filter "sistema_unificado.html" -ErrorAction SilentlyContinue
        
        # 3. Revisar si hay typos (archivos con 'unificad' en el nombre)
        Write-Host "`n[3] Archivos sospechosos con 'unificad' en el nombre:"
        Get-ChildItem "$projectPath\sistema_alojamientos\templates" | Where-Object { $_.Name -match "unificad" }
        
        # 4. Verificar que base.html tenga bloques content/title
        Write-Host "`n[4] Bloques en base.html:"
        Select-String -Path "$projectPath\sistema_alojamientos\templates\base.html" -Pattern "block"
        
        # 5. Revisar urls.py principal para ver si apunta a la vista sistema_unificado
        Write-Host "`n[5] urls.py principal:"
        Select-String -Path "$projectPath\sistema_alojamientos\urls.py" -Pattern "sistema_unificado"
        
        # 6. Revisar vista en alojamientos_app/views.py
        Write-Host "`n[6] Vista sistema_unificado en alojamientos_app/views.py:"
        Select-String -Path "$projectPath\alojamientos_app\views.py" -Pattern "sistema_unificado"
   