# programa de operadores logicos
# todos tienen igual jerarquia
# solo aplica la asociatividad 
# de izquierda a derecha

a = 10
b = 5
c = 15

print(a<b and c>=a or a!=b)
# 0 and 1 or 1
# 0 or 1
# 1 = true

print(a<b and (c>=a or a!=b))
# 0 and (1 or 1)
# 0 and 1
# 0 = false

print(not False)
print(not True)