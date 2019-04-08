from collections import defaultdict


# def covers(key, vector):
#     _key = key.replace('[','').replace(']','').replace(',',"").replace(" ","")
#     _vector = vector.replace('[','').replace(']','').replace(',',"").replace(" ","")
#     bool = True
#     for char1, char2 in zip(_key, _vector):
#         if (char1 == '*') or (char2 == '*') or (char1 == char2):
#             bool = True
#         else:
#             bool = False
#             break
#     return bool

# def decrement_counts(dict):
#     dict=sorted(dict.items(), key = lambda kv: kv[1])
#     i=0
#     for (key, value) in dict:
#         if i>0:
#             value=value-1
#         i+=1
#         #dict[key] = value
#     return dict

# def get_masked_vectors_that_covers_vector(dict_masked_vectors, vector):
#     dict_masked_vectors_cover = defaultdict(int)
#     for key, value in dict_masked_vectors.items():
#         if covers(key, vector):
#             dict_masked_vectors_cover[key]=value
#     return dict_masked_vectors_cover

def get_masked_vectors_that_covers_vector_riccardo(eight_eight_vector, vector):
    covering = {}
    for key, value in vector.items():
        if (eight_eight_vector!=key):
            if check_if_cover(key, eight_eight_vector):
                covering[key]=value
    return covering

def get_max_masked_vectors_that_covers_vector_riccardo(eight_eight_vector, dict):
    covering = {}
    max = 0
    max_key = ''
    for key, value in dict.items():
        if (eight_eight_vector!=key):
            if check_if_cover(key, eight_eight_vector):
                covering[key]=value
                if value > max:
                    max = value
                    max_key = key
    return max_key

def check_if_cover(eight_eight_vector,masked_vector):
    bool = True
    for i in range(len(eight_eight_vector)):
        if (eight_eight_vector[i] == "*") or (masked_vector[i] == "*") or (eight_eight_vector[i] == masked_vector[i]):
            bool = True
        else:
            bool = False
            break
    return bool
