# Escreva um programa para controlar uma pequena máquina registradora.
# Seu programa deve exibir o total das compras depois que o usuário digitar 0.
# Qualquer outro código deve gerar a mensagem de erro "Código inválido".

contador = 0
acumulador = 0
valor = 0

while True:
    produto = int(input('Código do Produto: '))
    quantidade = int(input('Quantidade: '))
    if produto == 1:
        valor = quantidade * 0.5    
    elif produto == 2:
        valor = quantidade * 1.0
    elif produto == 3:
        valor = quantidade * 4.0
    elif produto == 5:
        valor = quantidade * 7.0
    elif produto == 9:
        valor = quantidade * 8.0
    elif produto == 0:
        break
    else:
        print('Código Inválido!')
        continue
    acumulador = acumulador + valor
    contador = contador + 1 
    opcao = input('Deseja adicionar mais um produto? (sim ou 0 para finalizar) ')
    if opcao == '0':
        break    

print('O total da compra é de {} reais.'.format(acumulador))


