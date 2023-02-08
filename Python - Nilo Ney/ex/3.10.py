# Faça um programa que calcule o aumento de um salário.
# Ele deve solicitar o valor e a porcentagem de aumento.
# Exiba o valor do aumento e do novo salário. 

salario = float(input('Digite o valor do seu salário: '))
aumento = int(input('Digite a porcentagem do aumento: '))
valor_aumento = salario * aumento / 100
novo_salario = salario + valor_aumento
print('O valor do salário era {}, mas recebeu um aumento de {}%, ou seja, {} reais. A partir de agora é {} reais'.format(salario, aumento, valor_aumento, novo_salario))


