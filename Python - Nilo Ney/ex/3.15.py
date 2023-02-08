# Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
# Considere que um fumante perde 10 minutos de vida a cada cigarro.
# Calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

dia = int(input('Quantos cigarros você fuma por dia? '))
anos = int(input('Faz quantos anos que você fuma? '))
pordia = dia * 10
porano = pordia + (pordia * anos * 365)
perdido = porano / 1440
print('Você perdeu até agora %.2f dia(s) de vida pela quantidade de cigarros que consumiu!' % perdido)

# 1 dia fumando eu perco 10 minutos de vida
# 1 ano fumando eu perco 3650 minutos de vida
# 1 dia equivale à 1440 minutos
# 3660 / 1440 = 2,5 dias de vida perdido. 