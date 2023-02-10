# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = int(input('Base: '))
expoente = int(input('Expoente: '))

resultado = 1  # acumulador

for c in range(expoente):  # quantidade de iterações no laço for. ex.: base 2 e expoente 3
    resultado = resultado * base # resultado = 1, 1 * 2 no 1° laço e assim por diante.

print(resultado)

