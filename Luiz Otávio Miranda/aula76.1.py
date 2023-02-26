# Manipulando chaves e valores em dicionários

pessoa = {}

## 
##

chave = 'nome completo'

pessoa[chave] = 'Samuel'
pessoa['sobrenome'] = 'Oliveira'

print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome completo'])

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])

    