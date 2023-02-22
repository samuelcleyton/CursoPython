"""
Retorno de valores das funções (return)
"""

def soma(x, y):
    if x > 10:
        return 10
    
    return x + y # retorna o valor e dá possibilidade de utilizar o mesmo valor

soma1 = soma(2, 2)
soma2 = soma(3, 3)

print(soma1 + soma2)

# print dentro da função apenas exibe o valor na tela do tipo None (não é possível utilizá-lo)


