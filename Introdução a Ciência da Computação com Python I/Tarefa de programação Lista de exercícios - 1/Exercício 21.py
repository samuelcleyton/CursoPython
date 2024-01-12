# Escreva a função maximo que recebe 2 números inteiros como parâmeto e devolve o maior deles.

def maximo(x, y):
    if x > y:
        return x
    else:
        return y

x = maximo(9, 12)
print(x)
