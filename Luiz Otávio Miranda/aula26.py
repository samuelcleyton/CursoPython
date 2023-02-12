'''
# Formatação básica de strings
# s - string
# d - int
# f - float
# x ou X - Hexadecimal
(caractere)(><^)(qunatidade)
> - esquerda
< - direita
^ - centro
sinal + ou -
conversion flags - !r !s !a

'''

variavel = 'abc'
print(f'{variavel}')
print(f'{variavel: >10}') # esquerda
print(f'{variavel: <10}') # direita
print(f'{variavel: ^10}') # centro

print(f'{1000.565465468:.1f}')
print(f'O hexadecimal de 1500 é {1500:X}')
print(f'{variavel!r}')





