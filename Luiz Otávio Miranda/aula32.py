"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num = input('Digite um número inteiro: ')

try: # usamos o try para forçar o erro! quando o usuário digitar algo que não seja um número, except é executado...
    n_int = int(num)
    if n_int % 2 == 0:
        print('O número digitado é PAR!')
    else:
        print('O número digitado é Ímpar!')
except:
    print('Digite apenas números')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Que horas são? ')

try:
    hora_int = int(hora)
    if 0 <= hora_int <= 11:
        print('Bom dia!')
    elif 12 <= hora_int <= 17:
        print('Boa tarde!')
    elif 18 <= hora_int <= 23:
        print('Boa noite!')
    else:
        print('Não conheço essa hora!')
except:
    print('Digite um número!')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite o seu nome: ')
letras = len(nome)
if 0 < letras <= 4:
    print('O seu nome é curto!')
elif 5 <= letras <= 6:
    print('O seu nome é normal!')
else:
    print('O seu nome é muito grande!')


