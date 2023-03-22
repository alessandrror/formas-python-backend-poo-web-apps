u1 = {
    'id': 1,
    'usuario': 'alicia', 
    'correo': 'alicia@gmail.com', 
    'edad': 30,
    'rol': {
        1: 'gerente', 2: 'admin',
    },
}
u2 = {
    'id': 2,
    'usuario': 'beto', 
    'correo': 'beto@gmail.com', 
    'edad': 35,
    'rol': {
        3: 'ventas', 4: 'user', 5: 'rrhh',
    },
}
lista_usuarios = []
lista_usuarios.append(u1)
lista_usuarios.append(u2)
# como imprimo el correo de beto a partir de la lista?
print('correo de beto:', lista_usuarios[1]['correo'])
# como imprimir el rol admin de alicia
print('rol admin de alicia: ', lista_usuarios[0]['rol'][2])
# como imprimir todos los roles de beto (llaves y valores)?
print('roles de beto: ', lista_usuarios[1]['rol'])
for k,v in lista_usuarios[1]['rol'].items():
    print(f'{k}: {v}')