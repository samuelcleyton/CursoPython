"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# lembre-se do desempacotamento

x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# def soma(x, y):
#    return x + y

def soma(*args): # empacota o que eu enviar para função dentro de uma tupla
    print(args)
    total = 0
    for numero in args:
        total = total + numero
    return total

soma1_2_3 = soma(1, 2, 3)
print(soma1_2_3)

# print(sum((1, 2, 3, 4, 5, 6))) # sum soma diretamente vários valores 

numeros = 1, 2, 3, 4, 5, 6
outra_soma = soma(*numeros) # desempacota uma tupla
print(outra_soma)

print(sum(numeros))
