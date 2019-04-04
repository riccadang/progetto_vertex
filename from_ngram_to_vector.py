import json



"""
CONTINUARE DA QUI: read_txt_ang_get_all_n_gram legge il file txt che ho creato.
da qui si potrebbe costruire, per ogni pagina, il vettore usando le funzioni hash e salvare i risultati in questo modo:
"nome pagina: vettore"
"""
def read_txt_ang_get_all_n_gram():

	file = open("all_n_gram.txt", "r")
	for line in file:
		testo = (line.split("\t"))
		all_n_gram = (testo[1:])
		for n_gram in all_n_gram:
			print (n_gram)

if __name__ == '__main__':
	read_txt_ang_get_all_n_gram()


