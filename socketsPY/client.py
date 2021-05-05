import socket
import threading

PORT = 5050
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = "!exit"

#send msg to server
def send(msg):
    message = msg.encode(FORMAT)
    msgLength = len(message)
    sendLength = str(msgLength).encode(FORMAT)
    sendLength += b' ' * (HEADER-len(sendLength))
    client.send(sendLength)
    client.send(message)  

#rx msgs fm server
def recieve():
    while True:
        msgLength = client.recv(HEADER).decode(FORMAT)
        if msgLength:
            msgLength = int(msgLength)
            msg = client.recv(msgLength).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
            print(f"\r[{SERVER}] {msg}\n[SEND] ", end="")

#thread setup for rx msgs
def connect():
    thread = threading.Thread(target=recieve)
    thread.start()


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print(f"[Connected] Client connected to server at {ADDR}")
print("Use '!exit' to disconnect")

connect()
msg = ""
while (msg != DISCONNECT_MSG):
    print("[SEND] ", end="")
    msg = input()
    send(msg)