# Escreva um programa que receba um número natural n a entrada e imprima n! (fatorial) na saída.

n = int(input('digite um número natural: '))

fatorial = 1

while n > 1:
    fatorial = fatorial * n
    n = n - 1

print(fatorial)
