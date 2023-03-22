# programa para calculo de factorial
# 5! = 5x4x3x2x1 = 120

numero = int(input('Digite un numero: '))

f = numero 

# for i in range(1,numero,2: range(inicia, limite, intermitente)
#     print(i*numero)

for i in range(1,numero):
    f*=i # f = f * i

print(f'El factorial de {numero} es: {f}')