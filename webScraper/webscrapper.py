from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.climatempo.com.br/').content 
soup = BeautifulSoup(site, 'html.parser') # html.parser é o parser padrão do python, baixando o html do site
print(soup.prettify()) # prettify() retorna o html formatado em uma string
# temperatura = soup.find('span', class_="_block _margin-b-5 -gray")
print(soup.title) # retorna o titulo do site