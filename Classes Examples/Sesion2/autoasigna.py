# programa para uso de operadores de autoasignacion

numero = input('Digite un numero: ')
print('el numero digitado es: '+numero)
print('el tipo del numero digitado es: ', type(numero))

numero = int(numero) # float str boolean
print('el tipo del numero digitado es: ', type(numero))

numero += 5 # numero = numero + 5
print(numero) # 15
numero -= 5 # numero = numero - 5
print(numero) # 10
numero *= 5 # numero = numero * 5
print(numero) # 50
numero /= 5 # numero = numero / 5
print(numero) # 10
# TODO: implementar los operadores faltantes **=, //=, %=
