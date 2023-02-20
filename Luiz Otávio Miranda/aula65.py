"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

# def Print():
#    print('Várias1')
#    print('Várias2')
#    print('Várias3')
#    print('Várias4')

def imprimir(a, b, c): # parâmentros
    print(a, b, c)

imprimir(1, 2, 3) # valores
imprimir(4, 5, 6) # valores


def saudação(nome = 'Sem nome'):
    print(f'Olá, {nome}!')

saudação('Samuel')
saudação('Adriely')
saudação()

