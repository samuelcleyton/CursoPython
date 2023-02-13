""" while/else """

string = 'Valor qualquer'

i = 0

while i < len(string):
    letra = string[i]

    print(letra)

    i += 1
else:
    print('O else foi executado!')

print('fora do while!')

# Quando o laço vai até o final, o else é executado.
# Casa haja um break no meio do while, o else não será executado!

'''
While / Else:
Contadores e Acumuladores

Contadores: como o próprio nome diz, serve para contar o número de vezes que o laço é executado.
Acumuladores: é usado para acumular o resultado de um operação ao longo de várias iterações no laço.

'''

contador = 1
acumulador = 1

while contador <= 10: 
    print(contador, acumulador)

    if contador > 5:  # quando o contador for 6, o laço será interrompido e executará o print que está fora do laço.
        break

    acumulador = acumulador + contador
    contador = contador + 1
else:  # o Else será executado somente quando a condição do while é falsa.
    print('Cheguei no ELSE') # se não tiver a linha 16, será feito o laço e no final mostrará o else.
print('Isso será executado!')


