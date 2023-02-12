"""
Repetições
while (enquanto)

while <condição>:
    'enquanto essa condição for verdadeira, faça isso!
sempre checa a condição e continua executando o bloco de dentro até que passe a ser falsa.

Ctrl + c = interrompe a repetição do terminal
break - no laço while: finaliza o loop.

O laço de repetição é basicamente um círculo que se repete que também 
podemos colocar outras condições dentro do mesmo laço.

"""

condição = True

while condição: # loop infinito
    nome = input('Digite seu nome ou peça para sair: ')
    print(f'O seu nome é {nome}')
    
    if nome == 'sair':
        break # interrompe o código

print('Acabou')
