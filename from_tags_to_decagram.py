import urllib.request as urllib2
from bs4 import BeautifulSoup
import re
import time
import requests
from nltk import ngrams
import hashlib


URL = 'http://atzeni.dia.uniroma3.it'
page = requests.get(URL)
data = page.text
soup = BeautifulSoup(data, 'html.parser')
stringa = ""
tags =  (soup.findAll())
for i in tags:
   stringa = stringa + " " +(i.name)
stringa = stringa[1:]

print (stringa)
n = 10
decagram = ngrams(stringa.split(),n)
for grams in decagram:
    print (grams)


def hash_functions(html):

    # viene applicata una hash function, passato il valore in esadecimali e successivamente ricavato l'intero
    # per ultimo viene normalizzato tra 0 e 255
    h1 = int(hashlib.sha3_256(html.encode('utf-8')).hexdigest(),16) %255
    h2 = int(hashlib.sha224(html.encode('utf-8')).hexdigest(), 16) % 255
    h3 = int(hashlib.sha1(html.encode('utf-8')).hexdigest(), 16) % 255
    h4 = int(hashlib.sha3_384(html.encode('utf-8')).hexdigest(), 16) % 255
    h5 = int(hashlib.sha3_512(html.encode('utf-8')).hexdigest(),16) %255
    h6 = int(hashlib.sha384(html.encode('utf-8')).hexdigest(), 16) % 255
    h7 = int(hashlib.md5(html.encode('utf-8')).hexdigest(), 16) % 255
    h8 = int(hashlib.blake2b(html.encode('utf-8')).hexdigest(), 16) % 255
    return (h1,h2,h3,h4,h5,h6,h7,h8)

hash_functions("ciao come va che dici")