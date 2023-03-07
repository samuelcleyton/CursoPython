# Escreva um programa que leia três números e que imprima o maior e o menor. 
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

maior = max(a, b, c)
menor = min(a, b, c)

print('O valor maior é {} e o menor é {}!'.format(maior, menor))
