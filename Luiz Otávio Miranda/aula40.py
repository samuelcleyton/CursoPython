""" Calculadora com While """

while True:
    n1 = input('Primeiro número: ')
    n2 = input('Segundo número: ')
    operador = input('Operador: ')

    try:
        n1_int = int(n1)
        n2_int = int(n2)
        
        if operador == '+':
            print(f'{n1} + {n2} = {n1_int + n2_int}')
        elif operador == '-':
            print(f'{n1} - {n2} = {n1_int - n2_int}')
        elif operador == '*':
            print(f'{n1} * {n2} = {n1_int * n2_int}')
        elif operador == '/':
            print(f'{n1} / {n2} = {n1_int / n2_int}')
        else:
            print('Operador inválido!')
        
        sair = str(input('Deseja sair [S/N]? ')).strip().lower()
        if sair == 's':
            break
        else:
            continue
    except:
        if not n1.isdigit():
            print(f'{n1} não é um número válido')
        elif not n2.isdigit():
            print(f'{n2} não é um número válido')
        else:
            print('Digite um número!') 

