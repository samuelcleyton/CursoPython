# Execute o programa (listagem 5.14) para os seguintes valores: 501, 745, 384, 2, 7 e 1.
# Contagem de Cédulas

valor = int(input('Digite o valor a pagar: '))
cédulas = 0
atual = 50
apagar = valor

while True:
    if atual <= apagar:
        apagar = apagar - atual
        cédulas = cédulas + 1
    else:
        print('{} cédula(s) de {}'.format(cédulas, atual))
        if apagar == 0:
            break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cédulas = 0
