# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, de 15%.

salario = float(input('Digite o valor do seu salário: '))
maior = salario + (salario * 0.10)
menorouigual = salario + (salario * 0.15)
if salario > 1250:
    print('O seu salário aumentou 10%, a partir de agora é {} reais'.format(maior))
if salario <= 1250:
    print('O seu salário aumento 15%, a partir de agora é {} reais'.format(menorouigual))
