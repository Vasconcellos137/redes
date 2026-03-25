import threading

def tarefa():                      #função/método q a thead executará
    print("Executando tarefa...")

#tarefa()
t = threading.Thread(target=tarefa)
t.start()
t.join()

print("Finalizado")