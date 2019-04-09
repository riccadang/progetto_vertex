import clustering_service_corretto


def get_masked_vectors_that_covers_vector(eight_eight_vector, vector):
    covering = {}
    for key, value in vector.items():
        if (eight_eight_vector!=key):
            if check_if_cover(key, eight_eight_vector):
                covering[key]=value
    return covering

def get_max_masked_vectors_that_covers_vector(vector, all_masked):
    vectors = clustering_service_corretto.find_all_covering_vectors(all_masked,vector)
    max = sorted(vectors,key=lambda x: x[1], reverse=True)[0]
    return ''.join(max[0])

def check_if_cover(eight_eight_vector,masked_vector):
    bool = True
    for i in range(len(eight_eight_vector)):
        if (eight_eight_vector[i] == "*") or (masked_vector[i] == "*") or (eight_eight_vector[i] == masked_vector[i]):
            bool = True
        else:
            bool = False
            break
    return bool


