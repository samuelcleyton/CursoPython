# Dictionary Comprehension e Set Comprehension

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'escritório'
}

dc = {
    chave: valor
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}

# print(dc)

s1 = {i ** 2 for i in range(10)}
print(s1)