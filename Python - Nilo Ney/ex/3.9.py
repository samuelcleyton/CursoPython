# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. 
# Calcule o total em segundos.

dias = int(input('Digite a quantidade de dias: '))
horas = int(input('Digite a quantidade de horas: '))
minutos = int(input('Digite a quantidade de minutos: '))
segundos = int(input('Digite a quantidade de segundos: '))
total_segundos = dias * 86400 + horas * 3600 + minutos * 60 + segundos
print('O total em segundos é de %d' % (total_segundos))
