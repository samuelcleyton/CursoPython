""" Calculadora com While """

while True:
    n1 = input('Primeiro número: ')
    n2 = input('Segundo número: ')
    operador = input('Operador: ')

    try:
        n1_float = float(n1)
        n2_float = float(n2)
        
        if operador == '+':
            print(f'{n1} + {n2} = {n1_float + n2_float}')
        elif operador == '-':
            print(f'{n1} - {n2} = {n1_float - n2_float}')
        elif operador == '*':
            print(f'{n1} * {n2} = {n1_float * n2_float}')
        elif operador == '/':
            print(f'{n1} / {n2} = {n1_float / n2_float}')
        else:
            print('Operador inválido!')
        
        sair = str(input('Deseja sair [S/N]? '))
        sair = sair.strip().lower()
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

# startswith('s') - se a letra começa com s
# endswith('s') - se a letra termina com s


try: # má prática de programação: try and except
    ...
except Exception as error:  
    print(error) # serve para identificar o tipo de error.

##### resposta do professor!

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta. Confira o resultado abaixo:')
    
    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)
    elif operador == '/':
        print(num_1_float / num_2_float)
    else:
        ...

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break


