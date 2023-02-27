# Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add('Samuel')
# s1.update('Oliveira') # adiciona as letras separadas no set
s1.update(('Oliveira', 1, 2)) # adiciona a frase
print(s1) # adiciona um elemento por vez
# s1.clear() - limpa o set
s1.discard('Samuel') # precisa informar o valor que será descartado, justamento porque não possui índices


