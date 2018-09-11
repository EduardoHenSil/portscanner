#!/usr/bin/python3
# coding: utf-8

import socket
import sys

my_banner ="""
######################################################
#                                                    #
#               portscanner do EduardoH              #
#                                                    #
######################################################
"""

def print_usage():
    print("Usage: portscanner.py <target>")
    print("Ex: portscanner.py 192.168.0.10")
    print("Ex: portscanner.py http://google.com")
    exit(0)

def create_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    return sock

if __name__ == '__main__':
    print(my_banner)
    if len(sys.argv) != 2:
        print_usage()
    target = sys.argv[1] 

    for port in range(0, 65535):
        try:
            sock = create_socket()
            sock.connect((target, port))
            print("OPEN PORT: {}".format(port))
            banner = sock.recv(1024)
            print("  - port {}: -->> {}".format(port, banner.decode("utf8")))
            print("\n\n")
            del sock
        except Exception as e:
            continue
