
'''data un alista di tuple ed una tupla (chiave, valore) aggiorna il valore relativo alòla chiave nella lista'''
def update_value(list, tuple):
    flag = False
    for elem in list:
        if elem[0] == tuple[0]:
            elem[1] = tuple[1]
            flag = True
    if flag == False:
        list.append(tuple)
    return list