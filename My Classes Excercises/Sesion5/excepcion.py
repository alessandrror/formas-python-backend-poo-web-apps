# print('Inicio de programa...')
# 4/0
# print('Final de programa...')

# print('Inicio de programa...')
# try :
#     4/0
#     print('Mensaje en Try')
# except ZeroDivisionError as e:
#     print('Operación no permitida', e)
# print('Final de programa...')

print('Inicio del programa')

try : 
    a = [1,8,4]
    a[5]
except IndexError as e :
    print('Error de index')
except TypeError as e :
    print('Error de tipos')
except Exception as e :
    print('Ocurrió un error:', e)
finally :
    print('Ocurran o no errores, me imprimiré con Finally')

print('Final del programa')
