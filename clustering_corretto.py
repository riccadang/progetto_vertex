from tqdm import tqdm
import generate_masked_vector
from collections import defaultdict
import clustering_service_corretto

def create_masked(vector):
    all_masked = []
    all_masked.append(vector)
    six_eight_io = generate_masked_vector.generate_six_eight(vector)
    seven_eight_io = generate_masked_vector.generate_seven_eight(vector)
    all_masked = all_masked + six_eight_io
    all_masked = all_masked + seven_eight_io
    return all_masked


def first_part():
	#file = open("page_vector_elena.txt", "r", encoding='utf-8')
	file = open("prova.txt", "r", encoding='utf-8')

	vectors = []
	TABLE_H = []
	KEY = []
	VALUE = []
	for x in file:
		tmp = x.rstrip('\n').split(sep='\t')
		vectors.append(tmp[1])
	'''per ogni vettore delle pagine P'''
	for i in tqdm(vectors):
		i = i.replace('[', '').replace(']', '').replace(',', "").split()
		'''calcola tutti i masked shingle vectors'''
		all_masked = create_masked(i)
		'''per ogni masked shingle vector'''
		for masked in all_masked:
			'''se è presente nelle chiavi incrementa il contatore, altrimenti aggiungilo alle chiavi 
			e inizializzalo ad 1'''
			if masked in KEY:
				index = KEY.index(masked)
				VALUE[index] = VALUE[index]+1
			else:
				KEY.append(masked)
				VALUE.append(1)

	for i in range(len(KEY)):
		TABLE_H.append((KEY[i],VALUE[i]))
	return TABLE_H

def second_part(TABLE_H):
	# TROVO TUTTI GLI 8/8
	eight_eight_vectors = []
	for i in range(0,len(TABLE_H)):
		vettore = TABLE_H[i][0]
		vettore_stringa = ''.join(vettore)
		if vettore_stringa.find("*")==-1:
			eight_eight_vectors.append(TABLE_H[i])
	#ORA LI ORDINO DA QUELLO CON MINORI OCCORRENZE:
	eight_eight_vectors = (sorted(eight_eight_vectors, key=lambda x: x[1]))

	#PER OGNI 8/8 VETTORE:
	for eight_vector_tuple in eight_eight_vectors:
		eight_vector =  (eight_vector_tuple[0])
		#TROVO I VETTORI CHE LO COPRONO:
		all_covering_vectors_tuple = clustering_service_corretto.find_all_covering_vectors(TABLE_H,eight_vector)
		#LI ORDINO DA QUELLO CON PIU OCCORRENZE:
		all_covering_vectors_tuple = (sorted(all_covering_vectors_tuple, key=lambda x: x[1],reverse=True))
		#TROVO IL VETTORE COPRENTE CHE HA PIU' OCCORRENZE:
		max_covering_vector_tuple = all_covering_vectors_tuple[0]

		# PER OGNI RICOPRENTE != max_covering_vector_tuple, DIMINUISCI IL SUO VALORE
		# DENTRO TABLE_H CON IL VALORE DI eight_vector
		for i in range(0,len(all_covering_vectors_tuple)):
			if max_covering_vector_tuple[0]!=all_covering_vectors_tuple[i][0]:
				#TROVO INDICE DELL'IESIMO COVERING VECTOR DENTRO TABLE_H
				index = [x for x, y in enumerate(TABLE_H) if y[0] == all_covering_vectors_tuple[i][0]]
				#TROVATO L'INDICE DI QUESTO BENEDETTO COVERING VECTOR AGGIORNO IL SUO CONTATORE
				TABLE_H[index[0]] = (all_covering_vectors_tuple[i][0],all_covering_vectors_tuple[i][1]-eight_vector_tuple[1])
	return (TABLE_H)




if __name__ == '__main__':
	# TABLE H: [(vettore1, occorrenze),(vettore2,occorrenze),...]
	TABLE_H = first_part()

	#VETTORE PER FARE PROVE:
	#TABLE_H = [(["1","2","3","4"],8),(["*","2","3","4"],2),(["0","2","3","4"],5),(["*","2","3","*"],6)]

	#table_copy = TABLE_H.copy()
	#print ("=====")
	TABLE_H_UPDATED = second_part(TABLE_H)
	#for i in range(0,len(TABLE_H)):
		#print (table_copy[i],TABLE_H_UPDATED[i])





