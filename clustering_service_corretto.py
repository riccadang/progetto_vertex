
def check_if_is_cover(vettore1,vettore2):
	for i in range(len(vettore1)):
		if (vettore1[i] == "*") or (vettore2[i] == "*") or (vettore1[i] == vettore2[i]):
			bool = True
		else:
			bool = False
			break
	return bool

###
def find_all_covering_vectors(TABLE_H,eight_vector):
	covers_vector = []
	for i in range(0, len(TABLE_H)):
		vector = TABLE_H[i][0]
		if check_if_is_cover(vector, eight_vector):
			covers_vector.append((TABLE_H[i]))
	return covers_vector