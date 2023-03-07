# Escreva um programa que calcule o tempo de uma viagem de carro.
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem. 

distancia = int(input('Me informe a distância em km: '))
vm = int(input('Me informe a velocidade média para a viagem: '))
tempo = distancia / vm
minutos = tempo * 60
print('O tempo da viagem de carro é de %d minutos' % (minutos))
