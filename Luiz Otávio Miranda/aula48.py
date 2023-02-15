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


lista = [10, 20, 30, 40]
lista[2] = 300
del lista[2] # apaga um valor da lista
print(lista)
lista.append(50) # adiciona um valor na lista
lista.pop(3) # remove o último elemento da lista, agora remove o índice 3 da lista
print(lista)
'''

'''
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
'''
'''
lista = [10, 20, 30, 40]
lista.append('Samuel')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear() # limpra a lista
lista.insert(1, 12) # O primeiro valor é o indice, o segundo valor será inserido na lista
print(lista, nome)
'''
'''
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b # união das duas listas
d = a.extend(b) # não retornar nenhum valor, mas mexe diretamente com a lista a
print(a)
'''

'''
Cuidados com dados mutáveis
= - copiando o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)

'''

lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy() # copiando o valor da lista a

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)

