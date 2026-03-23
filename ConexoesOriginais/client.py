# Cliente
import socket #importa biblioteca

HOST = "192.168.246.106" #String   127.0.0.1
PORT = 9002              #int

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"ola socket")
    print(s.recv(1024).decode())