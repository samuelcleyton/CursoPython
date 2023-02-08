# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
# Regra 1: Anos divisíveis por 4, menos se terminarem em '00'.
# Regra 2: Só são bissextos se forem divisíveis por 400.

import datetime
ano = int(input('Qual ano você quer analisar? '))
if ano == 0:
    ano = datetime.date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO!'.format(ano))





