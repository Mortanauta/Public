# Autor: Mortanauta
# Fecha: 01/10/2023
# Web: https://elrincondemorta.wordpress.com/
# Github: https://github.com/Mortanauta/Public  
# Licencia: GPL 3.0 https://www.gnu.org/licenses/gpl-3.0.en.html

import http.server
import socketserver
import socket  # Importa el módulo socket
import os
import sys
import ipaddress

print(f"\n                                                                  Version 2.1\n")
print(f"          ____    |\            --------------                  by: Mortanauta")
print(f"         ||__||   | \          |   SERVIDOR   |                 https://elrincondemorta.wordpress.com/")
print(f"         [ -=.]`) | /          |    WEB 🌍    |                 https://github.com/Mortanauta/Public ")
print(f"         ====== 0 |/            --------------\n")
print(f"    Comparte la carpeta donde esté ubicado el archivo en cualquier navegador web.\n\n")

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

