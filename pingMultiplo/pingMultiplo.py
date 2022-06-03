from dbm import dumb
import os
import time


with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('*' * 50)
        print('Verificando o IP: ' + ip)
        os.system('ping -c 2 ' + ip)
        print('*' * 50)
        time.sleep(2)
