# Operadores Lógicos
# and (e) or (ou) not(não)

# or se qualquer valor for verdadeiro, a expressão será considerada verdadeira

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Digite a senha: ')

senha_permitida = '123456'

if entrada == 'E' or entrada == 'e' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

print(True or True)

senha = input('Senha: ') or 'Sem senha'
print(senha)
