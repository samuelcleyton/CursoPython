"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
'''
texto = iter('Samuel')


print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
'''

# Erro: StopIteration  - quando esgotam os valores

texto = 'Luiz' # iterável
iterador = iter(texto) # iterador

while True:
    try: # tenta pegar o next do iterator
        letra = next(iterador)
        print(letra)
    except StopIteration: # quando o try gerar o erro, o código para.
        break


