# Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2...
n = int(input('Tabuada de: '))
x = 1
while x <= 10:
    print('{} x {} = {}'.format(n, x, n * x))
    x = x + 1 
