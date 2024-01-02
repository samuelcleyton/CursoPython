# Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado, 
# calcule e imprima (saída de dados) seu perímetro e sua área.

L = input('Digite o valor correspondente ao lado de um quadrado: ')
Lint = int(L)

perímetro = Lint * 4
área = Lint ** 2

print(f'perímetro: {perímetro} - área: {área}')