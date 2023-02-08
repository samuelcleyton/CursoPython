# Faça um programa que leia a largura e a altura de uma parede em metros,
# Calcule a sua área e a quantidade de tinta necessária para pintá-lo.
# Sabendo que cada litro de tinta, pinta um área de 2m quadrados.

lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

área = lar * alt
litro = área / 2

print('A área dessa parede é de {:.2f} m², serão necessários {} litros de tinta para pintá-la!'.format(área, litro))

