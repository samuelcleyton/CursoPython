# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# s1 = {1, 2, 3, 3, 3, 3, 3, 1} # o set remove valores duplicados
# print(s1)

# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)
# print(l2)

s1 = {1, 2, 3}
print(3 in s1) # 3 está em s1? - True

for numero in s1:
    print(numero)
