import urllib.request as urllib2
from bs4 import BeautifulSoup
import re
import time
import requests
from nltk import ngrams
import hashlib
import numpy as np

def hex_msb_to_int(hex_string):
	return int(hex_string[-2:], 16)

def apply(shingle):
    shingle = shingle.encode('utf-8')
    m = hashlib.sha256()
    m.update(shingle)
    return hex_msb_to_int(m.hexdigest())

URL = 'http://atzeni.dia.uniroma.it'
try:
    page = requests.get(URL)
    data = page.text
    soup = BeautifulSoup(data, 'html.parser')
    stringa = ""
    tags =  (soup.findAll())
    for i in tags:
       stringa = stringa + " " +(i.name)
    stringa = stringa[1:]
    n = 10
    decagram = ngrams(stringa.split(),n)

    for grams in decagram:
         (grams)

except requests.exceptions.RequestException as e:
    print (e)

def map_number_range(number):
	mapped = int(np.interp(number, [111111111111111111111111111111111111, 999999999999999999999999999999999999999], [0, 255]))
	return mapped

def hash_functions(html):
    # viene applicata una hash function, passato il valore in esadecimali e successivamente ricavato l'intero
    # per ultimo viene normalizzato tra 0 e 255

    # h1 = int(hashlib.sha3_256(html.encode()).hexdigest(),16) %255
    # h2 = int(hashlib.sha224(html.encode()).hexdigest(), 16) % 255
    # h3 = int(hashlib.sha1(html.encode()).hexdigest(), 16) % 255
    # h4 = int(hashlib.sha3_384(html.encode()).hexdigest(), 16) % 255
    # h5 = int(hashlib.sha3_512(html.encode()).hexdigest(),16) %255
    # h6 = int(hashlib.sha384(html.encode()).hexdigest(), 16) % 255
    # h7 = int(hashlib.md5(html.encode()).hexdigest(), 16)%255
    # h8 = int(hashlib.blake2b(html.encode()).hexdigest(), 16) % 255
    h1 = int(hashlib.md5(html.encode()).hexdigest(), 16) % 255
    h2 = int(hashlib.sha1(html.encode()).hexdigest(), 16) % 255
    h3 = int(hashlib.sha224(html.encode()).hexdigest(), 16) % 255
    h4 = int(hashlib.sha256(html.encode()).hexdigest(), 16) % 255
    h5 = int(hashlib.sha384(html.encode()).hexdigest(),16) %255
    h6 = int(hashlib.sha512(html.encode()).hexdigest(), 16) % 255
    h7 = int(hashlib.sha3_224(html.encode()).hexdigest(), 16)%255
    h8 = int(hashlib.sha3_256(html.encode()).hexdigest(), 16) % 255
    return (h1,h2,h3,h4,h5,h6,h7,h8)

    #print (h1_,h1)
    #return (h1, h2, h3, h4, h5, h6, h7, h8)

if __name__ == '__main__':
    stringa = "stringa di prova"

