
print('inicio de programa....')
try:
    4/0
    print('mensaje en try')
except ZeroDivisionError as e:
    print('operacion no permitida', e)

print('intermedio')

try:
    a = [1,8,4]
    a[5]
except IndexError as e:
    print('error de index')
except TypeError as e:
    print('error de tipos')
except Exception as e:
    print('ocurrio un error', e)
finally:
    print('ocurran errores o no aqui estoy')

print('final de programa')