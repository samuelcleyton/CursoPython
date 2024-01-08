# Receba um número inteiro positivo na entrada e imprina os n primeiros números ímpares naturais. 
# Para a saída, siga o formato do exemplo abaixo. 

n = int(input('digite um número inteiro positivo: '))

i = 1
contador = 1

while n >= contador: 
    print(i)
    i = i + 2
    contador = contador + 1
