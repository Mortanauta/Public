# Author: Mortanauta
# Date: 01/10/2023
# Website: https://elrincondemorta.wordpress.com/
# Github: https://github.com/Mortanauta/Public  
# License: GPL 3.0 https://www.gnu.org/licenses/gpl-3.0.en.html

import socket
import ipaddress
import re
import datetime
import platform
import os
import time

# --Cut here--8<-------------------------------------------------------------------
# Main page

# Define colors
class Color:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    GREY = '\033[90m'

# Check the operating system
OS = platform.system()
OS_version = platform.release()

print(f"""

   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
   ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                        
                            ▬ Port Scanner ▬            
      
    This code quickly scans a network for open ports, displaying accessible ones.

    NOTE:    
    ├ Leave the end IP blank to scan only selected IP.
    └ Leave the end port blank to scan only selected port.  
           
    {Color.RED + 'ATTENTION:' + Color.RESET} Scanning a network without permission may be illegal.

    {Color.GREY + '● Author: Mortanauta' + Color.RESET} 
    {Color.GREY + '● Version: 1.32' + Color.RESET} 
    {Color.GREY + '● Website: https://elrincondemorta.wordpress.com/' + Color.RESET}
    {Color.GREY + '● Github: https://github.com/Mortanauta/Public' + Color.RESET}  
    {Color.GREY + '● License: GPL 3.0 https://www.gnu.org/licenses/gpl-3.0.en.html' + Color.RESET}
      
   ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ 
   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""")
# Print operating system check
input(f"""
    CHECKING OPERATING SYSTEM
     └ Detected operating system: {OS} {OS_version}

      Press Enter to continue...""")   

# Clear the screen
os.system("cls" if OS == "Windows" else "clear")
time.sleep(1)

# --Cut here--8<-------------------------------------------------------------------
# Main Program

# Function to validate an IP address using a regular expression
def validate_ip_address(ip):
    ip_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    return re.match(ip_pattern, ip)

# Function to validate that a port is a number between 1 and 65535
def validate_port(port):
    try:
        port = int(port)
        return 1 <= port <= 65535
    except ValueError:
        return False

# Function to scan a range of IP addresses and ports for open ports
def scan_ips(start_ip, end_ip, start_port, end_port, verbose=False):
    # Convert start and end IP addresses to ipaddress objects
    start = ipaddress.ip_address(start_ip)
    if not end_ip:
        end_ip = start_ip # If no end IP is specified, use the start IP
    end = ipaddress.ip_address(end_ip)
    
    # Create a list of IP addresses in the specified range
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
                    print(f"  IP: {ip_address}, Port: {port} - Open :)")
                else:
                    print(f"  IP: {ip_address}, Port: {port} - Closed")
            if result == 0:
                open_ports.append((ip_address, port))
            sock.close()
    return open_ports

# Get the local IP address of the machine
#local_ip_address = socket.gethostbyname(socket.gethostname()) # When there's only one IP address associated with the machine (A)

# Main Program
print("""\n                                 PORT SCANNER                                    V:1.32\n
    |\\        ╔══════════════════════════════════════════════════╗        
    |⁜\\       ║  This program scans a network for open ports.    ║   ╔═╗ ╚═╝ ╔═╗ ╚═╝ ║
    |Morta    ║      ⸎    Enter the network data to scan:        ║   ╚═╝ ╔═╗ ╚═╝ ╔═╗ ║ 
    |Nauta    ╚══════════════════════════════════════════════════╝
\n """)

#print(f"           Machine's IP Address: {local_ip_address} \n ") # When there's only one IP address associated with the machine (A)

# List all IP addresses associated with this machine (IPv4 and IPv6)
print("           Machine's IP Addresses:")
host_name = socket.gethostname()
ip_list = []
for info in socket.getaddrinfo(host_name, None):
    ip = info[4][0]
    if ipaddress.ip_address(ip).version == 4:
        ip_list.append(ip)
ip_list.sort(key=lambda ip: (ipaddress.IPv4Address(ip), ip)) # Sort by IPv4 address
for ip in ip_list:
    print("             »", ip)

# Request the start IP and validate it is a valid IP address
print("\n")
while True:
    start_ip = input(" O - Enter the Start IP: ")
    if validate_ip_address(start_ip):
        break
    else:
        print("\n     Incorrect IP. Please try again.\n")
# Request the end IP and validate it is a valid IP address, allowing it to be left blank
while True:
    end_ip = input(" O - Enter the End IP:   ")
    if validate_ip_address(end_ip) or end_ip == "":
        break
    else:
        print("\n     Incorrect IP. Please try again.\n")

# Request the start port and validate it is a valid port
while True:
    start_port = input(" O - Enter the Start Port (min. 1):   ")
    if validate_port(start_port):
        start_port = int(start_port)
        break
    else:
        print("\n     Invalid port. Please try again.\n")

# Request the end port and validate it is a valid port, allowing it to be left blank
while True:
    end_port = input(" O - Enter the End Port (max. 65535): ")
    if end_port == "":
        end_port = start_port # If no end port is specified, use the start port
        break
    elif validate_port(end_port):
        end_port = int(end_port)
        break
    else:
        print("\n     Invalid port. Range is 0 to 65535, please try again.\n")

# Request if verbose mode is desired
verbose = input(" O - Verbose Mode? (y/n): ").lower() == "y"
print("\nScanning... 👀 \n")

# Record current time
t1 = datetime.datetime.now()

# Perform port scanning and display the results
results = scan_ips(start_ip, end_ip, start_port, end_port, verbose)

if results:
    print("\nOpen Ports:")
    for result in results:
        print(f"  IP: {result[0]}, Port: {result[1]}")
else:
    print("\nNo open ports found. ¯\\(°_o)/¯ ")

# Record final time and calculate total time
t2 = datetime.datetime.now()
total = t2 - t1
#print(f"\nTotal time: {total}")

# Convert time format. Extract individual time parts
hours = total.seconds // 3600
minutes = (total.seconds % 3600) // 60
seconds = total.seconds % 60

# Create a custom format string
print(f"                                               ⌛ Duration ►► {hours} h {minutes} min {seconds} s")
# Wait for Enter to be pressed to exit

input("\nPress Enter to exit...")


