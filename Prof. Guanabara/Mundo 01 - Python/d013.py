# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salário = float(input('Digite o seu salário: '))
aumento = salário + (salário * 15/100)
print('O seu salário anterior era {:.2f} reais, com o aumento de 15% passou a ser {:.2f} reais!'.format(salário, aumento))

