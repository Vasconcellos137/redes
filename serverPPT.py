# Servidor
import socket

HOST = "0.0.0.0"
PORT = 9002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)

    #aguarda gamers
    print("[Server] Aguardando Jogador 1")
    conn_1, addr_1 = s.accept()
    conn_1.sendall("[Server] OK. Você é o jogador 1".encode())
    conn_1.sendall("[Server] Aguardando Jogador 2")

    conn_2, addr_2 = s.accept() 
    conn_2.sendall("[Server] OK. Você é o jogador 2".encode())
    conn_2.sendall("[Server] Aguardando Jogador 1 iniciar")
    # conn_1.sendall("[Server] Digite sua jogada: ")

    j = conn_1.sendall("Escreva sua jogada: ")
    j2 = conn_2.sendall("Escreva sua jogada: ")

    match j:
        case "pedra":
            if j2 == "papel":
                msg = "Jogador 2 ganhou"
            if j2 == "tesoura":
                msg = "Jogador 1 ganhou"
            if j2 == "pedra":
                msg = "Empate"
        case "papel":
            if j2 == "pedra":
                msg = "Jogador 1 ganhou"
            if j2 == "tesoura":
                msg = "Jogador 2 ganhou"
            if j2 == "papel":
                msg = "Empate"
        case "tesoura":
            if j2 == "pedra":
                msg = "Jogador 2 ganhou"
            if j2 == "papel":
                msg = "Jogador 1 ganhou"
            if j2 == "tesoura":
                msg = "Empate"


    #envia msg aos gamers.
    # conn_1.sendall("[Server] OK. Você é o jogador 1".encode())
    # conn_2.sendall("[Server] OK. Você é o jogador 2".encode())

    conn_1.close()
    conn_2.close()
1.
    # with conn:
    #     data = conn.recv(1024)
    #     conn.sendall(b"OK: " + data)1.