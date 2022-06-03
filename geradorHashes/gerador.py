import hashlib

string = input("Digite um texto: ")

menu = int(input("Digite 1 para MD5, 2 para SHA1, 3 para SHA256, 4 para SHA512: "))

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8')) #encode para converter a string em bytes
    print('Hash MD5 da string: ', string, 'é ', resultado.hexdigest()) # Converte bytes para hexadecimal
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print('Hash SHA1 da string: ', string, 'é ', resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print('Hash SHA256 da string: ', string, 'é ', resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print('Hash SHA512 da string: ', string, 'é ', resultado.hexdigest())
else:
    print("Opção inválida")

# resultado = hashlib.md5(b'Python security') # Converte a string para bytes