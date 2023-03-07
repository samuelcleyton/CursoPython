# Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto.
# Considere que pagam imposto pessoas cujo o salário é maior que R$ 1.200,00.

x = float(input('Digite o seu salário: '))
if x > 1200:
    print('Você deve pagar imposto!')
else:
    print('Você está isento do imposto!')

