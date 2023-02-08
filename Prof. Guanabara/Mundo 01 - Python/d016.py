'''
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
ex: 6.127 tem a parte inteira 6.
'''

import math
n = float(input('Digite um número qualquer: '))
pi = math.trunc(n)
print('O número digitado foi {} e a sua parte inteira é {}!'.format(n, pi))
