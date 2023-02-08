# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntas = ''.join(palavras)
inverso = ''
#  inverso = juntas[::-1]
for letra in range(len(frase) - 1, -1, -1):
    inverso = inverso + juntas[letra]
print('O inverso de {} é {}.'.format(juntas, inverso))
if inverso == juntas:
    print('Temos um palídromo!')
else:
    print('Não temos um palídromo!')
