# Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. 
# Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.
# Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima "longe" na saída.
# Caso contrário, quando a distância for menor que 10, imprima perto. 

import math

x1 = float(input('Digite o valor da coordenada x1: '))
y1 = float(input('Digite o valor da coordenada y1: '))
x2 = float(input('Digite o valor da coordenada x2: '))
y2 = float(input('Digite o valor da coordenada y2: '))

d = (x1 - x2) ** 2 + (y1 - y2) ** 2
d1 = math.sqrt(d)

if d1 >= 10:
    print('longe')
else:
    print('perto')


