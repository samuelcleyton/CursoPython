# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Escreva um frase: ')).strip().lower()
print('A quantidade de vezes que aparece a letra "a": {} vezes'.format(frase.count('a')))
print('A primeira letra "a" apareceu na {} posição'.format(frase.find('a')+1))
print('A última letra "a" apareceu na {} posição'.format(frase.rfind('a')+1))


