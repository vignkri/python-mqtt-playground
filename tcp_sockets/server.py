#!/usr/bin/env python

"""
Socket Server
"""

import socket
import socketserver


TCP_IP = "127.0.0.1"
TCP_PORT = 5005
BUFFER_SIZE = 1024

while True:
    _availSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _availSocket.bind((TCP_IP, TCP_PORT))
    _availSocket.listen(1)
    conn, addr = _availSocket.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data: 
                break
            # conn.sendall(data)
            print("Received: ", repr(data))
