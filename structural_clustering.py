from collections import defaultdict
import generate_masked_vector

def create_masked(vector):
    all_masked = []
    all_masked.append(i)
    six_eight_io = generate_masked_vector.generate_six_eight(i)
    seven_eight_io = generate_masked_vector.generate_seven_eight(i)
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
    for i in vectors:
        i = i.replace('[','').replace(']','').replace(',',"").replace(" ","")
        i = list(i)
        all_masked = create_masked(i)
        for masked in all_masked:
            masked = ''.join(masked)
            dict[masked]= dict[masked]+1
    return dict
