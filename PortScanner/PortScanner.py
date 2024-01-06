# Author: Mortanauta
# Date: 01/10/2023
# Website: https://elrincondemorta.wordpress.com/
# Github: https://github.com/Mortanauta/Public  
# License: GPL 3.0 https://www.gnu.org/licenses/gpl-3.0.en.html

import socket
import ipaddress
import re
import datetime

# Function to validate an IP address using a regular expression
def validate_ip_address(ip):
    ip_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    return re.match(ip_pattern, ip)

# Function to validate whether a port is a number between 1 and 65535
def validate_port(port):
    try:
        port = int(port)
        return 1 <= port <= 65535
    except ValueError:
        return False

# Function to scan a range of IP addresses and ports for open ports
def scan_ips(start_ip, end_ip, start_port, end_port, verbose=False):
    # Convert start and end IP addresses into ipaddress objects
    start = ipaddress.ip_address(start_ip)
    if not end_ip:
        end_ip = start_ip  # If no end IP is specified, use the start IP
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
# local_ip = socket.gethostbyname(socket.gethostname())  # When only one IP address is associated with the machine (A)

# Main Program
print("\n                                 PORT SCANNER                    V:1.31\n")
print("   |\\         -----------------------------------------------       By: Mortanauta            ")           
print("   |⁜\\       |  This program scans a network for open ports  |      https://elrincondemorta.wordpress.com/  " )
print("   |Morta    |        Enter the network data to scan:        |      https://github.com/Mortanauta/Public")
print("   |Nauta     -----------------------------------------------\n")

# Print all IP addresses associated with this machine (IPv4 and IPv6)
print("           Machine's IP Addresses:")
host_name = socket.gethostname()
ip_list = []
for info in socket.getaddrinfo(host_name, None):
    ip = info[4][0]
    if ipaddress.ip_address(ip).version == 4:
        ip_list.append(ip)
ip_list.sort(key=lambda ip: (ipaddress.IPv4Address(ip), ip))  # Sort by IPv4 address
for ip in ip_list:
    print("             »", ip)

# Request the start IP and validate it as a valid IP address
print("\n")
while True:
    start_ip = input(" O - Enter the Start IP: ")
    if validate_ip_address(start_ip):
        break
    else:
        print("\n     Incorrect IP. Please try again.\n")

# Request the end IP and validate it as a valid IP address, allowing it to be left blank
while True:
    end_ip = input(" O - Enter the End IP:   ")
    if validate_ip_address(end_ip) or end_ip == "":
        break
    else:
        print("\n     Incorrect IP. Please try again.\n")

# Request the start port and validate it as a valid port number
while True:
    start_port = input(" O - Enter the Start Port (min. 1):   ")
    if validate_port(start_port):
        start_port = int(start_port)
        break
    else:
        print("\n     Invalid port. Please try again.\n")

# Request the end port and validate it as a valid port number, allowing it to be left blank
while True:
    end_port = input(" O - Enter the End Port (max. 65535): ")
    if end_port == "":
        end_port = start_port  # If no end port is specified, use the start port
        break
    elif validate_port(end_port):
        end_port = int(end_port)
        break
    else:
        print("\n     Invalid port. Range from 1 to 65535, please try again.\n")

# Ask if verbose mode is desired
verbose = input(" O - Verbose mode? (y/n): ").lower() == "y"
print("\nScanning... 👀 \n")

# Capture current time
t1 = datetime.datetime.now()

# Perform port scanning and display the results
results = scan_ips(start_ip, end_ip, start_port, end_port, verbose)

if results:
    print("\nOpen ports:")
    for result in results:
        print(f"  IP: {result[0]}, Port: {result[1]}")
else:
    print("\nNo open ports found. ¯\\(°_o)/¯ ")

# Capture final time and calculate total time
t2 = datetime.datetime.now()
total = t2 - t1

# Time format conversion. Extract individual time parts
hours = total.seconds // 3600
minutes = (total.seconds % 3600) // 60
seconds = total.seconds % 60

# Create a customized time format string
print(f"                                               ⌛ Duration ►► {hours} h {minutes} min {seconds} s")
# Wait for Enter key press to exit

input("\nPress Enter to exit...")
