# List comprehension em Python
# List comprehension é uma forma rápida de criar listas
# a partir de iteráveis

lista = []

for numero in range(10):
    lista.append(numero)

# print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
print(lista)

