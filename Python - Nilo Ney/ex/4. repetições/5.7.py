# Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10.
n = int(input('Tabuada de: '))
v = int(input('Tabuada de {} até quanto? '.format(n)))
x = 1
while x <= v:
    print('{} x {} = {}'.format(n, x, n * x))
    x = x + 1
    
