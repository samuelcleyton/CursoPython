# Faça um programa que leia 5 números e informe o maior número.

c = 1
numeros = []
while c <= 5:
    n = int(input('Digite o {}° número: '.format(c)))
    numeros.append(n)
    c = c + 1

print('O maior número digitado foi {}'.format(max(numeros)))
