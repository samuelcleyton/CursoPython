# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

import time
velocidade = float(input('Qual é a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
print('Analisando...')
time.sleep(2)
if velocidade <= 80:
    print('Tenha um bom dia! Dirija com segurança.')
else:
    print('Multado! Você excedeu o limite permitido que é de 80km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
