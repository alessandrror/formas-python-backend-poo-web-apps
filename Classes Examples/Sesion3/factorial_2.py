# programa para calculo de factorial
# 5! = 5x4x3x2x1 = 120

numero = int(input("Digite un numero: "))

f = numero
i = 1
while i<numero:
    f*=i
    i+=1

print(f'el factorial de {numero} es: {f}')