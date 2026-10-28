import os
import sys
import subprocess

def ejecutar_comando(comando, mensaje):
    print(f"\n[INFO] {mensaje}...")
    resultado = subprocess.run(comando, shell=True)
    if resultado.returncode != 0:
        print(f"[ADVERTENCIA] Hubo un detalle al {mensaje.lower()}, pero continuaremos.")

def main():
    print("==================================================")
    print("      INICIADOR AUTOMÁTICO - SISTEMA DE ALOJAMIENTOS")
    print("==================================================")
    
    # 1. Verificar si estamos en la raíz del proyecto
    if not os.path.exists("manage.py"):
        print("[ERROR] No se encuentra el archivo 'manage.py'. Asegúrate de ejecutar este script desde la raíz del proyecto.")
        sys.exit(1)

    # 2. Aplicar migraciones automáticamente por si hay cambios pendientes
    ejecutar_comando("python manage.py makemigrations", "Verificando cambios en los modelos")
    ejecutar_comando("python manage.py migrate", "Aplicando migraciones a la base de datos")

    # 3. Recopilar archivos estáticos (opcional pero previene errores)
    ejecutar_comando("python manage.py collectstatic --noinput", "Organizando archivos estáticos")

    print("\n--------------------------------------------------")
    print("🚀 ¡Todo listo! Iniciando el servidor local...")
    print("🌐 Abre tu navegador en: http://127.0.0.1:8000/")
    print("🛑 Para detener el servidor, presiona las teclas Ctrl + C")
    print("--------------------------------------------------\n")

    # 4. Iniciar el servidor de desarrollo de Django sin interrupciones
    try:
        subprocess.run("python manage.py runserver", shell=True)
    except KeyboardInterrupt:
        print("\n\n[INFO] Servidor detenido correctamente. ¡Hasta luego!")

if __name__ == "__main__":
    main()
