# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km, e R$ 0,45 para viagens mais longas.

distancia = float(input('Digite a distância da sua viagem: '))
valor = 0
if distancia <= 200:
    valor = distancia * 0.50
    print('O preço da viagem é de {} reais'.format(valor))
else:
    valor1 = distancia * 0.45
    print('O valor da viagem é de {} reais'. format(valor1))
    