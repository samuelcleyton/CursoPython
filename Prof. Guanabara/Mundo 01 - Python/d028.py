# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import time
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
sorteio = random.randint(0, 5)
n = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
time.sleep(3)
print('O número sorteado foi {}!'.format(sorteio))
if n == sorteio:
    print('Parabéns, você venceu!')
else:
    print('Não foi dessa vez :(')

