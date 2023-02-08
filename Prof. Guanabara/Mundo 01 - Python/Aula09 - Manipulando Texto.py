'''

Fatiamento:
frase = 'Curso em Vídeo Python'
frase[9] = 'V'
frase[9:13] = 'Vide"
frase[9:21] = 'Vídeo Python'
frase{9:21:2] = 'Vdo Pto' - pulando de 2 em dois
frase[:5] = 'Curso'
frase[15:] = 'Python'
frase[9::3] = 'VePh'

Análise:
len(frase) = comprimento da frase
frase.count('o') = contar quantas vezes tem a letra 'o'
frase.count('o', 0, 13) = contar do primeiro índice até o índice 12. resultado: 1

frase.find('deo') = quantas vezes encontrou o 'deo', o resultado será 11 que é a posição de início do 'deo'.
frase.find('Android') = o resultado será -1 porque não encontra esse valor na string
frase.rfind = procura inciando pelo final
'Curso' in frase = existe a palavra 'Curso' em frase? - resultado: True

Transformação:

frase.replace('Python', 'Android') = procura por 'Python' e substuirá o 'Android'
frase.upper() = O que for maiúsculo mantém, o que não for ficará.
frase.lower() = O que for minúsculo mantém, o que não for ficará.
frase.capitalize() = Joga tudo para minúsculo e somente a primeira letra será maiúscula.
frase.title() = Essa função verifica cada espaço na string e as primeiras letras ficarão maiúsculas.
frase.strip() = serve para remover os espaços inúteis na string, remove os primeiros e os últimos.
frase.rstrip() = serve para remover os espaços inúteis na string do lado direito, somente os últimos espaços.
frase.lstrip() = serve para remover os espaços inúteis na string do lado esquerdo, somente os primeiros espaços.

Divisão:
frase.split() = divide uma string em uma lista pelo espaços. 'Curso' palavra 0, 'em' palavra 1...

Junção:
'-'.join(frase) = juntar uma coisa na outra, juntar todos elementos de frase com o separador '-'.

'''

frase = 'Curso em Vídeo Python'
print(frase[0:15:2])