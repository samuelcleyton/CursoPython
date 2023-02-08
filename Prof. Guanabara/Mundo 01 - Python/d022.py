# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas
# Quantas letras ao todo sem considerar espaços
# Quantas letras tem o primeiro nome.


nome = str(input('Digite o seu nome completo: ')).strip()
print('nome em letras maiúsculas: {}.'.format(nome.upper()))
print('nome em letras minúsculas: {}.'.format(nome.lower()))
print('quantidade de letras sem considerar os espaços: {} letras.'.format(len(''.join(nome.split()))))
dividido = nome.split()
print('quantidade de letras no primeiro nome: {} letras.'.format((len(dividido[0]))))

