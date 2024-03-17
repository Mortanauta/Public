# Autor: Mortanauta
# Versión: 1.10
# Web: https://elrincondemorta.wordpress.com/
# Github: https://github.com/Mortanauta/Public  
# Licencia: GPL 3.0 https://www.gnu.org/licenses/gpl-3.0.en.html

#Changelog:
#1.1 - Añadido temporizador y verbose de archivos convertidos 05/12/2023

#Elementos necesarios para la ejecución del programa:
#pip install python-docx
#pip install PyPDF2


import os
from PyPDF2 import PdfReader
from docx import Document
import time
import platform

# --Corte aquí--8<-------------------------------------------------------------------
# Página principal

# Define colores
class Color:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    GREY = '\033[90m'

# Comprobar el sistema operativo
OS = platform.system()
OS_version = platform.release()

print(f"""
                                                                    {Color.GREY +'by Mortanauta' + Color.RESET} 
   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
   ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                        
                        ▬ Conversor de PDF a Word/TXT ▬            
      
    Este código convierte archivos PDF a texto o Word de una forma rápida.

    Convierte todos los archivos PDF que encuentre en la carpeta especificada, 
    permitiendo seleccionar el formato de salida (TXT o DOCX).

    NOTA: El resultado puede variar en función de la codificación del PDF.    
        
    {Color.GREY + '● Autor: Mortanauta' + Color.RESET} 
    {Color.GREY + '● Versión: 1.32' + Color.RESET} 
    {Color.GREY + '● Sitio web: https://elrincondemorta.wordpress.com/' + Color.RESET}
    {Color.GREY + '● Github: https://github.com/Mortanauta/Public' + Color.RESET}  
    {Color.GREY + '● Licencia: GPL 3.0 https://www.gnu.org/licenses/gpl-3.0.en.html' + Color.RESET}
      
   ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ 
   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""")


# Imprimir comprobación del sistema operativo
input(f"""
    COMPROBANDO EL SISTEMA 
     └ Sistema operativo detectado: {OS} {OS_version}

      Presiona Enter para continuar...""")   

# Limpiar la pantalla
os.system("cls" if OS == "Windows" else "clear")
time.sleep(1)

# --Corte aquí--8<-------------------------------------------------------------------
# Página principal

def pdf_a_texto(ruta_pdf, ruta_salida, formato):
    if formato == 1:
        with open(ruta_pdf, 'rb') as archivo_pdf:
            lector = PdfReader(archivo_pdf)
            texto = ''
            for numero_pagina in range(len(lector.pages)):
                texto += lector.pages[numero_pagina].extract_text()

        with open(ruta_salida, 'w', encoding='utf-8') as archivo_salida:
            archivo_salida.write(texto)
    elif formato == 2:
        doc = Document()
        with open(ruta_pdf, 'rb') as archivo_pdf:
            lector = PdfReader(archivo_pdf)
            for numero_pagina in range(len(lector.pages)):
                texto = lector.pages[numero_pagina].extract_text()
                doc.add_paragraph(texto)

        doc.save(ruta_salida)

if __name__ == "__main__":
    print(f"""\n
                                                                            Version 1.1

    |\        ╔════════════════════════════════════════════════════╗             
    |⁜\       ║         📚  CONVERSOR PDF a Word/TXT               ║   ╔═╗ ╚═╝ ╔═╗ ╚═╝ ║
    |Morta    ║       Convierte los archivos PDF a texto           ║   ╚═╝ ╔═╗ ╚═╝ ╔═╗ ║   
    |Nauta    ╚════════════════════════════════════════════════════╝   \n """)             

    # Solicitar al usuario la ruta de la carpeta que contiene los archivos PDF
    carpeta_pdf = input("\n    ♦   Ingresa la ruta de la carpeta que contiene los archivos PDF: ")

    # Solicitar al usuario la ruta de la carpeta de salida para los archivos
    carpeta_texto = input("    ♦   Ingresa la ruta para la carpeta de salida de archivos\n        (si no ingresas, se utilizará la misma ruta que la carpeta de PDF): ")

    if not carpeta_texto:
        carpeta_texto = carpeta_pdf  # Si no se ingresa ruta, se utiliza la misma que la de PDF

# Solicitar al usuario el formato de salida
    while True:
        formato_salida = input("\n    ♦   Elige el formato de salida (1 para TXT, 2 para DOCX): ")
        if formato_salida in ['1', '2']:
            break
        else:
            print("        Por favor, ingresa 1 para TXT o 2 para DOCX.")

    # Contadores para archivos y tiempo de ejecución
    archivos_convertidos = 0
    inicio_tiempo = time.time()
    print("""
    Convirtiendo archivos:""")
# Convertir todos los archivos PDF a texto en la carpeta de salida
    for archivo in os.listdir(carpeta_pdf):
        if archivo.endswith(".pdf"):
            ruta_pdf = os.path.join(carpeta_pdf, archivo)
            nombre_archivo = os.path.splitext(archivo)[0]

            if formato_salida == '1':
                ruta_salida = os.path.join(carpeta_texto, nombre_archivo + ".txt")
            elif formato_salida == '2':
                ruta_salida = os.path.join(carpeta_texto, nombre_archivo + ".docx")

            pdf_a_texto(ruta_pdf, ruta_salida, int(formato_salida))
            archivos_convertidos += 1
            print(f"- Archivo convertido: {archivo}")

    tiempo_transcurrido = round(time.time() - inicio_tiempo, 2)

    print(f"\n    ---¡CONVERSIÓN COMPLETADA!--- :)")
    print(f"    ♦ Archivos convertidos: {archivos_convertidos}")
    print(f"    ♦ Tiempo de proceso:    {tiempo_transcurrido} segundos")
    input("\n     (Pulse Enter para salir...)")
