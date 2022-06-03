import itertools

string = input("Digite a string: ")
resultado = itertools.permutations(string, len(string)) # permutação de 3 caracteres

for i in resultado:
    print(''.join(i))