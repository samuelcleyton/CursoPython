# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# milhar, centena, dezena e unidade

num = int(input('Digite um valor entre 0 a 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))


# o símbolo // faz a divisão e só pega o que esta antes da vírgula.
# o símbolo % faz a divisão e só pega o que esta depois da vírgula.







