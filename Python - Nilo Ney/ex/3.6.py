# Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. 
# Para ser aprovado, todas as médias do aluno devem ser maiores que 7.
'''
Considere que o aluno cursa apenas três matérias, 
e que a nota de cada uma está armazenada nas seguintes variáveis: 
matéria1, matéria2, matéria3.
'''
m1 = float(input('Digite a nota da primeira matéria: '))
m2 = float(input('Digite a nota da segunda matéria: '))
m3 = float(input('Digite a nota da terceira matéria: '))
média = (m1 + m2 + m3)/3
print('A sua média foi {}',format(média))
if média > 7:
    print('Você está aprovado, parabéns!')
else:
    print('Você foi reprovado, estude mais! :(')

