'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa.
'''
import math

co = float(input('Valor do Cateto Oposto: '))
ca = float(input('Valor do Cateto Adjacente: '))
hip = math.hypot(ca, co)
print('Cateto Op. é {}, Cateto Adj. é {} e a hipotenusa é igual a {:.2f}!'.format(co, ca, hip))
