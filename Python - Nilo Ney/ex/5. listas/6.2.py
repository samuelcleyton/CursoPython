# Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.

l1 = []
l2 = []

while True:
    n1 = int(input('Digite um número para a lista 1 (0 para sair): '))
    if n1 == 0:
        break
    l1.append(n1)

while True:
    n2 = int(input('Digite um número para a lista 2 (0 para sair): '))
    if n2 == 0:
        break
    l2.append(n2)

l3 = l1 + l2
print(f'A lista 3 é composta por {l3}')

