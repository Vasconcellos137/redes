# Servidor
import socket

HOST = "0.0.0.0"
PORT = 9002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)

    #aguarda gamers
    print("[Server] Aguardando Jogador 1")
    conn_1, addr_1 = s.accept() #s.accept() -> Faz par com s.recv(...)
    conn_1.sendall("[Server] OK. Você é o jogador 1".encode())
    conn_1.sendall("[Server] Aguardando Jogador 2".encode())

    conn_2, addr_2 = s.accept() 
    conn_2.sendall("[Server] OK. Você é o jogador 2".encode())
    conn_2.sendall("[Server] Aguardando Jogador 1 iniciar".encode())

    conn_1.sendall("Escreva sua jogada: ".encode())
    j = conn_1.recv(1024).decode() 
    print(j)
    conn_1.sendall("Aguardando jogador 2 jogar...".encode())

    conn_2.sendall("Escreva sua jogada: ".encode())
    j2 = conn_2.recv(1024).decode() #.decode() -> "Descodifica" os bits p string.
    print(j2)

    # conn_1.sendall("Vencedor é..".encode())
    # conn_2.sendall("Vencedor é..".encode()) #.encode() -> "Codifica" a string p bits.

    cont1 = 0
    cont2 = 0

    while cont1 or cont2 != 3:

        match j:
            case "pedra":
                if j2 == "papel":
                    # msg = "Jogador 2 ganhou"
                    cont2 = +1
                if j2 == "tesoura":
                    # msg = "Jogador 1 ganhou"
                    cont1 = +1
                if j2 == "pedra":
                    # msg = "Empate"
                    cont1 = +0
                    cont2 = +0

            case "papel":
                if j2 == "pedra":
                    # msg = "Jogador 1 ganhou"
                    cont1 = +1
                if j2 == "tesoura":
                    # msg = "Jogador 2 ganhou"
                    cont2 = +1
                if j2 == "papel":
                    # msg = "Empate"
                    cont1 = +0
                    cont2 = +0

            case "tesoura":
                if j2 == "pedra":
                    # msg = "Jogador 2 ganhou"
                    cont2 = +1
                if j2 == "papel":
                    # msg = "Jogador 1 ganhou"
                    cont1 = +1
                if j2 == "tesoura":
                    # msg = "Empate"
                    cont1 = +0
                    cont2 = +0
        
        if cont1 > cont2:
            msg = "Jogador 1 ganhou"
        else: 
            msg = "Jogador 2 ganhou"

    conn_1.sendall(msg.encode())
    conn_2.sendall(msg.encode())

    conn_1.close()
    conn_2.close()
