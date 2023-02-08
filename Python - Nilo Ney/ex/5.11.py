# Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
# Exiba os valores mês a mês para os 24 primeiros meses. 
# Escreva o total ganho com juros no período. 

depósito = float(input('Depósito inicial: '))
taxa = float(input('Taxa de Juros em %: '))

contador = 1
acumulador = 0

while contador <= 24:
    acumulador = acumulador + (taxa * depósito / 100)
    rendimento = depósito + acumulador
    print('{} mês rendeu {} reais'.format(contador, rendimento))
    contador = contador + 1



