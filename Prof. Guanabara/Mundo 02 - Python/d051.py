# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = termo + (10 - 1) * r
for c in range(termo, decimo + r, r):
    print(c, end=' > ')
print('Acabou')


