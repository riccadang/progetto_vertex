from collections import defaultdict
import generate_masked_vector
from tqdm import tqdm
import masked_shingle_vector_service as masked_service
import clustering_corretto as clustering
import list_service

def create_masked(vector):
    all_masked = []
    all_masked.append(vector)
    six_eight_io = generate_masked_vector.generate_six_eight(vector)
    seven_eight_io = generate_masked_vector.generate_seven_eight(vector)
    all_masked = all_masked + six_eight_io
    all_masked = all_masked + seven_eight_io
    return all_masked

#FIRST PART
def first_part():
    dict = defaultdict(int)
    file = open("page_vector_elena.txt","r", encoding='utf-8')
    vectors = []
    for x in file:
        tmp = x.rstrip('\n').split(sep='\t')
        vectors.append(tmp[1])
    for i in tqdm(vectors):
        i = i.replace('[','').replace(']','').replace(',',"").replace(" ","")
        i = list(i)
        all_masked = create_masked(i)
        for masked in all_masked:
            masked = ''.join(masked)
            dict[masked]= dict[masked]+1
    return dict

#SECONDA FASE CORRETTA:
def second_part_riccardo(list):
    #TROVO TUTTI GLI 8/8
    eight_eight_list = []
    for chiave,valore in list:
        if "*" in chiave:
            eight_eight_list = list_service.update_value(eight_eight_list, (chiave, valore))
            # eight_eight_dict[chiave]=valore
    #LI ORDINO: DA QUELLO CON MENO OCCORRENZR A PIU' OCCORRENZE
    eight_eight_list = sorted(list, key = lambda x: x[1])
    # eight_eight_dict =  sorted(eight_eight_dict.items(), key=lambda x: x[1])
    #PER OGNI 8/8:
    for eight_vector in eight_eight_list:
        #TROVO I VETTORI CHE LO COPRONO
        covering_vector = masked_service.get_masked_vectors_that_covers_vector_riccardo(eight_vector[0],dict)

        #TROVO IL MASSIMO CHE LO COPRE:
        covering_vector = sorted(covering_vector.items(), key=lambda x: x[1],reverse=True)
        max_cover = covering_vector[0]

        #PER OGNI RICOPRENTE != max_cover, DIMINUISCI IL SUO VALORE
        #DENTRO IL DIZIONARIO DICT CON IL VALORE DI eight_vector
        for cover_vector in covering_vector:
            print (cover_vector,type(cover_vector),max_cover,type(max_cover),eight_vector,type(eight_vector), dict[cover_vector[0]],type(dict[cover_vector[0]]))
            if (cover_vector[0]!=max_cover[0]):
                #print(str(dict[cover_vector[0]])+' - '+str(eight_vector[1]))
                val = dict[cover_vector[0]]
                dict[cover_vector[0]] = val - [eight_vector[1]]
                if (dict[cover_vector[0]] == 0):
                    dict.pop(cover_vector[0])
    return dict


#third part
def third_part(list):
    clusters = defaultdict(list)
    for key, value in dict:
        clusters[key] = []
    file = open("page_vector_elena.txt", "r", encoding='utf-8')
    vectors = []
    for x in file:
        tmp = x.rstrip('\n').split(sep='\t')
        vectors.append(tmp)
    for vector in vectors:
        print("eccoci")
        key = masked_service.get_max_masked_vectors_that_covers_vector_riccardo(vector[1], dict)
        clusters[key].add(vector[0])
    return clusters

def third_part_corretta(all_masked):
    clusters = defaultdict(list)
    file = open("page_vector_elena.txt", "r", encoding='utf-8')
    vectors = []
    for x in file:
        tmp = x.rstrip('\n').split(sep='\t')
        vectors.append(tmp[1])

    for i in tqdm(vectors):
        i = i.replace('[', '').replace(']', '').replace(',', "").split()
        key = masked_service.get_max_masked_vectors_that_covers_vector_riccardo(i, all_masked)
        clusters[key].append(i)


if __name__ == '__main__':
    list1 = clustering.first_part()
    for i in list1:
        print(i)
    dict = third_part_corretta(list1)
    for i in dict :
        print(i)
        print("\n")
