# CONSTANTE = "Variáveis" que não vão mudar
# Muitas condições no mesmo if (ruim) - muito complexo
# O código precisa ser fácil para ser lido

velocidade = 61 # velocidade atual do carro
km = 90 # o local que o carro está na estrada

radar_1 = 60 # velocidade máxima do radar
local_1 = 100 # km onde o radar 1 está
radar_range = 1 # A distância onde o radar pega, entre 99 km e 101 km, seria multado

km_radar_1 = velocidade > radar_1
carro_passou = km >= (local_1 - radar_range) and km <= (local_1 + radar_range)
carro_multado = carro_passou and km_radar_1

if km_radar_1:
    print('Velocidade do carro quando passou no radar')
if carro_passou:
    print('Carro passou no radar')
if carro_multado:
    print('O carro multado no radar')



