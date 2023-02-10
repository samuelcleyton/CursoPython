# Altere o programa anterior para mostrar no final a soma dos números. 

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
acumulador = 0

if n1 > n2:
    for c in range(n2 + 1, n1):
        print(c)
        acumulador = acumulador + c
else:
    for c in range(n1 + 1, n2):
        print(c)
        acumulador = acumulador + c

print('A soma dos números que estão no intervalo é igual {}.'.format(acumulador))



