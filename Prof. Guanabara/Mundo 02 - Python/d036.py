# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('=-' * 10)
print('\033[36mEMPRESTIMO BANCÁRIO: \033[m')
print('=-' * 10)

casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o valor do seu salário? '))
anos = int(input('Em quantos anos você pretende pagar? '))

parcela = casa / (anos * 12)
minimo = salario * 30/100

if parcela <= minimo:
    print('Empréstimo concedido! O valor da parcela será de R${:.2f}'.format(parcela))
else:
    print('Empréstimo negado! O valor da parcela seria R${:.2f}, acaba excedendo 30% do seu salário!'.format(parcela))



















