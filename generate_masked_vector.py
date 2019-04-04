from itertools import permutations


def generate_six_eight(vettore):
	#genero tutte le possibili permutazioni dei numeri da 1 a 8
	permutazioni = list(permutations(range(1, 9)))
	posizioni = []

	#dalle permutazioni, seleziono tutte le posizioni in cui ho il numero 1 e 2: (pos_1,pos_2)
	for p in permutazioni:
		posizioni.append((p.index(1),p.index(2)))

	posizioni =  (list(set(posizioni)))

	#elimino situazioni del tipo: (1,4) e (4,1) e ne mantengo una sola
	posizioni =  list(({tuple(sorted(t)): t for t in posizioni}.values()))

	all_maschera_six_eight= []

	#per ogni posizione che ho trovato, sostiuisci con *
	for maschera in posizioni:
		copia_vettore = vettore.copy()
		primo,secondo =  maschera[0],maschera[1]
		copia_vettore[primo] ="*"
		copia_vettore[secondo]="*"
		all_maschera_six_eight.append(copia_vettore)
	return all_maschera_six_eight



def generate_seven_eight(vettore):
	all_maschera_seven_eight = []
	for i in range(0,len(vettore)):
		vettore_copia = vettore.copy()
		vettore_copia[i]="*"
		all_maschera_seven_eight.append(vettore_copia)
	return all_maschera_seven_eight



if __name__ == '__main__':
	vettore = [2,0,1,0,0,0,1,0]
	all_masked = []
	all_masked.append(vettore)
	six_eight_io = generate_six_eight(vettore)
	seven_eight_io = generate_seven_eight(vettore)
	all_masked = all_masked+six_eight_io
	all_masked = all_masked+seven_eight_io

