# Servidor
import socket

HOST = "0.0.0.0"
PORT = 9002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept() #aceitar conexao do client, um pra cada se tivermos dois
    with conn:
        data = conn.recv(1024)
        conn.sendall(b"OK: " + data)