from collections import defaultdict


def covers(key, vector):
    _key = key.replace('[','').replace(']','').replace(',',"").replace(" ","")
    _vector = vector.replace('[','').replace(']','').replace(',',"").replace(" ","")
    bool = True
    for char1, char2 in zip(_key, _vector):
        if (char1 == '*') or (char2 == '*') or (char1 == char2):
            bool = True
        else:
            bool = False
            break
    return bool

def decrement_counts(dict):
    dict=sorted(dict.items(), key = lambda kv: kv[1])
    i=0
    for (key, value) in dict:
        if i>0:
            value=value-1
        i+=1
        #dict[key] = value
    return dict

def get_masked_vectors_that_covers_vector(dict_masked_vectors, vector):
    dict_masked_vectors_cover = defaultdict(int)
    for key, value in dict_masked_vectors.items():
        if covers(key, vector):
            dict_masked_vectors_cover[key]=value
    return dict_masked_vectors_cover