# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]



acertos = 0

questão_1 = perguntas[0]['Pergunta']
print(f'Pergunta: {questão_1}')
print()

print('Opções:')
for x, alternativas in enumerate(perguntas[0]['Opções']):
    print(f'{x}) {alternativas}')
print()

resposta_1 = input('Escolha uma opção: ')

if resposta_1 == '2':
    print('Acertou!')
    acertos = acertos + 1
else:
    print('Errou!')

print()

questão_2 = perguntas[1]['Pergunta']
print(f'Pergunta: {questão_2}')
print()

print('Opções:')
for x, alternativas in enumerate(perguntas[1]['Opções']):
    print(f'{x}) {alternativas}')
print()

resposta_2 = input('Escolha uma opção: ')

if resposta_2 == '0':
    print('Acertou!')
    acertos = acertos + 1
else:
    print('Errou!')

print()

questão_3 = perguntas[2]['Pergunta']
print(f'Pergunta: {questão_3}')
print()

print('Opções:')
for x, alternativas in enumerate(perguntas[2]['Opções']):
    print(f'{x}) {alternativas}')
print()

resposta_3 = input('Escolha uma opção: ')

if resposta_3 == '1':
    print('Acertou!')
    acertos = acertos + 1
else:
    print('Errou!')

print()
print(f'Você acertou {acertos} de 3 perguntas')

