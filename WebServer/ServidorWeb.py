# Autor: Mortanauta
# Versión: 2.2
# Sitio web: https://elrincondemorta.wordpress.com/
# Github: https://github.com/Mortanauta/Public
# Licencia: GPL 3.0 https://www.gnu.org/licenses/gpl-3.0.en.html

import http.server
import socketserver
import socket  
import os
import sys
import ipaddress
import platform
import time

# --Corte aquí--8<-------------------------------------------------------------------
# Página principal

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

   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
   ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                        
                             ▬ SERVIDOR WEB ▬            
      
    Este programa permite compartir la carpeta donde se encuentre el archivo.
    Solo es necesario ejecutar el programa y compartir la dirección IP.

    Utilizar con {Color.RED + 'precaución' + Color.RESET}, el programa no tiene medidas de seguridad.

               Presiona Ctrl+C para detener el servidor.

    {Color.GREY + '● Autor: Mortanauta' + Color.RESET} 
    {Color.GREY + '● Versión: 2.2' + Color.RESET} 
    {Color.GREY + '● Sitio web: https://elrincondemorta.wordpress.com/' + Color.RESET}
    {Color.GREY + '● Github: https://github.com/Mortanauta/Public' + Color.RESET}  
    {Color.GREY + '● Licencia: GPL 3.0 https://www.gnu.org/licenses/gpl-3.0.en.html' + Color.RESET}
      
   ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ 
   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""")
# Imprimir comprobación del sistema operativo
input(f"""
    COMPROBANDO EL SISTEMA OPERATIVO
     ├ Sistema operativo detectado: {OS} {OS_version}
     └ Directorio actual: {os.path.dirname(os.path.abspath(sys.argv[0]))}

      Presiona Enter para continuar...""")   

# Limpiar la pantalla
os.system("cls" if OS == "Windows" else "clear")
time.sleep(1)

# --Corte aquí--8<-------------------------------------------------------------------
# Programa principal

print(f"""\n                                                                 Version 2.2\n
             ____    |\         ╔══════════════╗         
            ||__||   |⁜\        ║   SERVIDOR   ║ ╔═╗ ╚═╝ ╔═╗ ╚═╝ ║           
            [ -=.]`) |Morta     ║     WEB 🌍   ║ ╚═╝ ╔═╗ ╚═╝ ╔═╗ ║           
            ====== 0 |Nauta     ╚══════════════╝              
        
            Comparte la carpeta donde esté ubicado el archivo en cualquier navegador web.\n\n""")


# Especifica el puerto en el que deseas que se ejecute el servidor
puerto = 8000

# Configura el manejador de solicitudes
manejador = http.server.SimpleHTTPRequestHandler

#Obtiene y cambia de carpeta de trabajo por la que está ubicada el script, resuelve el tema de los portatiles
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

# Obtiene la dirección IP local
#direccion_ip = socket.gethostbyname(socket.gethostname())
host_name = socket.gethostname()
ip_list = []
for info in socket.getaddrinfo(host_name, None):
    direccion_ip = info[4][0]
    if ipaddress.ip_address(direccion_ip).version == 4:
        ip_list.append(direccion_ip)
ip_list.sort(key=lambda direccion_ip: (ipaddress.IPv4Address(direccion_ip), direccion_ip)) # Ordena por dirección IPv4


# Crea el servidor en la dirección IP y el puerto especificados
with socketserver.TCPServer(("", puerto), manejador) as servidor:
    print(f"    ♦ Servidor dirección IP:") 
    for direccion_ip in ip_list:
        print(f"                  » {direccion_ip}:{puerto}")
    print(f"    ♦ Carpeta publicada:") 
    print(f"                  » {os.getcwd()} \n" )   
    print(f"       (Pulse Ctrl+C para finalizar)\n")
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido con éxito por el usuario.")
        

input("\nPulse Enter para salir...")

