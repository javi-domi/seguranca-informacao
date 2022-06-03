import os  # Importar modulo os

print("#" * 60)

ip_ou_host = input("Digite o IP ou o nome do host a ser verificado: ") # Recebe o IP ou o nome do host a ser verificado

print("-" * 60)

os.system('ping -c 4 {}'.format(ip_ou_host)) # Comando para verificar o IP ou o nome do host

print("#" * 60)