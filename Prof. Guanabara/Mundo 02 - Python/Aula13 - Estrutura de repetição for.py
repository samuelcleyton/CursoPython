# laço c no intervalo (1,10)
# for c in range (1, 10):

for c in range(1, 6):  # print de 'Oi' - 5 vezes: (1, 6) - não considera o último número.
    print('Oi')
print('FIM')  # print 'FIM' no final do laço
# se o comando fim estiver no laço, vai repetir também

for c in range(0, 6):  # vai escrever de 0 a 5
    print(c)

for c in range(1, 7):  # vai escrever de 1 até 6
    print(c)

for c in range(6, 0, -1):  # para contar para trás precisa colocar a vírgula e -1.
    print(c)

# a iteração desse programa vai começar no 6 e vai tirar um

for c in range(0, 7):  # vai contar de zero a seis
    print(c)

for c in range(0, 7, 2):  # vai mostrar na tela 0, 2, 4, 6 - contou de 0 a 7 pulando de dois em dois
    print(c)

n = int(input('Digite um número: ')) # utilizar o n para passagem da estrutura for
for c in range(0, n+1):
    print(c)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)

for c in range(0, 3):  # esse for acontece 3x
    n = int(input('Digite um valor: '))

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n  # s += n
print('O somotário de todos os valores foi {}'.format(s))




