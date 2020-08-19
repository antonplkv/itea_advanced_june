import socket
import time

HOST = '127.0.0.1'
PORT = 9101

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))


try:
    while True:
        client_socket.send(b'Hello world')
        server_response = client_socket.recv(1024)
        print(server_response)
        time.sleep(2)
except KeyboardInterrupt:
    client_socket.close()