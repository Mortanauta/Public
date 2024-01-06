# Author: Mortanauta
# Date: 10/01/2023
# Website: https://elrincondemorta.wordpress.com/
# Github: https://github.com/Mortanauta/Public  
# License: GPL 3.0 https://www.gnu.org/licenses/gpl-3.0.en.html

import http.server
import socketserver
import socket  
import os
import sys
import ipaddress

print(f"\n                                                                 Version 2.1\n")
print(f"          ____    |\            --------------             ")
print(f"         ||__||   |⁜\          |   SERVER     |            by: Mortanauta")
print(f"         [ -=.]`) |Morta       |    WEB 🌍    |            https://elrincondemorta.wordpress.com")
print(f"         ====== 0 |Nauta        --------------             https://github.com/Mortanauta/Public\n")
print(f"    Share the folder where the file is located in any web browser.\n\n")

# Specify the port on which you want the server to run
port = 8000

# Configure the request handler
handler = http.server.SimpleHTTPRequestHandler

# Get and change working directory to where the script is located, resolves the issue for laptops
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

# Get the local IP address
# local_ip = socket.gethostbyname(socket.gethostname())
host_name = socket.gethostname()
ip_list = []
for info in socket.getaddrinfo(host_name, None):
    local_ip = info[4][0]
    if ipaddress.ip_address(local_ip).version == 4:
        ip_list.append(local_ip)
ip_list.sort(key=lambda local_ip: (ipaddress.IPv4Address(local_ip), local_ip)) # Sort by IPv4 address

# Create the server at the specified IP address and port
with socketserver.TCPServer(("", port), handler) as server:
    print(f"    ♦ Server IP address:") 
    for local_ip in ip_list:
        print(f"                  » {local_ip}:{port}")
    print(f"    ♦ Published folder:") 
    print(f"                  » {os.getcwd()} \n" )   
    print(f"       (Press Ctrl+C to terminate)\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer successfully stopped by the user.")
        
input("\nPress Enter to exit...")
