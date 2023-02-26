# Shallow Copy vs Deep Copy em dados mutáveis Python
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2], # o que é multável, não é copiado
}

d2 = copy.deepcopy(d1) # cópia total sem afetar o outro dicionário.


d2['c1'] = 1000 # d2 é alterado, mas d1 dão é
d2['l1'][1] = 999

print(d1)
print(d2)

# listas e dicionários são mutáveis
# shallow copy ou cópia rasa não entra nos subníveis, por exemplo, se adicionar uma lista
# no dicionário, a lista será a mesma


