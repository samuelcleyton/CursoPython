# Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo.
# Utilize apenas os operadores de soma e subtração para calcular o resultado.
# Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles.
# Assim, 4 x 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

p = int(input('Primeiro número: '))
s = int(input('Segundo número: '))
x = 1
resultado = 0

while x <= s: # O código vai se repetir 4x
    resultado = resultado + p 
    x = x + 1 
print('{} x {} = {}'.format(p, s, resultado))

