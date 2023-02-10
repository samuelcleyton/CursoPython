# Faça um programa que leia 5 números e informe a soma e a média dos números. 

contador = 1
acumulador = 0

while contador <= 5:
    n = int(input('Digite o {}° número: '.format(contador)))
    acumulador = acumulador + n
    contador = contador + 1

print()
print('A soma de todos os valores é igual a {}'.format(acumulador))
print('A média dos números é igual a {}'.format(acumulador/5))
