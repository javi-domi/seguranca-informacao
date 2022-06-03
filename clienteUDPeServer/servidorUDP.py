import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # IPv4, UDP
print("Socket criado com sucesso!!")

host = 'localhost'
porta = 5432

s.bind((host, porta))
msg = '\nServidor: Mensagem para cliente'

while 1:
    dados, end = s.recvfrom(4096) # 4096 = tamanho da mensagem
    if dados:
        print("Servidor enviando mensagem...")
        s.sendto(dados + msg.encode(), end) # encode = enpacotando a mensagem em bytes