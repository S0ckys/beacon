import os
import sys
import time
import socket
import threading


PORT = 8080
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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



if __name__ == "__main__":
    try:
        max = int(input("Let's count! Pick a number: "))
    except ValueError:
        max = int(input("Hey! Number, please: "))
    for i in range(max):
        print(i)
        time.sleep(.2)
    time.sleep(.3)
    print(SERVER)
    
    start()

print("start server...")
