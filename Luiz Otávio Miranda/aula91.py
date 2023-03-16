# Introdução às Generator functions em Python
# generator = (n for n in range (1000000))

def generator(n=0):
    yield 1 # pausar
    print('Continuando...')
    yield 2 # pausar
    print('Mais uma...')
    yield 3
    print('Vou terminar')
    return 'ACABOU'

gen = generator(n=0)
for n in gen:
    print(n)

# Segundo exemplo:

def generator(n = 0, maximum = 10):
    while True:
        yield n
        n += 1

        if n > maximum:
            return

gen = generator(maximum=1000)
for n in gen:
    print(n)