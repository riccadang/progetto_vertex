from xml.dom import minidom
import urllib.request as urllib2
from bs4 import BeautifulSoup
from tqdm import tqdm
import requests
from nltk import ngrams
import from_ngram_to_vector

"""
scarica le pagine, calcola gli ngrammi, e salva i risultati in questo modo:
"nome pagine	vector "
"""

if __name__ == '__main__':
    file = open("page_vector.txt", "w+")
    PATH_SITE_MAP = 'sitemap.xml'
    xmldoc = minidom.parse(PATH_SITE_MAP)
    itemlist = xmldoc.getElementsByTagName('loc')
    STOP = 0
    for page in tqdm(itemlist):
        page_name = page.childNodes[0].nodeValue
        if not (page_name.endswith("doc") or page_name.endswith(".docx")):
            try:
                page = requests.get(page_name)
                data = page.text
                soup = BeautifulSoup(data, 'html.parser')
                stringa = ""
                tags = (soup.findAll())
                for i in tags:
                    stringa = stringa + " " + (i.name)
                stringa = stringa[1:]
                n_grammi = 10
                decagram = ngrams(stringa.split(), n_grammi)

                grams_list = []
                for grams in decagram:
                    grams_list.append(grams)
                vector = from_ngram_to_vector.from_decagram_to_vector(grams_list)

                file.write(page_name)
                file.write("\t" + str(vector) + "\n")
                STOP = STOP + 1

                if STOP == 2000:
                    break
            except requests.exceptions.RequestException as e:
                print(e)