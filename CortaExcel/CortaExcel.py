import pandas as pd
import os
import time
import platform

# Define colores
class Color:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    GREY = '\033[90m'

# Comprobar el sistema operativo
OS = platform.system()
OS_version = platform.release()

print(f"""
                                                                        {Color.GREY +'by Mortanauta' + Color.RESET} 
   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
   ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                        
                            ▬ Cortar Excel ▬            
      
    Este programa divide un archivo Excel (xlsx) en archivos Excel más pequeños
    en función del número de filas que le hayamos indicado.
    
    Para funcionar, inserta la ruta completa y el nombre del archivo original,
    por ejemplo: {Color.BLUE + 'C:/Documentos/excel.xlsx '+ Color.RESET}
    Y luego la ruta de destino, si lo dejamos en blanco, se procesará en la misma 
    ruta el archivo original.
    
    {Color.RED + 'NOTA:  ' + Color.RESET} La cabecera es una línea adicional, es decir, que si pedimos un corte 
    de 200 líneas generará archivos de 201 líneas (200 + cabecera). 

    {Color.GREY + '● Author: Mortanauta' + Color.RESET} 
    {Color.GREY + '● Version: 1.00' + Color.RESET} 
    {Color.GREY + '● Website: https://elrincondemorta.wordpress.com/' + Color.RESET}
    {Color.GREY + '● Github: https://github.com/Mortanauta/Public' + Color.RESET}  
    {Color.GREY + '● License: GPL 3.0 https://www.gnu.org/licenses/gpl-3.0.en.html' + Color.RESET}
      
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

# Programa Principal

def split_excel_file():
    print(f"""\n                                    Divisor Excel                    {Color.GREY + "By Mortanauta" + Color.RESET}
                                                                            V:1.00\n
                                                                       
        {Color.GREEN + '|' + Color.RESET}\\        ╔═══════════════════════════════════════════╗        
        {Color.GREEN + '|⁜' + Color.RESET}\\       ║          Divide un excel en bloques       ║   ╔═╗ ╚═╝ ╔═╗ ╚═╝ ║
        {Color.GREEN + '|Morta' + Color.RESET}    ║     🔗    según el número de línea        ║   ╚═╝ ╔═╗ ╚═╝ ╔═╗ ║ 
        {Color.GREEN + '|Nauta' + Color.RESET}    ╚═══════════════════════════════════════════╝  \n """)

    
    # Solicitar el nombre del archivo de origen
    input_file = input("     ⭕ Ruta y nombre del archivo (incluye .xlsx):     ")
    
    # Solicitar la carpeta de salida
    output_folder = input("     ⭕ Carpeta de salida (blanco, carpeta de origen): ")
    
    # Si no se introduce una carpeta de salida, usar la carpeta de origen
    if output_folder.strip() == "":
        output_folder = os.path.dirname(input_file)
    else:
        # Crear la carpeta de salida si no existe
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

    # Solicitar el número de filas por archivo
    rows_per_file = int(input("\n     ⭕ Introduce el número de filas por archivo: "))
    
    print(f"""\n
          {Color.CYAN + 'COMIENZA CONVERSION'+ Color.RESET} 
          {Color.RED  + '********************************' + Color.RESET }\n """)
    
    # Leer el archivo Excel
    df = pd.read_excel(input_file)
    
    # Obtener el número total de filas
    total_rows = len(df)
    
    # Calcular el número de archivos a generar
    num_files = (total_rows // rows_per_file) + (1 if total_rows % rows_per_file != 0 else 0)
    
    # Obtener el nombre base del archivo sin extensión
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    
    # Contador de archivos generados
    files_created = 0
    
    # Dividir el DataFrame y guardar en nuevos archivos
    for i in range(num_files):
        start_row = i * rows_per_file
        end_row = (i + 1) * rows_per_file
        split_df = df[start_row:end_row]
        
        # Generar el nombre del nuevo archivo
        new_file_name = f"{base_name}_{i + 1}.xlsx"
        full_output_path = os.path.join(output_folder, new_file_name)
        
        # Guardar el DataFrame en un nuevo archivo Excel
        split_df.to_excel(full_output_path, index=False)
        
        # Incrementar el contador de archivos creados
        files_created += 1
        print(f"        Archivo generado: {full_output_path}")
    
    # Mostrar el número total de archivos creados
    print(f"""\n
          {Color.RED  + '********************************' + Color.RESET }
          {Color.CYAN + 'Total archivos creados: ' + Color.RESET} {files_created} 
          
          {Color.CYAN + ' ⫷ Proceso finalizado 😎 ⫸ '+ Color.RESET}""")
        

if __name__ == "__main__":
    split_excel_file()
    
input("\n\nPulse Enter para salir... ")
