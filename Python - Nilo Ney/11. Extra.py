cpf = input('Digite o seu CPF: ')
nove_digitos = cpf[:9]

count_1 = 10
soma_1 = 0

count_2 = 11
soma_2 = 0

try:
    cpf_int = int(nove_digitos)
    
    novo_cpf = [nove_digitos]

    for digitos in nove_digitos:
        multi_1 = int(digitos) * count_1
        soma_1 = soma_1 + multi_1
        count_1 = count_1 - 1

    for numeros in novo_cpf:
        multi_2 = int(numeros) * count_2
        soma_2 = soma_2 + multi_2
        count_2 = count_2 - 1

    resultado_1 = (soma_1 * 10) % 11
    resultado_2 = (soma_2 * 10) % 11

    if resultado_1 <= 9:
        novo_cpf.append(str(resultado_1))
    else:
        novo_cpf.append('0')

    if resultado_2 <= 9:
        novo_cpf.append(str(resultado_2))
    else:
        novo_cpf.append('0')

except:
    print('Digite apenas números!')

cpf_completo = ''.join(novo_cpf)
print(cpf_completo)
