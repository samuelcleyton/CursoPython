# Operadores Lógicos
# and (e) or (ou) not(não)

# and - todas as condições precisam ser verdadeiras
# se qualquer valor for considerado falso, a expressão inteira será falsa
# são considerados falsy - 0, 0.0 ''

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Digite a senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

print(True and True)

