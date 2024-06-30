import os
import sys
import time
import subprocess
import socket
import threading


PORT = 8080
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind(ADDR)
except OSError:
    subprocess.call("ps -fA | grep python", shell=True)
    kill = input("Kill the third number, then we can continue: ")
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
        msg = conn.recv()


print("Starting server...")


def silly_lil_func(num):
    for idx in range(num):
        print(idx)




if __name__ == "__main__":
    print(SERVER)
    start()

