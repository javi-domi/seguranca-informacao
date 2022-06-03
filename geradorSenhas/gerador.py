import random, string

tamanho = int(input("Digite o tamanho da senha: "))
chars = string.ascii_letters + string.digits + 'çñ!@#$%-+=,.:;/\&*()'
rnd = random.SystemRandom() # os.urandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))