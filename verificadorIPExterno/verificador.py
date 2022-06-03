import re
import json
from urllib.request import urlopen

url = 'http://ipinfo.io/json'

resposta = urlopen(url)
dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']

print('Detalhes do IP Externo:\n')
print('IP: {}\nOrganização: {}\nCidade: {}\nPaís: {}\nRegião: {}'.format(ip, org, cid, pais, regiao))