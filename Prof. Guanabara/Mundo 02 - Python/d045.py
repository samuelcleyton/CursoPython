# Crie um programa que faça o computador jogar Jokenpô com você.
# pedra: ganha da tesoura e perde para o papel
# tesoura: ganha do papel e perde para a pedra
# papel: ganha da pedra e perde para a tesoura

import random
import time
jogador = str(input('Pedra, Papel ou Tesoura? ')).lower().strip()
cpu = ['pedra', 'papel', 'tesoura']
escolha = random.choice(cpu)
time.sleep(1)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')

print('-' * 25)
print('O computador jogou {}'.format(escolha))
print('O jogador jogou {}'.format(jogador))
print('-' * 25)

if jogador == escolha:
    print('EMPATE!')
elif jogador == 'pedra':
    if escolha == 'papel':
        print('COMPUTADOR VENCE')
    elif escolha == 'tesoura':
        print('JOGADOR VENCE')
elif jogador == 'papel':
    if escolha == 'pedra':
        print('JOGADOR VENCE')
    elif escolha == 'tesoura':
        print('COMPUTADOR VENCE')
elif jogador == 'tesoura':
    if escolha == 'pedra':
        print('COMPUTADOR VENCE')
    elif escolha == 'papel':
        print('JOGADOR VENCE')
else:
    print('Código inválido. Tente novamente!')






