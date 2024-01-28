# Autor: Mortanauta
# Fecha: 01/10/2023
# Web: https://elrincondemorta.wordpress.com/
# Github: https://github.com/Mortanauta/Public  
# Licencia: GPL 3.0 https://www.gnu.org/licenses/gpl-3.0.en.html


import socket
import ipaddress
import re
import datetime
import platform
import os
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
                        
                            ▬ Escaner de Puertos ▬            
      
    Este código permite buscar de una forma rápida puertos abiertos en la red 
    especificadam mostrando aquellos que están accesibles.

    NOTA:    
    ├ Dejar la IP final en blanco para escanear solo una IP.
    └ Dejar el puerto final en blanco para escanear solo un puerto.  
           
    {Color.RED + 'ATENCIÓN:' + Color.RESET} Escanear una red sin permiso puede ser delito.

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
    COMPROBANDO EL SISTEMA OPERATIVO
     └ Sistema operativo detectado: {OS} {OS_version}

      Presiona Enter para continuar...""")   

# Limpiar la pantalla
os.system("cls" if OS == "Windows" else "clear")
time.sleep(1)

# --Corte aquí--8<-------------------------------------------------------------------
# Programa principal


# Función para validar una dirección IP utilizando una expresión regular
def validar_direccion_ip(ip):
    patron_ip = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    return re.match(patron_ip, ip)

# Función para validar que un puerto sea un número entre 1 y 65535
def validar_puerto(puerto):
    try:
        puerto = int(puerto)
        return 1 <= puerto <= 65535
    except ValueError:
        return False

# Función para escanear un rango de direcciones IP y puertos en busca de puertos abiertos
def scan_ips(start_ip, end_ip, start_port, end_port, verbose=False):
    # Convierte las direcciones IP de inicio y final en objetos ipaddress
    start = ipaddress.ip_address(start_ip)
    if not end_ip:
        end_ip = start_ip # Si no se especifica una IP final, se toma la IP inicial
    end = ipaddress.ip_address(end_ip)
    
    # Crea una lista de direcciones IP en el rango especificado
    ip_range = list(range(int(start), int(end) + 1))

    open_ports = []

    for ip in ip_range:
        ip_address = str(ipaddress.ip_address(ip))
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.005)
            result = sock.connect_ex((ip_address, port))
            if verbose:
                if result == 0:
                    print(f"  IP: {ip_address}, Puerto: {port} - Abierto :)")
                else:
                    print(f"  IP: {ip_address}, Puerto: {port} - Cerrado")
            if result == 0:
                open_ports.append((ip_address, port))
            sock.close()
    return open_ports

# Obtiene la dirección IP local del equipo
#direccion_ip = socket.gethostbyname(socket.gethostname()) # Cuando solo hay una dirección IP asociada al equipo (A)

# Main Program
print("""\n                                 ESCANER PUERTOS                                    V:1.32\n
    |\\        ╔══════════════════════════════════════════════════════════════╗        
    |⁜\\       ║  Este programa escanea una red en busca de puertos abiertos  ║   ╔═╗ ╚═╝ ╔═╗ ╚═╝ ║
    |Morta    ║      ⸎    Introduzca los datos de la red a escanear:         ║   ╚═╝ ╔═╗ ╚═╝ ╔═╗ ║ 
    |Nauta    ╚══════════════════════════════════════════════════════════════╝   \n """)

#print(f"           Dirección IP del equipo: {direccion_ip} \n ") # Cuando solo hay una dirección IP asociada al equipo (A)


# Lista todas las direcciones IP asociadas a este equipo (IPv4 e IPv6)
print("           Direcciones IP del equipo:")
host_name = socket.gethostname()
ip_list = []
for info in socket.getaddrinfo(host_name, None):
    ip = info[4][0]
    if ipaddress.ip_address(ip).version == 4:
        ip_list.append(ip)
ip_list.sort(key=lambda ip: (ipaddress.IPv4Address(ip), ip)) # Ordena por dirección IPv4
for ip in ip_list:
    print("             »", ip)

# Solicita la IP de inicio y valida que sea una dirección IP válida
print("\n")
while True:
    start_ip = input(" O - Introduzca la IP Inicial: ")
    if validar_direccion_ip(start_ip):
        break
    else:
        print("\n     IP incorrecta. Inténtelo de nuevo.\n")
# Solicita la IP final y valida que sea una dirección IP válida, permitiendo dejarla en blanco
while True:
    end_ip = input(" O - Introduzca la IP Final:   ")
    if validar_direccion_ip(end_ip) or end_ip == "":
        break
    else:
        print("\n     IP incorrecta. Inténtelo de nuevo.\n")

# Solicita el puerto de inicio y valida que sea un puerto válido
while True:
    start_port = input(" O - Introduzca el Puerto Inicial (min. 1):   ")
    if validar_puerto(start_port):
        start_port = int(start_port)
        break
    else:
        print("\n     Puerto no válido. Inténtelo de nuevo.\n")

# Solicita el puerto final y valida que sea un puerto válido, permitiendo dejarlo en blanco
while True:
    end_port = input(" O - Introduzca el Puerto Final (max. 65535): ")
    if end_port == "":
        end_port = start_port # Si no se especifica un puerto final, se toma el puerto inicial
        break
    elif validar_puerto(end_port):
        end_port = int(end_port)
        break
    else:
        print("\n     Puerto no válido. Rango de 0 a 65535, inténtelo de nuevo.\n")

# Solicita si se desea un modo verbose
verbose = input(" O - ¿Modo Verbose? (s/n): ").lower() == "s"
print("\nEscanenado... 👀 \n")

# Captura de tiempo actual
t1 = datetime.datetime.now()

# Realiza el escaneo de puertos y muestra los resultados
results = scan_ips(start_ip, end_ip, start_port, end_port, verbose)

if results:
    print("\nPuertos abiertos:")
    for result in results:
        print(f"  IP: {result[0]}, Puerto: {result[1]}")
else:
    print("\nNo hay puertos abiertos. ¯\\(°_o)/¯ ")

# Captura de tiempo final y cálculo del tiempo total
t2 = datetime.datetime.now()
total = t2 - t1
#print(f"\nTiempo total: {total}")

#Conversión formato tiempo. Extrae las partes de tiempo individuales
horas = total.seconds // 3600
minutos = (total.seconds % 3600) // 60
segundos = total.seconds % 60

# Crea una cadena de formato personalizada
print(f"                                               ⌛ Duración ►► {horas} h {minutos} min {segundos} s")
# Espera a que se pulse Enter para salir

input("\nPulse Enter para salir...")