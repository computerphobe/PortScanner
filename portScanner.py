#!/bin/python

import pyfiglet
import sys
import socket
import datetime

# ascii art

ascii_banner = pyfiglet.figlet_format("Port Scanner")
print(ascii_banner)

if len(sys.argv) ==2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid arguments")
    print("syntex: python3 <filename> hostname")

# add banner
print("="*50)
print(f"scanning target {target}")
print("="*50)


try:
    for ports in range(1,6520):
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target, ports))

        if result == 0:
            print("No port are open")
        s.close()

except KeyboardInterrupt:
    sys.exit()

except socket.gaierror:
    print("SocketError")
    sys.exit()

except socket.error:
    sys.exit()

