# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
# Você deve calcular a soma, subtração multiplicação e divisão. 
# Exiba o resultado da operação solicitada. 

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
operação = str(input('Qual operação você deseja realizar?\nSoma, Subtração, Multiplicação ou Divisão?\n')).strip().lower()
if operação == 'soma':
    soma = n1 + n2
    print('A soma entre {} e {} é igual a {}.'.format(n1, n2, soma))
elif operação == 'subtração':
    subtração = n1 - n2
    print('A subtração entre {} e {} é igual a {}.'.format(n1, n2, subtração))
elif operação == 'multiplicação':
    multiplicação = n1 * n2
    print('A multiplicação entre {} e {} é igual a {}.'.format(n1, n2, multiplicação))
elif operação == 'divisão':
    divisão = n1 / n2
    print('A divisão entre {} e {} é igual a {}.'.format(n1, n2, divisão))
else:
    print('Categoria inválida')
