# (Parte 2) Métodos úteis nos dicionários Python (dict)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

p1 = {
    'nome': 'Samuel',
    'sobrenome': 'Oliveira',
}

# print(p1['nome']) # se não tiver, acontecer o KeyError
# print(p1.get('nome', 'Não existe')) # se tiver, retorna o valor, se não, retorna None

# nome = p1.pop('nome') # apaga um item com a chave especificada
# print(p1)

# ultima_chave = p1.popitem()
# print(p1)

p1.update({
    'nome': 'Cleyton',
    'idade': 30,
})
print(p1)

# p1.update(nome = 'Cleyton', idade = 30) *outra forma
