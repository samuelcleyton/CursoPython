# if / elif / else
# se, se não se, se não

entrada = input('Você quer "entrar" ou "sair"? ')

# condição retorna True or False

if entrada == 'entrar': # será executado somente se a condição for verdadeira
    print('Você entrou no sistema!')
elif entrada == 'sair':
    print('Você saiu do sistema!')
else:
    print('Você não digitou nem entrar nem sair!')

print('FORA DO BLOCO!')


