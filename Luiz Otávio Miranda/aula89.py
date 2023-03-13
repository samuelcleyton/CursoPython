# dir, hasattr e getattr em Python

string = 'Samuel'
metodo = 'upper'

if hasattr(string, 'upper'): # verifica se existe o método upper na string
    print('existe upper')
    print(getattr(string, metodo)())
else:
    print('não existe o método', metodo)
    