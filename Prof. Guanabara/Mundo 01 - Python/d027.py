#  Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()
separar = nome.split()
contagem = (len(separar)-1)
print('O seu primeiro nome é {}.'.format(separar[0]))
print('O seu último nome é {}.'.format(separar[contagem])) # format(separar[len(separar)-1])


# nome = str(input('Nome: '))
# separar = nome.split()
# final = (len(separar)-1)
# print(separar)
# print(separar[0])
# print(separar[final])

