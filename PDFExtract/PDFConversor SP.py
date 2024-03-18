import os
import time
import platform
from pdf2docx import Converter

# --Corte aquí--8<-------------------------------------------------------------------
# Página principal

# Definir colores
class Color:
    RESET = '\033[0m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    GREY = '\033[90m'

# Comprobar el sistema operativo
OS = platform.system()
OS_version = platform.release()

print(f"""
                                                                        {Color.GREY +'by Mortanauta' + Color.RESET} 
   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
   ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                        
                            ▬ Conversor de PDF a Word ▬            
      
    Este programa convierte un archivo PDF a Word, manteniendo las imágenes, la 
    estructura y el formato del archivo original.
    
    Para funcionar, inserta la ruta completa y el nombre del archivo original,
    por ejemplo: {Color.BLUE + 'C:/Documentos/articulo.pdf'+ Color.RESET}
    Y luego la ruta y el nombre del archivo de destino, si lo deja en blanco, 
    se procesará con la misma carpeta y el mismo nombre que el archivo original
    con formato Word.
    
    {Color.RED + 'Advertencia:  ' + Color.RESET}● Verifica el resultado, varía mucho dependiendo del formato
                    del PDF y su estructura. 
                  ● Este programa no es un OCR, por lo que no puede leer imágenes
                    de PDF escaneadas. 
    
    {Color.GREY + '● Autor: Mortanauta' + Color.RESET} 
    {Color.GREY + '● Versión: 1.1' + Color.RESET} 
    {Color.GREY + '● Sitio web: https://elrincondemorta.wordpress.com/' + Color.RESET}
    {Color.GREY + '● Github: https://github.com/Mortanauta/Public' + Color.RESET}  
    {Color.GREY + '● Licencia: GPL 3.0 https://www.gnu.org/licenses/gpl-3.0.en.html' + Color.RESET}
      
   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
   ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
""")

# Imprimir comprobación del sistema operativo
input(f"""
    COMPROBANDO EL SISTEMA 
     └ Sistema operativo detectado: {OS} {OS_version}

      Pulsa Enter para continuar...""")   

# Limpiar la pantalla
os.system("cls" if OS == "Windows" else "clear")
time.sleep(1)

# --Corte aquí--8<-------------------------------------------------------------------
# Programa Principal

print(f"""\n
                                                       Ver: 1.1
        |\       ╔══════════════════════════╗ 
        |⁜\      ║   Conversor PDF a Word   ║  ╔═╗ ╚═╝ ╔═╗ ╚═╝ ║
        |Morta   ║       con imágenes       ║  ╚═╝ ╔═╗ ╚═╝ ╔═╗ ║  
        |Nauta   ╚══════════════════════════╝ 
                                                                """) 

pdf_file = input("\n        ♦   Introduce la ruta completa y el nombre del archivo PDF: ")
print(f"""\n                   {Color.GREY +'(Dejad vacío para usar el mismo nombre y carpeta)'+Color.RESET}""")
docx_file = input("        ♦   Introduce la ruta completa y el nombre del archivo WORD DESTINO: ")

print(f"\n\nConvirtiendo PDF a Word... 🤖 \n")
# Comprobar si se proporcionó un nombre de archivo de salida
if not docx_file:
    # En caso de que no se haya proporcionado un nombre de archivo de salida, reutilizar el nombre del archivo PDF para el archivo de Word
    docx_file = pdf_file.replace(".pdf", ".docx")

# Conversión de PDF a Word  
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()

input("\nPulsa Enter para salir...")
