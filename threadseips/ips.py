import ipaddress

ip = '192.168.0.1'
ip_net = '192.168.0.0/24'


endereco = ipaddress.ip_address(ip)
rede = ipaddress.ip_network(ip_net)
print(endereco)
print(rede)

for ip in rede:
    print(ip)