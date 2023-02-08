# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
import time
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
print('Analisando...')
time.sleep(3)
print('Os números digitados foram {}, {} e {}.'.format(n1, n2, n3))
print('O maior é {}.'.format(max(n1, n2, n3)))
print('O menor é {}.'.format(min(n1, n2, n3)))



