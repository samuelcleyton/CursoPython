# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento.

# à vista/dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
print('=' * 10, 'LOJAS AMERICANAS', '=' * 10)
produto = float(input('Qual é o valor do produto? R$ '))
pagamento = str(input("""Qual será a forma de pagamento? 
[1] à vista - dinheiro/cheque
[2] à vista no cartão
[3] em até 2x no cartão
[4] 3x ou mais no cartão \n"""))


if pagamento == '1':
    desconto = produto - (produto * 10/100)
    print('Pagamentos à vista tem 10% de desconto, de R${:.2f} ficará por R${:.2f}'.format(produto, desconto))
elif pagamento == '2':
    desconto = produto - (produto * 5/100)
    print('Pagamentos à vista no cartão tem 5% de desconto, de R${:.2f} ficará por R${:.2f}'.format(produto, desconto))
elif pagamento == '3':
    parcelas = int(input('Quantas parcelas?'))
    if parcelas == '2':
        print('Sua compra será parcelada em 2x de RS{}'.format(produto / 2))
    normal = produto
    print('Em até 2x no cartão, o preço do produto é o mesmo. R${:.2f}.'.format(normal))
elif pagamento == '4':
    parcelas = int(input('Quantas Parcelas? '))
    if parcelas == parcelas:
        print('Sua compra será parcelada em {}x de R${} com juros.'.format(parcelas, (produto / 10)))
    acrescimo = produto + (produto * 20/100)
    print('3x ou mais no cartão tem um acréscimo de 20% no valor da compra, o produto que era R${:.2f} passa a ser '
          'R${:.2f}'.format(produto, acrescimo))
else:
    print('Código Inválido. Tente Novamente!')



