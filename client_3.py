import socket

# Configurações do cliente
host = '127.0.0.0'  # Endereço IP do servidor
port = 12347  # Porta do servidor

# Criação do socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta-se ao servidor
client_socket.connect((host, port))
print("Conectado ao servidor")

valor = True
horarioP = 0

while True:
        # Recebe os dados que o servidor envia.
        data = client_socket.recv(512).decode()

        #Atribui os dados de data para as variáveis
        horario, luminosidade = data.split(',')

        # Pega o primeiro horário que o servidor enviou e manda para outra variável. Para seguir uma linha de tempo e não ficar recebendo sempre horários aleatórios.
        if valor == True:
             horarioP = int(horario)
             valor = False

        print("Horário atual:", str(horarioP) + ":00")

        # Testa se o poste deve estar ligado ou desligado.
        if horarioP >= 19:
            status = ("Poste está com a luz ligada!")
    
        elif horarioP <= 7:
            status = ("Poste está com a luz ligada!")
    
        elif horarioP > 7 and horarioP < 19 and int(luminosidade) < 50:
            print("Luminosidade atual:", luminosidade)
            status = ("Poste está com a luz ligada!")

        else:
            print("Luminosidade atual:", luminosidade)
            status = ("Poste está com a luz desligada!")

        print("Status: ", status)
        print()

        # Soma duas horas no horário atual.
        horarioP = horarioP + 2

        # Vira o dia se o horário passar de 24 horas.
        if horarioP > 24:
            horarioP = horarioP - 24
