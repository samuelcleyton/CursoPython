"""
https://docs.python.org/pt-br/3/library/stdtypes.html

Imutáveis que vimos: str, int, float, bool
Os tipos primitivos são imutáveis, não conseguimos mudar o valor 
"""


string = 'samuel'
string1 = f'{string[:]}kleyton'
print(string1)

# métodos de strings

print(string.capitalize()) # Primeira letra maiúscula
print(string.zfill(10)) # acrescenta zeros a esquerda

