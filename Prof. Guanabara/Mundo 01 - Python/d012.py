# Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Preço do produto? '))
desconto = produto - (produto * 5/100)

print('O preço do produto é {:.2f} reais, mas com o desconto de 5% sai por {:.2f} reais!'.format(produto, desconto))
