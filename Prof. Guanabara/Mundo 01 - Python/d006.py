# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))

d = n * 2
t = n * 3
r = n ** (1/2)

print('O número digitado foi {}, \no seu dobro é {}, \no seu triplo é {} \ne a raiz quadrada é {}.'.format(n, d, t, r))

