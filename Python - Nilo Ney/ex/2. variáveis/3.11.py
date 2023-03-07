# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e o preço a pagar. 

mercadoria = float(input('Digite o preço da mercadoria: '))
desconto = float(input('Digite o percentual de desconto para hoje: '))
vdesconto = mercadoria * desconto / 100
preco = mercadoria - desconto
print('O desconto foi de %d reais, o preço a pagar é %d reais!' % (vdesconto, preco))
