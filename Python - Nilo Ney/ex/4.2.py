# Escreva um programa que pergunte a velocidade do carro de um usuário.
# Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado.
# Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80km/h.
'''
velocidade = int(input('Qual é a sua velocidade? '))
multa = (velocidade - 80) * 5
if velocidade > 80:
    print('Você foi multado! O preço da multa é de {} reais.'.format(multa))
if velocidade < 80 :
    print('Parabéns, você está no limite permitido de velocidade! ')
'''    

# Quem ganha menos de 1.000,00 não paga imposto de renda
# Entre 1.000,00 e 3.000,00 pagam 20%
# Acima de 3.000,00 pagam 35%

salario = float(input('Digite o valor do seu salário: '))
base = salario
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
    print('O valor do salário é {}, o valor do imposto é {:2.f} reais!'.format(salario, imposto))
