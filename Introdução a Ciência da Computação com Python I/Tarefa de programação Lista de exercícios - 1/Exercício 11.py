# Receba 3 números inteiros na entrada e imprima "crescente" se eles forem dados em ordem crescente.
# Caso contrário, imprima "não está em ordem crescente"

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n2 == n1 + 1 and n3 == n2 + 1:
    print('crescente')
else:
    print('não está em ordem crescente')
