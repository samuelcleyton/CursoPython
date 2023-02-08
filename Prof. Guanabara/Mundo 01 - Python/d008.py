# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Digite um valor em metros: '))

cen = metros * 100
min = metros * 1000

print('O valor digitado em metros foi {:.2f}, em centímetos é {:.2f} e em milímetros é {:.2f}'.format(metros, cen, min))
