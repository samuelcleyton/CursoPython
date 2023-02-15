"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, ler, alterar, apagar = lista [i] (GRUD)
"""
#        +01234 
#        -54321
'''
string = 'ABCDE' # 5 caracteres (len)

lista = [123, True, 'Luiz Otávio', 1.2, []]
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))
'''

lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2] # apaga um valor da lista
# print(lista)
lista.append(50) # adiciona um valor na lista
lista.pop(3) # remove o último elemento da lista, agora remove o índice 3 da lista
print(lista)
