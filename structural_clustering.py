from collections import defaultdict
import generate_masked_vector
from tqdm import tqdm
import masked_shingle_vector_service as masked_service

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

#SECOND PART
# def second_part(dict, pages):
#     dict_masked_covered = defaultdict(int)
#     file = open(pages, "r", encoding='utf-8')
#     vectors = []
#     #get vectors
#     for x in file:
#         tmp = x.rstrip('\n').split(sep='\t')
#         vectors.append(tmp[1])
#     #for each vector get the set of masked shingle vectors that covers it an decrement their counts except the leader one (the one with the most counts)
#     for vector in vectors:
#         dict_masked_covered = masked_service.get_masked_vectors_that_covers_vector(dict, vector)
#         dict_masked_covered = masked_service.decrement_counts(dict_masked_covered)
#         #update the dictionary of masked shingle vectors
#         for key, value in dict_masked_covered:
#             dict[key] = value
#     return dict



#SECONDA FASE CORRETTA:
def second_part_riccardo(dict):
    #TROVO TUTTI GLI 8/8
    eight_eight_dict = {}
    for chiave,valore in dict.items():
        if chiave.find("*")==-1:
            eight_eight_dict[chiave]=valore
    #LI ORDINO: DA QUELLO CON MENO OCCORRENZR A PIU' OCCORRENZE
    eight_eight_dict =  sorted(eight_eight_dict.items(), key=lambda x: x[1])
    #PER OGNI 8/8:
    for eight_vector in eight_eight_dict:
        #TROVO I VETTORI CHE LO COPRONO
        covering_vector = masked_service.get_masked_vectors_that_covers_vector_riccardo(eight_vector[0],dict)

        #TROVO IL MASSIMO CHE LO COPRE:
        covering_vector = sorted(covering_vector.items(), key=lambda x: x[1],reverse=True)
        max_cover = covering_vector[0]

        #PER OGNI RICOPRENTE != max_cover, DIMINUISCI IL SUO VALORE
        #DENTRO IL DIZIONARIO DICT CON IL VALORE DI eight_vector
        for cover_vector in covering_vector:
            print (cover_vector,max_cover,eight_vector)
            #if (covering_vector[0]!=max_cover[0]):

                #dict[cover_vector[0]]=dict[covering_vector[0]]-[eight_vector[1]]


    return dict


if __name__ == '__main__':
    dict = first_part()
    print (dict)
    #dict_normalized = second_part(dict, "page_vector_elena.txt")
    #print (dict_normalized)
    #dict = second_part_riccardo(dict)
    #print (dict)