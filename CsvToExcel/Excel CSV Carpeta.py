# Autor: Mortanauta
# Fecha: 01/12/2023
# Web: https://elrincondemorta.wordpress.com/
# Github: https://github.com/Mortanauta/Public  
# Licencia: GPL 3.0 https://www.gnu.org/licenses/gpl-3.0.en.html



#Elementos necesarios para la ejecución del programa:
#pip install pandas
#pip install openpyxl


import os
import pandas as pd
import time

print(f"""\n
\n                                                                          Version 1.0

      |\        ******************************************************          By: Mortanauta      
      | \       *           CONVERSOR CSV ˂-˃ XLSX                   *          https://elrincondemorta.wordpress.com/     
      | /       *     Convierte archivos CSV a XLSX y viceversa      *          https://github.com/Mortanauta/Public  
      |/        ******************************************************       
                                                                        """)

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
    print(f"\n    ---¡CONVERSIÓN COMPLETADA!--- :)")
    print(f"    • Archivos convertidos: {archivos_convertidos}")
    print(f"    • Tiempo de proceso:    {tiempo_transcurrido} segundos")
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
    print(f"\n    ---¡CONVERSIÓN COMPLETADA!--- :)")
    print(f"    • Archivos convertidos: {archivos_convertidos}")
    print(f"    • Tiempo de proceso:    {tiempo_transcurrido} segundos")
    input("\n     (Pulse Enter para salir...)")


#Programa principal
if __name__ == "__main__":
    ruta_origen = input("      • Ruta de la carpeta de origen: ")
    carpeta_salida = input("""      • Ruta de la carpeta de salida 
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

