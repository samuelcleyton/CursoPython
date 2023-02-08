# A Confederação Nacional de Natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

import datetime
nas = int(input('Em que ano você nasceu? '))
idade = datetime.date.today().year - nas
print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Nadador - MIRIM')
elif idade < 9 or idade <= 14:
    print('Nadador - INFANTIL')
elif idade < 14 or idade <= 19:
    print('Nadador - JUNIOR')
elif idade < 19 or idade <= 25:
    print('Nadador - SÊNIOR')
else:
    print('Nadador - MASTER')
