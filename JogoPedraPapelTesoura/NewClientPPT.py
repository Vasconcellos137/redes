# Cliente
import socket #importa biblioteca

HOST = "192.168.246.175"
PORT = 9002              

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    #Conecta com server
    s.connect((HOST, PORT))

    #Recebe msg do server
    msg = s.recv(1024).decode() #s.recv() -> Faz par com s.accept(...) / recebe -> ("[Server] OK. Você é o jogador 1".encode())
    print(msg)
    msg = s.recv(1024).decode() 
    print(msg)

    msg = s.recv(1024).decode() #Recebe msg p fazer jogada
    print(msg)

    jog = input("Jogue: ") #N precisa de duas, estão a utilizar msm code

    s.sendall(jog.encode())

    msg = s.recv(1024).decode() 
    print(msg)

    print(s.recv(1024).decode()) #print resultado d if
