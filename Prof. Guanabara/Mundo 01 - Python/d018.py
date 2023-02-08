# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente.
import math

a = int(input('Valor do ângulo em °: '))

sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))

print('O ângulo é {}°, o Seno vale {:.2f}°, Cosseno vale {:.2f}° e a Tangente vale {:.2f}°.'.format(a, sen, cos, tan))
