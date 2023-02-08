'''
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada. 
'''

import random
alunos = ['Samuel', 'Adriely', 'Socorro', 'Adryan']
random.shuffle(alunos)
print('A sequência é {}'.format(alunos))

