import socket

# IPv4 = AF_INET
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket criado com sucesso!!")

host = 'localhost'
porta = 5433
msg = 'Mensagem de teste'

try:
    print("Cliente enviando mensagem...")
    s.sendto(msg.encode(), (host, 5432)) # encode = enpacotando a mensagem em bytes

    dados, servidor = s.recvfrom(4096) # 4096 = tamanho da mensagem
    dados = dados.decode() # decode = desenpacotando a mensagem
    print("Cliente: " + dados)
finally:
    print("Fechando socket...")
    s.close()