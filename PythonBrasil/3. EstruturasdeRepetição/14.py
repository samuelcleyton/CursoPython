# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares. 

contador_par = 0
contador_impar = 0

for c in range(1, 11):
    n = int(input('Digite o {}° número inteiro: '.format(c)))
    if n % 2 == 0:
        contador_par += 1
    else:
        contador_impar += 1

print('Foram digitados {} números pares e {} números ímpares!'.format(contador_par, contador_impar))




    