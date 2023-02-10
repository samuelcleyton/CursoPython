# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. 

tabuada = int(input('Escolha um número entre o 1 e 10 para mostrar a sua tabuada: '))

for c in range(1, 11):
    print('{} x {:^2} = {}'.format(tabuada, c, tabuada * c))
    
