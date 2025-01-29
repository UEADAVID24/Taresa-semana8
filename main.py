import os
import subprocess

def mostrar_codigo(ruta_script):
    """
    Muestra el contenido de un archivo Python dado su nombre.

    Parámetros:
        ruta_script (str): Ruta del archivo Python.

    Retorna:
        str: Contenido del archivo si se encuentra, de lo contrario, None.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("Error: El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    """
    Ejecuta un script de Python en una nueva ventana.

    Parámetros:
        ruta_script (str): Ruta del script a ejecutar.
    """
    try:
        if os.name == 'nt':  # Para Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Para sistemas basados en Unix
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Error al ejecutar el código: {e}")

def mostrar_menu():
    """
    Muestra el menú principal con opciones personalizadas.
    """
    ruta_base = os.path.dirname(__file__)  # Directorio base del script

    opciones = {
        '1': 'Gestión de Proyectos',
        '2': 'Reportes',
        '3': 'Configuración'
    }

    while True:
        print("\n--- Menú Principal - Dashboard ---")
        for key, value in opciones.items():
            print(f"{key} - {value}")
        print("0 - Salir")

        eleccion = input("Elige una opción o '0' para salir: ")
        if eleccion == '0':
            print("Saliendo del programa.")
            break
        elif eleccion in opciones:
            if eleccion == '1':
                mostrar_sub_menu(os.path.join(ruta_base, 'Proyectos'))
            elif eleccion == '2':
                mostrar_reportes()
            elif eleccion == '3':
                mostrar_configuracion()
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_sub_menu(ruta_proyectos):
    """
    Muestra el submenú de gestión de proyectos.

    Parámetros:
        ruta_proyectos (str): Ruta donde están los proyectos.
    """
    sub_carpetas = [f.name for f in os.scandir(ruta_proyectos) if f.is_dir()]

    while True:
        print("\n--- Gestión de Proyectos ---")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar")

        eleccion = input("Elige un proyecto o '0' para regresar: ")
        if eleccion == '0':
            break
        else:
            try:
                eleccion = int(eleccion) - 1
                if 0 <= eleccion < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_proyectos, sub_carpetas[eleccion]))
                else:
                    print("Error: Opción no válida.")
            except ValueError:
                print("Error: Entrada no válida.")

def mostrar_scripts(ruta_proyecto):
    """
    Muestra los scripts Python disponibles en la carpeta seleccionada.

    Parámetros:
        ruta_proyecto (str): Ruta del proyecto seleccionado.
    """
    scripts = [f.name for f in os.scandir(ruta_proyecto) if f.is_file() and f.name.endswith('.py')]

    while True:
        print("\n--- Scripts Disponibles ---")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar")

        eleccion = input("Elige un script o '0' para regresar: ")
        if eleccion == '0':
            break
        else:
            try:
                eleccion = int(eleccion) - 1
                if 0 <= eleccion < len(scripts):
                    ruta_script = os.path.join(ruta_proyecto, scripts[eleccion])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Ejecutar script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                else:
                    print("Error: Opción no válida.")
            except ValueError:
                print("Error: Entrada no válida.")

def mostrar_reportes():
    """
    Muestra una sección de reportes (en desarrollo).
    """
    print("\n--- Generación de Reportes ---")
    print("Funcionalidad en desarrollo. Próximamente más opciones.")

def mostrar_configuracion():
    """
    Muestra opciones de configuración (en desarrollo).
    """
    print("\n--- Configuración del Sistema ---")
    print("Funcionalidad en desarrollo. Agregaremos más opciones pronto.")

# Punto de entrada del programa
if __name__ == "__main__":
    mostrar_menu()
