# Escreva a função maximo que recebe 2 números inteiros como parâmeto e devolve o maior deles.

def maximo(x, y):
    if x > y:
        return x
    else:
        return y

x = int(input('digite um número inteiro: '))
y = int(input('digite outro número inteiro: '))

print(maximo(x, y))