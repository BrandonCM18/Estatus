import os
import time
import subprocess

# Nombre del proceso a monitorear (cambia esto por el nombre de tu aplicación)
APP_NAME = "Safari"

def esta_corriendo(nombre_proceso):
    """Revisa si el proceso está corriendo"""
    try:
        resultado = subprocess.check_output(["pgrep", "-x", nombre_proceso])
        return bool(resultado.strip())
    except subprocess.CalledProcessError:
        return False

def main():
    while True:
        if not esta_corriendo(APP_NAME):
            print(f"La aplicación {APP_NAME} no está en ejecución.")
        else:
            print(f"La aplicación {APP_NAME} está corriendo.")
        time.sleep(10)  # Revisa cada 10 segundos

if __name__ == "__main__":
    main()
