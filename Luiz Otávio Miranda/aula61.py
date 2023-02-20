"""
Calculo do primeiro dígito do CPF

CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7

Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7

****************************

Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0

"""
import re 

cpf = str(input('Digite o seu CPF: '))

correção_1 = cpf.replace('.', '').replace('-', '')
correção_2 = re.sub(r'[^0-9]', '', correção_1)

nove_digitos = correção_2[:9]


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

    resultado_1 = (soma_1 * 10) % 11
    
    if resultado_1 <= 9:
        novo_cpf.append(str(resultado_1))
    else:
        novo_cpf.append('0')

    cpf_2_dig = novo_cpf[0] + novo_cpf[1]

    for numeros in cpf_2_dig:
        multi_2 = int(numeros) * count_2
        soma_2 = soma_2 + multi_2
        count_2 = count_2 - 1
    
    resultado_2 = (soma_2 * 10) % 11
    
    if resultado_2 > 9:
        novo_cpf.append('0')
    else:
        novo_cpf.append(str(resultado_2))

    cpf_completo = novo_cpf [0] + novo_cpf[1] + novo_cpf[2]
    print(f'Os dois últimos digitos do seu cpf é {resultado_1, resultado_2}')
    print(f'CPF: {cpf_completo}')

except:
    print('Digite apenas números!')


