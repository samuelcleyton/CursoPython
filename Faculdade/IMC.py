# Criação de um programa de calculo de IMC, utilizando o programa o Google cloud Shell Editor.

nome = input('Qual é o seu nome? ')
altura = float(input('Qual é a sua altura? '))
peso = int(input('Quanto você pesa? '))

imc = peso / altura ** 2

print(f'{nome} tem {altura:.2f} de altura e pesa {peso} quilos, por tanto seu IMC é {imc:.2f}')
