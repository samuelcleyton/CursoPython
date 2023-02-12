"""
Flag (Bandeira) = Marcar um local
None = não valor
is e is not = é ou não é (tipo, valor identidade)
id = identidade

"""
v1 = 'a'
v2 = 'a' # id iguais = valores iguais
print(id(v1))

condição = True
passou_no_if = None

if condição:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

print(passou_no_if, passou_no_if is None) 
print(passou_no_if, passou_no_if is not None) 

# is é a mesma coisa que "==", mas utilizamos is com None

# se a condição for verdadeira, será atribuido "True", e o passou no if não é verdadeira - 1° print
# se a condição for falsa, ainda será "None", e o passou no if é verdadeira - 1° print

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
    

