# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o valor do seu salário: '))
if salario > 1250:
    aumento = salario + (salario * 10/100)
    print('O seu salário era R${:.2f} e com o aumento de 10% passou a ser {:.2f} reais'.format(salario, aumento))
else:
    aumento = salario + (salario * 15/100)
    print('O seu salário era R${:.2f} e com o aumento de 15% passou a ser {:.2f} reais'.format(salario, aumento))
