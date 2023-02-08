# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.
soma_idade = 0
maioridade_homem = 0
nome_velho = ''
tot_mulher = 0

for c in range(1, 5):
    print('-' * 5, '{}° pessoa'.format(c), '-' * 5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]? '))
    soma_idade = soma_idade + idade
    if c == 1 and sexo in 'Mm':
        maioridade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maioridade_homem:
        maioridade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        tot_mulher = tot_mulher + 1

media = soma_idade / 4

print('A média de idade do grupo é {} anos.'.format(media))
print('O homem mais velho se chama {} e tem {} anos.'.format(nome_velho, maioridade_homem))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(tot_mulher))
