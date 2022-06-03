import hashlib

arquivo1 = 'uno.txt'
arquivo2 = 'dos.txt'

hash1 = hashlib.new('ripemd160') # Algoritmo hash de 160 bits
hash1.update(open(arquivo1, 'rb').read()) # Lê o arquivo e atualiza o hash # rb = read binary

hash2 = hashlib.new('ripemd160') 
hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'Os arquivos {arquivo1} e {arquivo2} são diferentes')
    print(f'Hash do arquivo {arquivo1}: {hash1.hexdigest()}')
    print(f'Hash do arquivo {arquivo2}: {hash2.hexdigest()}')
else:
    print(f'Os arquivos {arquivo1} e {arquivo2} são iguais')
    print(f'Hash do arquivo {arquivo1}: {hash1.hexdigest()}')
    print(f'Hash do arquivo {arquivo2}: {hash2.hexdigest()}')