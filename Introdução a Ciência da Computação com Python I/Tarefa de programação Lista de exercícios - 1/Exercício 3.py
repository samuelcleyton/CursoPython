''' Escreva um programa que receba (entrada de dados através do teclado) o nome do cliente, o dia de vencimento, o mês de vencimento e o valor da fatura  e imprima (saída de dados) a mensagem com os dados recebidos, 
no mesmo formato da mensagem: 

Olá, Fulano de Tal
A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada. '''

nome = input('Digite o nome do cliente: ')
dia = input('Digite o dia de vencimento: ')
mês = input('Digite o mês de vencimento: ')
valor = input('Digite o valor da fatura: ')

print(f'Olá, {nome}')
print(f'A sua fatura com vencimento em {dia} de {mês} no valor de R$ {valor} está fechada.')