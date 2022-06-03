from bs4 import BeautifulSoup
import requests
import operator # implementar operadores + - * /
from collections import Counter

def start(url): # Definir todo o web crawler 

    wordlist = [] # todo o conteudo do site sera armazenado em uma lista
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, 'html.parser') # html.parser é o parser que vai ler o html do website

    for each_text in soup.find_all('div', {'class': 'entry-content'}): # procurar todos os divs com a classe entry-content
        content = each_text.text
        words = content.lower().split() # transformar todo o conteudo em minusculo e separar em palavras

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)
    
def clean_wordlist(wordlist): # remover simbolos inncesarios
    clean_list = []
    for word in wordlist:
        symbols = "!@#$%^&*()_+{}:\"<>?,./;'[]-=\|"

        for i in range(0, len(symbols)):
                word = word.replace(symbols[i], "")

        if len(word) > 0:
            clean_list.append(word) 
    create_dictionary(clean_list)

def create_dictionary(clean_list): 
    word_count = {}
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print("% s : % s " % (key, value))
    
    c = Counter(word_count) # contar o numero de vezes que cada palavra aparece, parte da lib Counter(collections)

    top = c.most_common(10)
    print(top)

if __name__ == '__main__':
    start('https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar')