# Dada uma sequência de números inteiros diferentes de zero, terminada por um zero, calcular a sua soma.

soma = 0

while True:
    n = int(input('digite um número inteiro: '))
    if n == 0:
        print(soma)
        break
    else: 
        soma = soma + n