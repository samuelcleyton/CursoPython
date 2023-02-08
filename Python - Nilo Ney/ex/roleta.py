import random

numeros_sorteados = []
for i in range(5):
    num = int(input("Digite o número sorteado: "))
    numeros_sorteados.append(num)

# Identifica se o número é preto ou vermelho
pretos = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
vermelhos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

# Identifica se o número está na 1ª, 2ª ou 3ª dúzia
primeira_duzia = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
segunda_duzia = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
terceira_duzia = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

# Identifica se o número está na 1ª, 2ª ou 3ª coluna
primeira_coluna = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
segunda_coluna = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
terceira_coluna = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]

pares = 0
impares = 0
vermelhos_count = 0
pretos_count = 0
primeira_duzia_count = 0
segunda_duzia_count = 0
terceira_duzia_count = 0
primeira_coluna_count = 0
segunda_coluna_count = 0
terceira_coluna_count = 0

for num in numeros_sorteados:
    if num in pretos:
        pretos_count += 1
    else:
        vermelhos_count += 1
    if num in primeira_duzia:
        primeira_duzia_count += 1
    elif num in segunda_duzia:
        segunda_duzia_count += 1
    else:
        terceira_duzia_count += 1
    if num in primeira_coluna:
        primeira_coluna_count += 1
    elif num in segunda_coluna:
        segunda_coluna_count += 1
    else:
        terceira_coluna_count += 1
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

probabilidade_pares = pares / 5
probabilidade_impares = impares / 5
probabilidade_pretos = pretos_count / 5
probabilidade_vermelhos = vermelhos_count / 5
probabilidade_primeira_duzia = primeira_duzia_count / 5
probabilidade_segunda_duzia = segunda_duzia_count / 5
probabilidade_terceira_duzia = terceira_duzia_count / 5
probabilidade_primeira_coluna = primeira_coluna_count / 5
probabilidade_segunda_coluna = segunda_coluna_count / 5
probabilidade_terceira_coluna = terceira_coluna_count / 5

# Gera o próximo número baseado nas probabilidades calculadas
sorteio = random.uniform(0, 1)
if sorteio < probabilidade_pares:
    # Gera número par
    while True:
        proximo_numero = random.randint(0, 36)
        if proximo_numero % 2 == 0:
            break
else:
    # Gera número ímpar
    while True:
        proximo_numero = random.randint(0, 36)
        if proximo_numero % 2 != 0:
            break

if proximo_numero in pretos:
    cor = "Preto"
else:
    cor = "Vermelho"

if proximo_numero in primeira_duzia:
    duzia = "1ª"
elif proximo_numero in segunda_duzia:
    duzia = "2ª"
else:
    duzia = "3ª"

if proximo_numero in primeira_coluna:
    coluna = "1ª"
elif proximo_numero in segunda_coluna:
    coluna = "2ª"
else:
    coluna = "3ª"

print("O próximo número sorteado será o", proximo_numero, "que é", cor, "da", duzia, "dúzia e da", coluna, "coluna.")

