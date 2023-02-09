# Faça um programa que leia e valide as seguintes informações:
# a. Nome: maior que 3 caracteres
# b. Idade: entre 0 e 150
# c. Salário: maior que zero
# d. Sexo: 'f' ou 'm'
# e. Estado Civil: 's', 'c', 'v', 'd'

while True:
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    salário = float(input('Salário: '))
    sexo = str(input('Sexo: [M/F] ')).lower()
    civil = str(input('Estado Civil: ')).lower()

    if len(nome) < 3:
        print('O nome precisa ter mais de 3 caracteres!')
        continue
    elif idade > 150 or idade < 0:
        print('Idade incorreta!')
        continue
    elif sexo not in 'mf':
        print('Sexo inválido!')
    elif civil not in 'scvd':
        print('Estado civil inválido')
    break
