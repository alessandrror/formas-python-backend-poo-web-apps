# programa para uso de operadores aritmeticos

a = 10
b = 3

# precedencia o jerarquia
# ()
# **
# *, /, //, %
# +, -
# igual precedencia? asociatividad por izquierda

print('la suma de a mas b es: ', a+b)
print('la resta de a menos b es: ', a-b)
print('la multiplicacion de a por b es: ', a*b)
print('la division de a entre b es: ', a/b)
print('la division entera de a entre b es: ', a//b)
print('el modulo de a entre b es: ', a%b)
print('la potencia de a elevado a la b es: ', a**b)
print('aplicando precedencia: ', (4+5)*2**2)
print('aplicando precedencia: ', 4+5*2**2)
print('aplicando precedencia: ', 4*5/2)