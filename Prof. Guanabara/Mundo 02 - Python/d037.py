# Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

import math
n = int(input('Digite um número inteiro: '))
base = int(input('Qual base: \n[1] BINÁRIO \n[2] OCTAL \n[3] HEXADECIMAL \n'))

if base == 1:
    binario = bin(n)
    print('O número digitado foi {} e a sua conversão para binário é {}'.format(n, binario[2:]))
elif base == 2:
    octal = oct(n)
    print('O número digitado foi {} e a sua conversão para octal é {}'.format(n, octal[2:]))
elif base == 3:
    hexadecimal = hex(n)
    print('O número digitado foi {} e a sua conversão para hexadecimal é {}'.format(n, hexadecimal[2:]))
else:
    print('Opção inválida! Tente novamente!')
