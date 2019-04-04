import json
import from_tags_to_decagram


"""
CONTINUARE DA QUI: read_txt_ang_get_all_n_gram legge il file txt che ho creato.
da qui si potrebbe costruire, per ogni pagina, il vettore usando le funzioni hash e salvare i risultati in questo modo:
"nome pagina: vettore"
"""
def from_decagram_to_vector(ngram):
	h1 = []
	h2 = []
	h3 = []
	h4 = []
	h5 = []
	h6 = []
	h7 = []
	h8 = []
	for i in ngram:
		s = "".join(i)
		hashes = from_tags_to_decagram.hash_functions(s)
		h1.append(hashes[0])
		h2.append(hashes[1])
		h3.append(hashes[2])
		h4.append(hashes[3])
		h5.append(hashes[4])
		h6.append(hashes[5])
		h7.append(hashes[6])
		h8.append(hashes[7])
	vector = []
	vector.append(max(h1))
	vector.append(max(h2))
	vector.append(max(h3))
	vector.append(max(h4))
	vector.append(max(h5))
	vector.append(max(h6))
	vector.append(max(h7))
	vector.append(max(h8))
	return vector






def read_txt_ang_get_all_n_gram():

	file = open("all_n_gram.txt", "r")
	for line in file:
		testo = (line.split("\t"))
		all_n_gram = (testo[1:])

		#for n_gram in all_n_gram:
		#	print (n_gram)

if __name__ == '__main__':
	read_txt_ang_get_all_n_gram()


