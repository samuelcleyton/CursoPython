'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
'''

import random

alunos = ['Samuel', 'Adriely', 'Adryan', 'Socorro']
sorteio = random.choice(alunos)
print('O aluno sorteado foi {}!'.format(sorteio))

