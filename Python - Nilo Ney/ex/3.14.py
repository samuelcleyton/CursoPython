# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado, assim como a quantidade de dias pelos quais o carro foi alugado. 
# Calcule o preço a pagar, sabendo que que o carro custa R$ 60 por dia e R$ 0,15 por km rodado. 

dias = int(input('Quantos dias o carro foi alugado? '))
km = int(input('Informe a quantidade de km percorridos: '))
preco = dias * 60 + km * 0.15
print('O valor a ser pago é R$ %.2f reais' % (preco))
