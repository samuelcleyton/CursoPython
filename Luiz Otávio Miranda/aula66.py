"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y): # parâmentos são as variáveis
    print(f'{x} + {y} = {x + y}')

soma(1, 2) # argumentos são os valores atribuídos a função - argumentos não nomeados
soma(y = 1, x = 2) # argumentos nomeados

print(1, 2, sep='-')

# A regra é clara: você não pode enviar argumentos posicionais após argumentos nomeados
# exemplo: soma(y = 1, 2) 
