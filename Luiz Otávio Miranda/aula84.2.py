# Filtro de dados em list comprehension (filter)

import pprint # organiza como o print será exibido na tela

def p(v):
    pprint.pprint(novos_produtos, sort_dicts=False, width=40)

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# print(*novos_produtos, sep = '\n')
# p(novos_produtos)

lista = [n for n in range(10) if n < 5] # o que vem na direita é mapeamento, na esquerda é filtro
print(lista)

# filtro significa que pode incluir o valor ou não na lista

