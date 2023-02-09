# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
# Valide a entrada e permita repetir a operação.

população_1 = int(input('Quantidade da primeira população: '))
população_2 = int(input('Quantidade da segunda polução: '))
taxa_1 = float(input('Taxa de crescimento anual da primeira população em %: '))
taxa_2 = float(input('Taxa de crescimento anual da segunda população em %: '))
conversão_1 = taxa_1 / 100
conversão_2 = taxa_2 / 100

anos = 0

if população_1 >= população_2:
    while população_1 > população_2:
        população_1 = população_1 + (população_1 * conversão_1)
        população_2 = população_2 + (população_2 * conversão_2)
        anos = anos + 1
else:
    while população_2 >= população_1:
        população_1 = população_1 + (população_1 * conversão_1)
        população_2 = população_2 + (população_2* conversão_2)
        anos = anos + 1
print('Serão necessários {} anos para que se iguale ou utrapasse a quantidade de pessoas'.format(anos))

