# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. 
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
# O valor da prestação mensal não pode ser superior a 30% do salário.
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

casa = int(input('Digite o valor da casa que você vai comprar: '))
salario = int(input('Digite o valor do seu salário: '))
anos = int(input('Em quantos anos você pretende pagar? '))

meses = anos * 12
prestação = casa / meses
aprovado = prestação > 0.30 * salario

if prestação < salario * 0.30:
    print('Parabéns, seu empréstimo foi concedido!')
else:
    print('Infelizmente o seu empréstimo foi negado!')
print('O valor da prestação será de {} reais'.format(prestação))
