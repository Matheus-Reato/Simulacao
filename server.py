import socket
import random
import time
import threading

# Configurações do servidor
server_ip = '127.0.0.0' #IP do servidor
ports = [12345,12346,12347,12348] #Portas dos clientes

#Gera um horário aleatório
horario = str(random.randint(0, 24))

def handle_client(client_socket, client_address):
    print(f"Conexão estabelecida com {client_address}")

    while True:   

        # Gera uma luminosidade aleatória
        luminosidade = str(random.randint(0, 100))

        # Envia os dados para o cliente
        client_socket.sendall((horario + ',' + luminosidade).encode())      
        
        time.sleep(4)  # Espera por 4 segundos antes de enviar novamente

# Cria um server_socket por vez e atribui nele um IP e porta
server_sockets = []
for port in ports:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, port))
    server_socket.listen(1)
    server_sockets.append(server_socket)

print("Aguardando conexões dos postes...")

threads = []
# Cria as threads para lidar com as conexões
for i, server_socket in enumerate(server_sockets):
    client_socket, client_address = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    threads.append(thread)

# Inicia todas as threads
for i, thread in enumerate(threads):
    thread.start()

