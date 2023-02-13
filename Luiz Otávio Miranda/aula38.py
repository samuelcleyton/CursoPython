"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
While dentro de While
"""

qtd_linhas = 5
qtd_colunas = 5

linha = 1 # contador
while linha <= qtd_linhas:
    coluna = 1 # contador
    while coluna <= qtd_colunas:
        print(f'{linha=}, {coluna=}')
        coluna += 1
    linha += 1

print('Acabou!')
