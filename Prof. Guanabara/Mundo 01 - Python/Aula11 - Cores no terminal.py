'''
# Padrão ANSI - escape sequence

# \033[m - entre o colchetes e o "m"
# 1° estilo da fonte
# 2° cor do texto
# 3° cor do fundo

\033[0;33;44m

# códigos para estilo: 0, 1, 4, 7
0 = normal
1 = negrito
4 = sublinhado
7 = inverte cor da letra pra fundo e vice e versa.

# códigos para cores do texto: 30 até 37
30 = branco
31 = vermelho
32 = verde
33 = amarelo
34 = azul
35 = rosa
36 = azul marinho
37 = cinza

# códigos para fundo: 40 até 47

40 = branco
41 = vermelho
42 = verde
43 = amarelo
44 = azul
45 = rosa
46 = azul marinho
47 = cinza

'''

print('\033[31mSamuel Cleyton Macena de Oliveira')
# para tirar a faixa no final, é necessário adicionar \033[m no final da string
print('\033[34;47mSamuel\033[m')
a = 2
b = 3
print('Os valores são \033[34m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
# utilizando o format
nome = 'Samuel'
print('Olá, prazer em te conhecer, {}{}{}!!!'.format('\033[34m', nome, '\033[m'))


