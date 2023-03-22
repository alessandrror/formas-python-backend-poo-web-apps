# programa para uso de operadores de autoasignacion

numero = input('Digite un numero: ')
print('El numero digitado es: ' + numero)
print('El numero digitado es de tipo: ', type(numero))
numero = int(numero) #flot() str() boolean()
print('El numero digitado es de tipo: ', type(numero))

numero += 5 # numero = numero + 5
print(numero) #15
numero -= 5 # numero = numero + 5
print(numero) #10
numero *= 5 # numero = numero + 5
print(numero) #50
numero /= 5 # numero = numero + 5
print(numero) #10.0

# TODO: implementar los operadores faltantes **=, //*, %=
numero **= 5 # numero = numero + 5
print(numero) #100000.0
numero //= 5 # numero = numero + 5
print(numero) #20000.0
numero %= 5 # numero = numero + 5
print(numero) #0.0