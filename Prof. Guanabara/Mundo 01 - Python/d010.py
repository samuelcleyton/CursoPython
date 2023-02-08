# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Digite quanto você tem em reais: '))
dólares = real / 5.15

print('Com {:.2f} reais você pode trocar por {:.2f} dólares'.format(real, dólares))

