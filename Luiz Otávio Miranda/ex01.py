# Faça um programa que peça para o usuário digitar um número inteiro, informe se este número é par ou ímpar.
# Caso o usuário não digite um número inteiro, informe que não é um número inteiro.

n = input('Digite um número inteiro: ')

if n == str(n):
    print('Digite um número inteiro!')
elif n % 2 == 0:
    print('O número é par!')
else:
    print('O número é ímpar!')
