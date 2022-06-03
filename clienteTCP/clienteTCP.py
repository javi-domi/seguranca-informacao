import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) # Address Family, Socket Type, Protocol
    except socket.error as msg:
        print("A conexão falhou!!")
        print("Erro: {}".format(msg))
        sys.exit(1)# Close em 1 segundo
    print("Conexão estabelecida com sucesso!!")

    host = input("Digite o Host/IP aser conectado: ")
    porta = int(input("Digite a porta: "))

    try:
        s.connect((host, porta))
        print("Cliente TCP conectado com sucesso! Host: " + host + " Porta: " + str(porta))
        s.shutdown(2) # Close em 2 segundos
    except socket.error as msg:
        print("A conexão falhou!!")
        print("Erro: {}".format(msg))
        sys.exit(1)

if __name__ == "__main__":
    main()