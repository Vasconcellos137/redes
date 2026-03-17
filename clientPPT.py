# Cliente
import socket #importa biblioteca

HOST = "192.168.246.106"
PORT = 9002              

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    #Conecta com server
    s.connect((HOST, PORT))

    #Recebe msg do server
    msg = s.recv(1024).decode()
    print(msg)
    msg = s.recv(1024).decode()
    print(msg)

