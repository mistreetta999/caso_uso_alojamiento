import os
import sys
import subprocess

def main():
    # Asegurar que estamos en el directorio raíz del proyecto
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_alojamientos.settings')
    
    print("==================================================")
    print("🚀 Iniciando Sistema de Alojamientos (Modo Seguro)")
    print("==================================================")
    
    try:
        import django
        django.setup()
    except Exception as e:
        print(f"❌ Error al configurar Django: {e}")
        sys.exit(1)

    # 1. Verificar y aplicar migraciones automáticamente para evitar errores de BD
    print("\n📦 Verificando base de datos y migraciones...")
    subprocess.run([sys.executable, "manage.py", "makemigrations"])
    subprocess.run([sys.executable, "manage.py", "migrate"])

    # 2. Recopilar estáticos o verificar integridad
    print("\n🛠️ Verificando estado del proyecto...")
    result = subprocess.run([sys.executable, "manage.py", "check"])
    
    if result.returncode != 0:
        print("\n⚠️ Se encontraron advertencias o errores menores, pero intentaremos iniciar el servidor...")
    else:
        print("\n✅ ¡Proyecto verificado con éxito sin errores críticos!")

    # 3. Levantar el servidor de desarrollo en el puerto 8000
    print("\n🌐 Levantando servidor en: http://127.0.0.1:8000/")
    print("Presiona CTRL + C para detener el servidor.\n")
    print("==================================================\n")
    
    try:
        subprocess.run([sys.executable, "manage.py", "runserver"])
    except KeyboardInterrupt:
        print("\n\n🛑 Servidor detenido correctamente. ¡Hasta luego!")

if __name__ == '__main__':
    main()