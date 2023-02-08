# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
# maioridade > 21

import datetime
totmaior = 0
totmenor = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = datetime.date.today().year - ano
    if idade <= 21:
        totmenor = totmenor + 1
    else:
        totmaior = totmaior + 1
print('Ao todo tivemos {} pessoas menores de idade'.format(totmenor))
print('E também tivemos {} pessoas maiores de idade'.format(totmaior))


