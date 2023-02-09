# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    user = str(input('usuário: '))
    senha = str(input('senha: '))
    if user == senha:
        print('a senha não pode ser igual ao nome do usuário!')
    else:
        print('senha cadastrada!')
        break
