from xml.dom import minidom
import urllib.request as urllib2
from bs4 import BeautifulSoup
from tqdm import tqdm
import requests
from nltk import ngrams



"""
scarica le pagine, calcola gli ngrammi, e salva i risultati in questo modo:
"nome pagine	ngramma1 	ngramma2 .. "
"""
import json
if __name__ == '__main__':
	file = open("all_n_gram.txt", "w+")
	PATH_SITE_MAP = 'sitemap.xml'
	xmldoc = minidom.parse(PATH_SITE_MAP)
	itemlist = xmldoc.getElementsByTagName('loc')

	ngram_json = {}
	STOP = 0
	for page in tqdm(itemlist):
		page_name = page.childNodes[0].nodeValue

		if not(page_name.endswith("doc") or page_name.endswith(".docx") ):
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

				ngram_json[page_name] = []
				j = 0
				grams_list = []
				for grams in decagram:
					grams_list.append(grams)
				file.write(page_name)
				for element in range(0,len(grams_list)-1):
					file.write("\t" + str(grams_list[element]))
				file.write("\t" + str(grams_list[len(grams_list)-1])+"\n")


				STOP = STOP+1
				if STOP==3000:
					break
			except requests.exceptions.RequestException as e:
				print(e)

			if STOP%10==0:
				print ("salvo")
				with open("write.json", "w") as f:
					json.dump(ngram_json, f, indent=3)




	with open("write.json", "w") as f:
		json.dump(ngram_json,f,indent=3)

