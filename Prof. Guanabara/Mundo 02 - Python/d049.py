# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
cont = 0
num = int(input('Digite um número para ver a sua tabuada: '))
for c in range(1, 11):
    cont = cont + 1
    print('{} x {:^2} = {}'.format(num, cont, num * cont))