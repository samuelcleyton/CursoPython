# Exercício com funções - Exercícios 
# Crie funções que duplicam, triplicam e quadriplicam
# o número recebido como parâmento
'''
def duplicar(numero):
    return numero * 2

def triplicar(numero):
    return numero * 3

def quadriplicar(numero):
    return numero * 4

print(duplicar(2))
print(triplicar(2))
print(quadriplicar(2))
'''

# outra forma que eu pensei para resolver o exercício

'''
def dup_tri_quad(n1, n2, n3):
    return n1 * 2, n2 * 3, n3 * 4

print(dup_tri_quad(2, 4, 6)) # retorna o valor em tuplas

'''

# resolução do professor

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = (criar_multiplicador(2))
triplicar = (criar_multiplicador(3))
quadriplicar = (criar_multiplicador(4))

print(duplicar(2))
print(triplicar(3))
print(quadriplicar(4))


