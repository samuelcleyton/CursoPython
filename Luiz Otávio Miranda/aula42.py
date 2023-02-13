frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
        'Python foi criado por Guido van Rossum.'

# print(frase.count('a')) # serve para contar quantas letras 'a' aparece na frase

i = 0
apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue

    qtd_letra = frase.count(letra_atual)

    if apareceu_mais_vezes < qtd_letra:
        apareceu_mais_vezes = qtd_letra
        letra_que_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_que_apareceu_mais_vezes}" que apareceu '
    f'{apareceu_mais_vezes}x'
)