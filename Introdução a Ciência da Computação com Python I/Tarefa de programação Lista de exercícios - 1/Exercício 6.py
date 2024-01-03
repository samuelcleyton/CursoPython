import math

a = float(input('qual é o valor de "a"? '))
b = float(input('qual é o valor de "b"? '))
c = float(input('qual é o valor de "c"? '))

delta = b ** 2 - 4 * a * c
print(f'delta vale {delta}')

if delta > 0:
    x1 = (- b + math.sqrt(delta)) / (2 * a) 
    x2 = (b + math.sqrt(delta)) / (2 * a)
    print(f'A primeira raiz vale {x1} e a segunda raiz vale {x2}')
elif delta == 0:
    x1 = -b / (2 * a)
    print(f'A equação possui apenas 1 raiz real = {x1}')
else:
    print('A equação não possui raízes reais.')





