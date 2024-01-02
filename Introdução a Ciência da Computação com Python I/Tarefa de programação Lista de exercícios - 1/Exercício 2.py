# Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética.

nota1 = input('Digite a primeira nota: ')
nota2 = input('Digite a segunda nota: ')
nota3 = input('Digite a terceira nota: ')
nota4 = input('Digite a quarta nota: ')

int_nota1 = float(nota1)
int_nota2 = float(nota2)
int_nota3 = float(nota3)
int_nota4 = float(nota4)

média = (int_nota1 + int_nota2 + int_nota3 + int_nota4) / 4

print(f'A média aritmética é {média:.1f}')