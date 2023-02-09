# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

# Quantos anos será necessário para que a população A ultrapasse ou iguale a população B.

anos = 0 # contador
A = 80000 # acumulador
B = 200000 # acumulador

while B >= A:
    A = A + (A * 3/100)
    B = B + (B * 1.5/100)
    anos = anos + 1
print(anos)
