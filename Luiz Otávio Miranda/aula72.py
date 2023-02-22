# Exercícios com funções + Solução (prepare-se para pausar)
# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multi(*args):
    total = 1
    for numero in args:
        total = total * numero
    return total

m = multi(2, 4, 10)
print(m)

# Crie uma função que fala se um número é par ou ímpar
# Retorne se o número é par ou ímpar

def numero(x):
    
    if x % 2 == 0:
        return f'{x} é par!'
    else:
        return f'{x} é ímpar!'

print(numero(10))


