
def get_masked_vectors_that_covers_vector_riccardo(eight_eight_vector, vector):
    covering = {}
    for key, value in vector.items():
        if (eight_eight_vector!=key):
            if check_if_cover(key, eight_eight_vector):
                covering[key]=value
    return covering

def get_max_masked_vectors_that_covers_vector_riccardo(vector, all_masked):

    # covering = {}
    # max = 0
    # max_key = ''
    # for key, value in dict.items():
    #     if (eight_eight_vector!=key):
    #         if check_if_cover(key, eight_eight_vector):
    #             covering[key]=value
    #             if value > max:
    #                 max = value
    #                 max_key = key
    # return max_key
    tmp = (0,-1)
    for masked in all_masked:
        if check_if_cover(vector, masked[0]):

            if(masked[1]>tmp[1]):
                tmp = masked
    print(''.join(tmp[0]))
    return ''.join(tmp[0])

def check_if_cover(eight_eight_vector,masked_vector):
    bool = True
    for i in range(len(eight_eight_vector)):
        if (eight_eight_vector[i] == "*") or (masked_vector[i] == "*") or (eight_eight_vector[i] == masked_vector[i]):
            bool = True
        else:
            bool = False
            break
    return bool


