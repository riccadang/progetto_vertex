from tqdm import tqdm
import generate_masked_vector
from collections import defaultdict

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



if __name__ == '__main__':
	TABLE_H = first_part()
	print (TABLE_H)

