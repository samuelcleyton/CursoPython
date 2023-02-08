# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
# Pergunte a quantidade de kWh consumida e o tipo de instalação: R, I e C.
# Calcule o preço a pagar de acordo com a tabela. 

energia = int(input('Digite o valor de kWh consumido: '))
instalação = str(input('Residência, Comércio ou Indústria?\n'))
valor = 0
'''
r1 = energia * 0.40
r2 = energia * 0.65
c1 = energia * 0.55
c2 = energia * 0.60
i1 = energia * 0.55
i2 = energia * 0.60
'''

if instalação == 'residência':
    energia <= 500
    print('O preço a ser pago é de {} reais.'.format(r1))
elif instalação == 'residência':
    energia > 500
    print('O valor a ser pago é {} reais.'.format(r2))
elif instalação == 'comércio':
    energia <= 1000
    print('O valor a ser pago é {} reais.'.format(c1))
elif instalação == 'comércio':
    energia > 1000
    print('O valor a ser pago é {} reais.'.format(c2))
elif instalação == 'indústria':
    energia <= 5000
    print('O valor a ser pago é {} reais.'.format(i1))
elif instalação == 'indústria':
    energia > 5000
    print('O valor a ser pago é {} reais.'.format(i2))
else:
    print('Código Inválido! Tente Novamente. ')
