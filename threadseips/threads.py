from threading import Thread
import time

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print(f'Piloto: {piloto}  |  Trajeto: {trajeto} \n')


thread_carro1 = Thread(target=carro, args=[1, 'Bruno']) # target = função, args = argumentos da função: velocidade
thread_carro2 = Thread(target=carro, args=[1.5, 'Lucas'])

thread_carro1.start()
thread_carro2.start()