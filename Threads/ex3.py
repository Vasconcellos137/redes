import threading
import time

WAITING_TIME = 0.1

# Semáforo
semaforo = threading.Semaphore(0)

def thread_0():
    for i in range(1, 11):
        semaforo.acquire() #Ponto d sincronização, a thread fica parada se for 0, se mudar, avança. 
                                              #Ele modifica o valor p 0 e continua parado.
        print(f"[Thread 0] {i}", flush=True)  #Decrementa o valor se for 0, se 1, continua.
    
        semaforo.release() #Incrementa o valor p +1 p q a outra thread continue.
        time.sleep(WAITING_TIME)

import threading
import time

WAITING_TIME = 0.1

# Semáforo
semaforo = threading.Semaphore(0)

def thread_0():
    for i in range(1, 11):
        semaforo.acquire()
    
        print(f"[Thread 0] {i}", flush=True)
    
        semaforo.release()
        time.sleep(WAITING_TIME)


def thread_1():
    for i in range(1, 11):
        semaforo.acquire()
        
        print(f"[Thread 1] {i}", flush=True)
    
        semaforo.release()
        time.sleep(WAITING_TIME)


# Instancia as threads
t0 = threading.Thread(target=thread_0)
t1 = threading.Thread(target=thread_1)

# Starta as threads
t0.start()
t1.start()

# Libera o semáforo
semaforo.release()

# Aguarda as threads finalizarem
print("[Main] Aguardando threads")
t0.join()
t1.join()

print("[Main] Finalizado")
def thread_1():
    for i in range(1, 11):
        semaforo.acquire()
        
        print(f"[Thread 1] {i}", flush=True)
    
        semaforo.release()
        time.sleep(WAITING_TIME)


# Instancia as threads
t0 = threading.Thread(target=thread_0)
t1 = threading.Thread(target=thread_1)

# Starta as threads
t0.start()
t1.start()

# Libera o semáforo
semaforo.release()

# Aguarda as threads finalizarem
print("[Main] Aguardando threads")
t0.join()
t1.join()

print("[Main] Finalizado")

#Há recursos q só podem ser acessados um por vez
#Uma vez distribuidos em subfunções, as threads, é necessário regular o fluxo, ?como um semáforo?