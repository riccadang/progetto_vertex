import urllib.request as urllib2
from bs4 import BeautifulSoup
import re
import time
import requests
from nltk import ngrams


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




