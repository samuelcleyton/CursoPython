# Exemplo de uso do  tipo set

letras = set()

while True:
    letra = input('Digite uma letra: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('Parabéns')
        break

    print(letras)
