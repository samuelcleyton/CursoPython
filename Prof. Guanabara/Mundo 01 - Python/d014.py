# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Digite a temperatura em Celsius: '))
f = c * 9 / 5 + 32
print('A temperatura em Celsius de {}° graus e em Fahrenheit é {}° graus'.format(c, f))

