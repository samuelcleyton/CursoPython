'''
while <condição>:
    'enquanto essa condição for verdadeira, faça isso!'
sempre checa a condição e continua executando o bloco de dentro até que passe a ser falsa.

x = 0
while x < 100: # a variável x recebe 0, sempre somando + 1
    print(x)
    x = x + 1
print('Acabou') # importante frizar que o print está for do bloco while e só será executado depois que a condição for falsa.

# quando x valer 99, ainda será impresso na tela, porém quando chegar a 100, a condição já não é mais válida.

continue - no laço while: sempre que houver a pralavra "continue" não será executado o que está abaixo do código.

x = 0
while x < 10:
    if x == 3: # não será impresso o número 3.
        x = x + 1
        continue
    
    print(x)
    x = x + 1

break - no laço while: finaliza o loop.

laço de repetição é basicamente um círculo que se repete que também podemos colocar outras condições dentro do mesmo laço.

x = 0 # coluna
while x < 10:
    y = 0 # linhas

    while y < 5:
        print('{}, {}'.format(x, y))
        y = y + 1
    
    x = x + 1
print('Acabou!')

nesse exemplo, temos dois laços de repetições, o 1° que informa que enquanto x < 10 ele vai repetir 5x o segundo bloco.

'''



