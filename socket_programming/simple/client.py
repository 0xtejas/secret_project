#!/usr/bin/env python
# -*- coding: utf-8 -*-


# "Standard library imports"
import socket
import sys


def main():
    if len(sys.argv) != 3:
        print("Usage: %s HOST PORT" % (sys.argv[0]))
        sys.exit(0)

    host = sys.argv[1]
    port = int(sys.argv[2])
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.send("Test")
    print(sock.recv(10000))
    sock.close()



if __name__ == "__main__":
    main()