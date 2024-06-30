import os
import sys
import time
import subprocess
import socket
import threading

HEADER = 64
PORT = 8080
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MSG = "!DROP"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind(ADDR)
except OSError:
    subprocess.call("ps -fA | grep python", shell=True)
    input("Kill the third number, then we can continue (format: kill ____): ")
    server.bind(ADDR)


def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


def handle_client(conn, addr):
    print(f"Connection Added: {addr} added")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(HEADER).decode(FORMAT)
        if msg == DISCONNECT_MSG:
            connected = False

        print(f"[{addr}] {msg}")
    conn.close()



print("Starting server...")


def silly_lil_func(num):
    for idx in range(num):
        print(idx)




if __name__ == "__main__":
    print(SERVER)
    start()

