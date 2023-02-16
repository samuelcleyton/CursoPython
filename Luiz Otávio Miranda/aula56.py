"""
split e join com list e str
split - divide uma string
join - une uma string

"""

frase = '   Olha só que, coisa interessante'
lista_palavras = frase.split(',')  # quebra na vírgula! * lista de frases
lista_frase = []

for i, frase in enumerate(lista_palavras):
    lista_frase.append(lista_palavras[i].strip())

# print(lista_palavras)
# print(lista_frase)

frases_unidas = '-'.join(lista_frase)
print(frases_unidas)








