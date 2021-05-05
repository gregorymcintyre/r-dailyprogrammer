# Socket Learning activity
# Console chat program built from foundation work in
# https://www.youtube.com/watch?v=3QiPPX-KeSc

import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = "!exit"

#Handles Rx msgs whilst connected to client
def clientHandler(conn, addr):
    print(f"[Connection] {addr} connected.")
    connected = True
    while connected:
        msgLength = conn.recv(HEADER).decode(FORMAT)
        if msgLength:
            msgLength = int(msgLength)
            msg = conn.recv(msgLength).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
            print(f"\r[{addr}] {msg}\n[SEND] ", end="") #got creative to keep the [SEND] at line start
    conn.close()
    print(f"[Connection] {addr} Closed.")

#connection and msg tx handling
def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=clientHandler, args=(conn, addr))
        thread.start()

        msg = ""
        while (msg != DISCONNECT_MSG):
            print("[SEND] ", end="")
            msg = input()
            send(conn, msg)

#send msg function, uses client info      
def send(conn, msg):
    message = msg.encode(FORMAT)
    msgLength = len(message)
    sendLength = str(msgLength).encode(FORMAT)
    sendLength += b' ' * (HEADER-len(sendLength))
    conn.send(sendLength)
    conn.send(message)  


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

print(f"[STARTING] Server running on {SERVER}:{PORT}")
start()
