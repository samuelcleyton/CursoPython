# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar
# ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
sexo = str(input('Qual é o seu sexo? \nMasculino ou Feminino? ')).lower()
ano = int(input('Informe o ano em que você nasceu: '))
idade = datetime.date.today().year - ano
alistamento = 18 - idade

if sexo == 'feminino':
    print('Você não precisa se alistar. ')

elif idade < 18:
    print('Quem nasceu em {} tem {} anos.'.format(ano, idade))
    print('Ainda faltam {} ano(s) para o seu alistamento.'.format(alistamento))
    print('O seu alistamento será em {}.'.format((datetime.date.today().year + (18 - idade))))

elif idade == 18:
    print('Quem nasceu em {} tem {} anos.'.format(ano, idade))
    print('Está na hora de se alistar.')
    print('O seu alistamento é nesse ano de {}.'.format(datetime.date.today().year))
else:
    print('Quem nasceu em {} tem {} anos.'.format(ano, idade))
    print('Você deveria ter se alistado há {} ano(s).'.format(-alistamento))
    print('Você deveria se alistar no ano de {}.'.format(datetime.date.today().year + (18 - idade)))




