'''
Iterando strings com while

'''

nome = 'Samuel'
indice = 0
novo_nome = ''

while indice <= len(nome)-1:
    letra = nome[indice]
    novo_nome += f'*{letra}'    
    indice += 1

print(novo_nome)

