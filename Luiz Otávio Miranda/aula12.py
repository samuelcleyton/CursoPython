nome = 'Samuel'
altura = 1.70
peso = 62
imc = peso / altura ** 2

print(nome, 'tem', altura, 'de altura,', end='\n')
print('pesa', peso, 'quilos e o seu IMC é', end='\n')
print(imc)

print(...) # Ellipsis

'f-strings'

print(f'{nome} tem {altura:.2f} de altura,')
print(f'pesa {peso} quilos e o seu IMC é:')
print(f'{imc:.2f}')

