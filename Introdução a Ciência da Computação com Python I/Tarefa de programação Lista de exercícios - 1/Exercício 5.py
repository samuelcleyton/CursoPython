# Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas. 

número = int(input('Digite um número inteiro: '))
dezena = número // 10
dígito = dezena % 10

print(f'O dígito das dezenas é {dígito}')