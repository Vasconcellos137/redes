# Servidor
import socket

HOST = "0.0.0.0"
PORT = 9002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #Cria new conexão
    s.bind((HOST, PORT)) #Diz ao comp q quer conexão com esses em específico
    s.listen(1) #Monopoliza 

    #Aguarda gamers
    print("[Server] Aguardando Jogador 1".encode())
    conn_1, addr_1 = s.accept() #s.accept() -> Faz par com s.recv(...)
    conn_1.sendall("[Server] OK. Você é o jogador 1".encode())
    conn_1.sendall("[Server] Aguardando Jogador 2".encode())

    conn_2, addr_2 = s.accept() 
    conn_2.sendall("[Server] OK. Você é o jogador 2".encode())
    conn_2.sendall("[Server] Aguardando Jogador 1 iniciar".encode())

    conn_1.sendall("Escreva sua jogada: ".encode())
    j = s.recv(1024).decode() 
    print(j)
    conn_1.sendall("Aguardando jogador 2 jogar...".encode())

    conn_2.sendall("Escreva sua jogada: ".encode())
    j2 = s.recv(1024).decode() #.decode() -> "Descodifica" os bits p string.
    print(j2)

    conn_1.sendall("Vencedor é..".encode())
    conn_2.sendall("Vencedor é..".encode()) #.encode() -> "Codifica" a string p bits.

    #Cálculo d comparação p descobrir qm venceu
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

    conn_1.sendall(msg.encode())
    conn_2.sendall(msg.encode())

    conn_1.close()
    conn_2.close()
