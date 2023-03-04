# Empacotamento e desempacotamento de dicionários + *args e **kwargs

a, b = 1, 2
a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

a, b = pessoa.values() # values retorna o valor da chave
# print(a, b)
a, b = pessoa.items() # retorna chave e valores
# print(a, b)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

