# programa para uso de diccionarios
usuario = {
    'usuario': 'alicia', 
    'correo': 'alicia@gmail.com', 
    'edad': 30,
}
print('Usuario:', usuario['usuario'])
print('Correo:', usuario['correo'])
print('Edad:', usuario['edad'])
print(usuario)
# modificar elementos
usuario['usuario'] = 'alicia20'
print(usuario)
# agregar elementos
usuario['telefono'] = '12345678'
print(usuario)
# eliminar elementos
usuario.pop('edad')
print(usuario)
# recorrer un diccionario
for llave in usuario.keys():
    print('llave:', llave)
for valor in usuario.values():
    print('valor:', valor)
for llave,valor in usuario.items():
    print(f'llave: {llave}, valor: {valor}')
# tamano del diccionario
print(len(usuario))