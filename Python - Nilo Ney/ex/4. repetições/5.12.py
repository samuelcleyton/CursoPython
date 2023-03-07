# Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
# Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.

depósito = int(input('Depósito inicial: '))
aportes = int(input('Aportes mensais: '))
taxa = int(input('Taxa de juros em %: '))

contador = 1
acumulador = 0

while contador <= 24:
    acumulador = acumulador + (depósito * taxa / 100) + aportes   
    rendimento = depósito + acumulador
    print('{} mês rendeu {} reais'.format(contador, rendimento))
    contador = contador + 1
