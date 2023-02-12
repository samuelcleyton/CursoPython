# Introdução ao try/except
'''
try - tenta executar o código
except - ocorreu algum erro ao tentar executar

'''

numero_str = input('Vou dobrar o número que você digitar: ')

# print(numero.isdigit()) # checa se digitou apenas números
try:
    print(f'str: {numero_str}')
    numero_float = float(numero_str) # Quando ocorrer o erro nessa linha, pula para o excepta
    print(f'float: {numero_float}')
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')

except:
    print('Isso não é um número!')

# Precisa errar o mais rápido possível para mandar para excessão!
# basicamente captura o erro!

