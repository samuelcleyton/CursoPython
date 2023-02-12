# Operadores in e not

# in - está entre 
# not in - não está entre

# Strings são iteráveis

#  0 1 2 3 4 5 
#  S a m u e l
# -6-5-4-3-2-1
'''
nome = 'Samuel'
print(nome[2])

print('m' in nome) # se a letra m está entre as letras do nome, retorna um valor bool

print('muel' not in nome) # se muel não está entre nome? como está o valor retornado será falso

'''

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
    
