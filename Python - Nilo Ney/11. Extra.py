salario = float(input('Digite o valor do salário: '))
aumento = int(input('Qual a porcentagem de aumento: '))

novo_salario = salario + (salario * aumento / 100)

print(f'Seu sálario era {salario}, mas com o aumento de {aumento}% será {novo_salario:.2f} reais')