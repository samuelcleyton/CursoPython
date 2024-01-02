'''Reescreva o programa contaSegundos para imprimir também a quantidade de dias, ou seja, faça um programa em Python que, dada a quantidade de segundos, 
"quebre" esse valor em dias, horas, minutos e segundos. A saída deve estar no formato: a dias, b horas, c minutos e d segundos. '''

número = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dias = número // 86400
seg_restantes = número % 86400
horas = seg_restantes // 3600
seg_restantes = número % 3600
minutos = seg_restantes // 60
seg_restantes_final = seg_restantes % 60

print(f'{dias} dias, {horas} horas, {minutos} minutos e {seg_restantes_final} segundos.')
