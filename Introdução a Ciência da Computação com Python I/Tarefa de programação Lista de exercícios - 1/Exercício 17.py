# Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída.

n = int(input('digite um número inteiro: '))

dígito = 0
soma = 0

while n > 0: 
    dígito = n % 10
    soma = soma + dígito
    n = n // 10
    dígito = dígito + 1

print(f'{soma}')
