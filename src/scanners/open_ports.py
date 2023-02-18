import socket
import sys

# scan a router for open ports
def scanForOpenPorts(ip):
    ports = []
    print()
    print("Scanning for open ports...")
    print()
    for port in range(1, 65535):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                ports.append(port)
                print("Port " + str(port) + " is open")
            s.close()
        except socket.gaierror:
            print("Hostname could not be resolved")
            sys.exit()
        except socket.error:
            print("Couldn't connect to server")
        except socket.timeout:
            print("Connection timed out")
    return ports