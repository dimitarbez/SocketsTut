import socket
import threading
from typing import MutableSequence

HEADER = 64
PORT = 4200
SERVER = "192.168.1.195"
print(SERVER)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"NEW CONNECTION: {addr} connected")
    connected = True
    while connected:
        #blocking line of code
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}]:'{msg}'")
    conn.close()

def start():
    server.listen()
    print("Server is starting on port " + str(PORT))
    while True:
        #blocking line of code
        (conn, addr) = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"ACTIVE CONNECTIONS: {threading.active_count() - 1}")

start()
