# Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal.
# Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.

dívida = float(input('Valor da dívida? '))
encargos = int(input('Qual o juro mensal em %? '))
pagamento = float(input('Qual valor que será pago mensalmente? '))

mes = 0
pago = 0
juros = encargos / 100
juros_mensal = dívida * juros
pag_juros = 0


while dívida > pago:
    pago = pago + pagamento
    pag_juros = pag_juros + juros_mensal
    dívida = dívida + juros_mensal
    mes = mes + 1

print()
print(f'O valor final da dívida foi R${dívida:.2f}')
print(f'Precisou de {mes} mes(es) para finalizar o débito!')
print(f'O total de juros pagos foi de R${pag_juros:.2f}')
print()


