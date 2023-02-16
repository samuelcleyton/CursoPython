# Desempacotamento em chamadas
# de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

# p, b, *_, u = lista
# print(p, u)

# for nome in lista:
#   print(nome, end=' ') # com espaço fica na mesma linha 

print(*lista)
print(*string)
print(*lista, sep='\n')
