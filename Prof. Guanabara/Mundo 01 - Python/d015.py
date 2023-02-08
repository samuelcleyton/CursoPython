# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram percorridos? '))

valor = (dias * 60) + (km * 0.15)

print('O carro foi alguado por {} dias e percorreu {}km, o preço a ser pago é {:.2f} reais.'.format(dias, km, valor))
