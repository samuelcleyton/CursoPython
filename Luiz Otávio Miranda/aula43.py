"""
Introdução ao for / in
A diferença entre o while e o for, é quando não sabemos definir quando o código acaba (enquanto for verdadeiro), 
o for precisa de um intervalo.

"""

texto = 'Python'
novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
print(novo_texto)

