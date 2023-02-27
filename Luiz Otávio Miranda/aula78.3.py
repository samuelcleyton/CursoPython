# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 # união
s3 = s1 & s2 # intersecção: o que está presente em ambos
s3 = s1 - s2 # diferença: o unico item presente no primeiro set
s3 = s2 - s1 # diferença: o unico item presente no segundo set
s3 = s1 ^ s2 # diferença simétrica: itens que não estão em abos
print(s3)
