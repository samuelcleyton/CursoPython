# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input('Digite algo: ')
print('O tipo primitivo de {} é {}'.format(n, type(n)))
print('É maiúsculo? {}'.format(n.isupper()))
print('É minúsculo? {}'.format(n.islower()))
print('É numérico? {}'.format(n.isnumeric()))
print('É alfabético? {}'.format(n.isalpha()))
print('É alfanumérico? {}'.format(n.isalnum()))
print('Está capitalizado? {}'.format(n.istitle()))



