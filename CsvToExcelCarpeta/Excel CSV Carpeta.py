# Autor: Mortanauta
# Versión: 1.1
# Web: https://elrincondemorta.wordpress.com/
# Github: https://github.com/Mortanauta/Public  
# Licencia: GPL 3.0 https://www.gnu.org/licenses/gpl-3.0.en.html



#Elementos necesarios para la ejecución del programa:
#pip install pandas
#pip install openpyxl


import os
import pandas as pd
import time
import platform

# --Corte aquí--8<-------------------------------------------------------------------
# Página principal

# Define colores
class Color:
    RESET = '\033[0m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    BOLD     = '\33[1m'
    GREY = '\033[90m'
    UNDERLINE = '\33[4m'
    

# Comprobar el sistema operativo
OS = platform.system()
OS_version = platform.release()

print(f"""
                                                                    {Color.GREY + 'By Mortanauta' + Color.RESET}
   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
   ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                        
                          ▬ CONVERSOR CSV <=> XLSX ▬            
      
    Este código permite convertir todos los archivos de una carpeta determinada
    de CSV a XLSX (y vicerversa).

    Valida que la carpeta exista, indica el núnero de archivos convertidos y 
    el tiempo que ha llevado la conversión.
           
    {Color.BOLD}{Color.BLUE + 'NOTA:' + Color.RESET} No convierte el formato.
    
    {Color.GREY + '● Author: Mortanauta' + Color.RESET} 
    {Color.GREY + '● Version: 1.10' + Color.RESET} 
    {Color.GREY + '● Website: https://elrincondemorta.wordpress.com/' + Color.RESET}
    {Color.GREY + '● Github: https://github.com/Mortanauta/Public' + Color.RESET}  
    {Color.GREY + '● License: GPL 3.0 https://www.gnu.org/licenses/gpl-3.0.en.html' + Color.RESET}

   ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ 
   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""")
# Imprimir comprobación del sistema operativo
input(f"""
    COMPROBANDO EL SISTEMA OPERATIVO
     └ Sistema operativo detectado: {OS} {OS_version}

      Presiona Enter para continuar...""")   

# Limpiar la pantalla
os.system("cls" if OS == "Windows" else "clear")
time.sleep(1)

# --Corte aquí--8<-------------------------------------------------------------------
# Programa principal

print(f"""\n                             CONVERSOR CSV <-> XLSX                          V:1.1\n

    |\\        ╔══════════════════════════════════════════════╗        
    |⁜\\       ║     ⸎     CONVERSOR CSV <-> XLSX             ║   ╔═╗ ╚═╝ ╔═╗ ╚═╝ ║
    |Morta    ║   Convierte archivos CSV a XLSX y viceversa  ║   ╚═╝ ╔═╗ ╚═╝ ╔═╗ ║ 
    |Nauta    ╚══════════════════════════════════════════════╝   \n 
            La conversión se realiza sobre {Color.BOLD}{Color.RED}{Color.UNDERLINE + 'TODOS' + Color.RESET} los archivos de la carpeta.   \n     """)

#Convierte archivos CSV a Excel XLSX
def csv_a_xlsx(ruta_carpeta, carpeta_salida):
    archivos_convertidos = 0
    inicio_tiempo = time.time()

    print("\nConvirtiendo archivos:")
    for archivo in os.listdir(ruta_carpeta):
        if archivo.endswith(".csv"):
            ruta_archivo = os.path.join(ruta_carpeta, archivo)
            nombre_archivo = os.path.splitext(archivo)[0] + ".xlsx"
            ruta_salida = os.path.join(carpeta_salida, nombre_archivo) if carpeta_salida else os.path.join(ruta_carpeta, nombre_archivo)

            df = pd.read_csv(ruta_archivo)
            df.to_excel(ruta_salida, index=False)
            
            archivos_convertidos += 1
            print(f"- Convirtiendo: {archivo}")

    tiempo_transcurrido = round(time.time() - inicio_tiempo, 2)
    print(f"\n    ---¡CONVERSIÓN COMPLETADA!--- 😎")
    print(f"    ► Archivos convertidos: {archivos_convertidos}")
    print(f"    ► Tiempo de proceso:    {tiempo_transcurrido} segundos")
    input("\n     (Pulse Enter para salir...)")

#Convierte archivos Excel XLS/XLSX a CSV
def xlsx_a_csv(ruta_carpeta, carpeta_salida):
    archivos_convertidos = 0
    inicio_tiempo = time.time()

    print("\nConvirtiendo archivos:")
    for archivo in os.listdir(ruta_carpeta):
        if archivo.endswith(".xls") or archivo.endswith(".xlsx"):
            ruta_archivo = os.path.join(ruta_carpeta, archivo)
            nombre_archivo = os.path.splitext(archivo)[0] + ".csv"
            ruta_salida = os.path.join(carpeta_salida, nombre_archivo) if carpeta_salida else os.path.join(ruta_carpeta, nombre_archivo)

            df = pd.read_excel(ruta_archivo)
            df.to_csv(ruta_salida, index=False)
            
            archivos_convertidos += 1
            print(f"- Convirtiendo: {archivo}")

    tiempo_transcurrido = round(time.time() - inicio_tiempo, 2)
    print(f"\n    ---¡CONVERSIÓN COMPLETADA!--- 😎 ")
    print(f"    ► Archivos convertidos: {archivos_convertidos}")
    print(f"    ► Tiempo de proceso:    {tiempo_transcurrido} segundos")
    input("\n     (Pulse Enter para salir...)")

#Programa principal
def validar_carpeta(ruta):
    return os.path.isdir(ruta)

if __name__ == "__main__":
    ruta_origen = input("      ► Ruta de la carpeta de origen: ")

    while not validar_carpeta(ruta_origen):
        print("      ERROR: La ruta de la carpeta de salida no es válida.")
        ruta_origen = input("      ► Ruta de la carpeta de origen: ")

    carpeta_salida = input("""      ► Ruta de la carpeta de salida 
        (Vacio, se utilizará la misma ruta que la carpeta de origen): """)

    if not carpeta_salida:
        carpeta_salida = ruta_origen
    else:
        while not validar_carpeta(carpeta_salida):
            print("      ERROR: La ruta de la carpeta de salida no es válida.")
            carpeta_salida = input("""      ► Ruta de la carpeta de salida 
        (Vacio, se utilizará la misma ruta que la carpeta de origen): """)
    
    print("""
        1. Convertir archivos CSV a Excel XLSX
        2. Convertir archivos Excel XLS/XLSX a CSV
    """)

    opcion = input("    Selecciona la opción (1/2): ")

    if opcion == '1':
        csv_a_xlsx(ruta_origen, carpeta_salida)
    elif opcion == '2':
        xlsx_a_csv(ruta_origen, carpeta_salida)
