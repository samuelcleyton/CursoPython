# (Parte 1) Métodos úteis nos dicionários Python (dict)

# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Samuel Cleyton',
    'sobrenome': 'Macena de Oliveira',
    # 'idade': 22   
}

# se a chave idade não existe o setdefault adiciona um valor

pessoa.setdefault('idade', 25)
print(pessoa['idade'])

# print(len(pessoa))
print(list(pessoa.keys())) # mostra as chaves do dicionário
print(list(pessoa.values())) # mostra os valores das chaves
print(list(pessoa.items())) # mostra chaves e valores

for valor in pessoa.values(): # for para utilizar cada iterável
    print(valor)

for chave, valor in pessoa.items(): # Enumerate
    print(chave, valor)
