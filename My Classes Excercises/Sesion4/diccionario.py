# programa para uso de diccionarios
Usuario = {
    'usuario' : 'alicia',
    'correo' : 'alicia@gmail.com',
    'edad' : 30,
}

print('Usuario: ', Usuario['usuario'])
print('Correo: ', Usuario['correo'])
print('Edad: ', Usuario['edad'])

# modificar elementos
Usuario['usuario'] = 'alicia20'
print(Usuario)

# agregar elementos
Usuario['telefono'] = '12345678'
print(Usuario)

# eliminar elementos
Usuario.pop('edad')
print(Usuario)

for llave in Usuario.keys() :
    print('llave: ', llave)

for valor in Usuario.values() :
    print('valor: ', valor)

for llave, valor in Usuario.items() :
    print(f'llave: {llave}, valor: {valor}')

# Tamaño del diccionario 
print(len(Usuario))

