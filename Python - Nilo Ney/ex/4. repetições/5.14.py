# Escreva um programa que leia números inteiros do teclado. 
# O programa deve ler os números até que o usuário digite 0 (zero).
# No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

soma = 0
quantidade = 0
while True:
    v = int(input('Digite um número inteiro: '))
    if v == 0:
        break
    soma = soma + v
    quantidade = quantidade + 1
print('Quantidade de números digitados {}'.format(quantidade))
print('Soma: {}'.format(soma))
print('Média: {}'.format(soma/quantidade))
