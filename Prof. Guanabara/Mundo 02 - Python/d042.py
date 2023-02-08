# Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isóceles: dois lados iguais, um diferente
# Escaleno: todos os lados diferentes

n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('Os segmentos PODEM formar um triângulo', end=' ')
    if n1 == n2 == n3:
        print('Equilátero.')
    elif n1 != n2 != n3 != n1:
        print('Escaleno.')
    else:
        print('Isóceles.')
else:
    print('Os segmentos não PODEM formar um triângulo.')

