# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
while True:
    nota = int(input('Qual foi a sua nota? '))
    if nota > 10:
        print('Valor inválido!')
    else:
        print('Nota registrada, obrigado!')
        break
