# Este projeto consiste na simulação de um servidor que compartilha informações de horário e luminosidade com postes de luz de uma região.
### Postes verificam a luminosidade e horário do dia para acender ou apagar a luz.
## Ferramentas Utilizadas

- Visual Studio Code
- Python 3.11.4  

## Configuração do Ambiente
1. Certifique-se de ter o Python instalado.
2. Instale o Visual Studio Code (ou outra IDE de sua preferência) e configure o projeto.
3. Abra o projeto no Visual Studio Code.
4. Configure o server.py com o endereço IPv4 da máquina (digite ipconfig no cmd para saber qual seu IP).
5. Para cada cliente crie uma máquina virtual ou use máquinas diferentes que estão conectadas na mesma rede.
6. Configure os clients.py com o IP colocado no server.py.

## Como Utilizar
1. Na máquina que será o servidor execute o seguinte comando no terminal:
```
python .\server.py
```
2. Nas máquinas que serão os clientes execute o seguinte comando no terminal: 
```
python .\client_{número_do_arquivo}.py
```


# Importante

No terminal é necessário estar na mesma pasta em que se encontra o arquivo .py para que a execução funcione

Como postes de luz são separados uns dos outros, para uma melhor visualização da simulação é recomendado que cada arquivo esteja em um computador diferente. 
