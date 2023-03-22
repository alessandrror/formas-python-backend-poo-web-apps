# programa para uso de operadores aritmeticos

a = 10
b = 3

# precedencia
# ()
# **
# * / // %
# + -
# igual precedencia? asociatividad por izquierda

print('la suma de a y b es:', a+b)
print('la resta de a y b es:', a-b)
print('la multiplicacion de a y b es:', a*b)
print('la division de a y b es:', a/b)
print('la division entera de a y b es:', a//b)
print('el modulo de a y b es:', a%b)
print('la potencia de a elevado a la b es:', a**b)
print('aplicando precedencia', (4+5)*2**2)
print('aplicando precedencia', 4+5*2**2)
print('aplicando precedencia', 4*5/2)